"""Static validation of our restricted frontmatter; not a general YAML parser.
Python 3.10+, standard library only. Does not execute Copilot or learner apps.
"""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(ok, message):
    if not ok:
        errors.append(message)
def read(path):
    return path.read_text(encoding="utf-8")
def metadata(path):
    text = read(path)
    check(text.startswith("---\n"), f"{path.name}: missing frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        errors.append(f"{path.name}: unclosed frontmatter")
        return {}
    result = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9-]*):\s*(.+)", line)
        if not match:
            errors.append(f"{path.name}: unsupported metadata line: {line}")
            continue
        key, raw = match.groups()
        check(key not in result, f"{path.name}: duplicate metadata {key}")
        try:
            if raw.startswith('"') or raw in ("true", "false"):
                value = json.loads(raw)
            else:
                check(bool(re.fullmatch(r"[a-z0-9-]+", raw)),
                      f"{path.name}: unsupported plain value")
                value = raw
            result[key] = value
        except ValueError:
            errors.append(f"{path.name}: invalid quoted value")
    return result

agents = ["learning-coach", "curriculum-designer", "lesson-author",
          "exercise-designer", "debugger", "code-reviewer"]
workflows = ["create-curriculum", "create-lesson", "create-exercise",
             "assess-progress", "debug", "review"]
owners = dict(zip(workflows, ["curriculum-designer", "lesson-author",
                             "exercise-designer", "learning-coach",
                             "debugger", "code-reviewer"]))
required = ["README.md", ".gitignore", ".github/copilot-instructions.md",
            "docs/architecture.md", "docs/repository-structure.md",
            "docs/getting-started.md", "docs/compatibility.md",
            "docs/assessment/initial-assessment.md", "docs/assessment/rubric.md",
            "docs/session-protocol.md", "docs/acceptance-checklist.md",
            "projects/01_todo/docs/requirements.md",
            "projects/01_todo/docs/api-contract.md",
            "projects/01_todo/docs/data-model.md",
            "projects/01_todo/docs/acceptance.md"]
required += [f"progress/{n}.md" for n in
             ["learner-profile", "roadmap", "progress", "assessments", "history"]]
required += [f".github/agents/{n}.agent.md" for n in agents]
required += [f".github/instructions/{n}.instructions.md" for n in
             ["curriculum", "react", "fastapi", "database", "project"]]
required += [f".github/prompts/{n}.prompt.md" for n in workflows]
required += [f".github/skills/{n}/SKILL.md" for n in
             ["build-learning-material"] + workflows]
for name in required:
    check((ROOT / name).is_file(), f"missing: {name}")

md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
fence = chr(96) * 3
for path in md_files:
    text = read(path)
    check(bool(text.strip()), f"empty Markdown: {path.relative_to(ROOT)}")
    prose = re.sub(r"^" + fence + r"[^\n]*\n.*?^" + fence + r"[ \t]*$", "",
                   text, flags=re.M | re.S)
    for href in re.findall(r"!?\[[^\]]*\]\(([^)\n]+)\)", prose):
        href = href.strip().strip("<>")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", href) or href.startswith("#"):
            continue
        target = unquote(href.split("#", 1)[0])
        check((path.parent / target).exists(),
              f"broken link: {path.relative_to(ROOT)} -> {href}")

for name in agents:
    path = ROOT / f".github/agents/{name}.agent.md"
    if path.exists():
        meta = metadata(path)
        check(meta.get("name") == name, f"agent name mismatch: {name}")
        check(bool(meta.get("description")), f"agent description missing: {name}")
        check(meta.get("user-invocable") is True, f"agent hidden: {name}")
        check(meta.get("disable-model-invocation") is True,
              f"unexpected automatic invocation: {name}")
        check("tools" not in meta, f"review compatibility before tools override: {name}")

for path in (ROOT / ".github/instructions").glob("*.instructions.md"):
    meta = metadata(path)
    check(bool(meta.get("applyTo")), f"applyTo missing: {path.name}")
    check(bool(meta.get("description")), f"description missing: {path.name}")

for name in workflows:
    path = ROOT / f".github/prompts/{name}.prompt.md"
    if path.exists():
        meta = metadata(path)
        check(meta.get("name") == "prompt-" + name, f"prompt collision: {name}")
        check(meta.get("agent") == owners[name], f"prompt owner mismatch: {name}")
        check("tools" not in meta, f"prompt overrides tools: {name}")

for path in (ROOT / ".github/skills").glob("*/SKILL.md"):
    meta = metadata(path)
    check(meta.get("name") == path.parent.name, f"skill name mismatch: {path}")
    check(bool(re.fullmatch(r"[a-z0-9-]{1,64}", str(meta.get("name", "")))),
          f"invalid skill name: {path}")
    desc = meta.get("description", "")
    check(isinstance(desc, str) and 0 < len(desc) <= 1024,
          f"invalid skill description: {path}")

lesson_headings = ["この教材で学ぶこと", "前提知識", "なぜ必要なのか",
                   "基礎概念", "具体例", "コード例", "実践", "演習",
                   "理解度チェック", "よくある間違い",
                   "実務ではどう使うか", "まとめ", "次に学ぶこと"]
exercise_headings = ["目的", "前提知識", "課題", "制約", "ヒント",
                     "完了条件", "チェックポイント", "発展課題"]
lessons = [p for p in (ROOT / "curriculum").rglob("*.md") if p.name != "README.md"]
exercises = list((ROOT / "exercises").glob("*/tasks/*.md"))
check(len(lessons) >= 5, "MVP requires at least five concrete lessons")
check(len(exercises) >= 8, "MVP requires at least eight initial exercises")
ids = set()
for path, headings, label in (
    [(p, lesson_headings, "教材ID") for p in lessons]
    + [(p, exercise_headings, "課題ID") for p in exercises]
):
    text = read(path)
    actual = re.findall(r"^## (.+)$", text, re.M)
    check(actual == headings, f"headings/order: {path.relative_to(ROOT)}")
    match = re.search(label + r": ([A-Z0-9-]+)", text)
    check(bool(match), f"missing ID: {path.relative_to(ROOT)}")
    if match:
        ident = match.group(1)
        check(ident not in ids, f"duplicate ID: {ident}")
        ids.add(ident)
levels = set()
for path in exercises:
    match = re.search(r"難易度: L([1-5])", read(path))
    if match:
        levels.add(match.group(1))
    else:
        errors.append(f"missing difficulty: {path.name}")
check(levels == set("12345"), "exercise levels must cover L1 through L5")

progress = ROOT / "progress/progress.md"
if progress.exists():
    for line in read(progress).splitlines():
        if not line.startswith("|") or "---" in line or "| Skill |" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        check(len(cells) == 8, f"progress row shape: {line}")
        if len(cells) == 8:
            check(all(x in "012345" and len(x) == 1 for x in cells[1:4]),
                  f"invalid scores: {line}")
            check(cells[4] in {"not_started", "learning", "ready", "independent", "revisit"},
                  f"invalid progress status: {line}")
check(len(list((ROOT / ".github/agents").glob("*.md"))) == 6,
      "unexpected Markdown in agent directory")
if errors:
    print("FAIL")
    print("\n".join("- " + e for e in errors))
    sys.exit(1)
print(f"PASS: {len(required)} required files; {len(md_files)} Markdown files; "
      f"{len(lessons)} lessons; {len(exercises)} exercises; local links and metadata.")
print("Not tested: Copilot discovery/behavior, learner implementations, remote links.")
