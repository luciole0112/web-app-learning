# Repository構成

Step 3〜12のMVPファイルを実装済みです。以下は実際の構成です。
.gitkeepは空フォルダーをGitで保存するためのファイルで、図からは省略しています。
Phase 2以降のフォルダーがあることは詳細教材の完成を意味しません。

## 全体構成

```text
web-app-learning/
├─ .github/
│  ├─ agents/
│  │  ├─ code-reviewer.agent.md
│  │  ├─ curriculum-designer.agent.md
│  │  ├─ debugger.agent.md
│  │  ├─ exercise-designer.agent.md
│  │  ├─ learning-coach.agent.md
│  │  └─ lesson-author.agent.md
│  ├─ instructions/
│  │  ├─ curriculum.instructions.md
│  │  ├─ database.instructions.md
│  │  ├─ fastapi.instructions.md
│  │  ├─ project.instructions.md
│  │  └─ react.instructions.md
│  ├─ prompts/
│  │  ├─ assess-progress.prompt.md
│  │  ├─ create-curriculum.prompt.md
│  │  ├─ create-exercise.prompt.md
│  │  ├─ create-lesson.prompt.md
│  │  ├─ debug.prompt.md
│  │  └─ review.prompt.md
│  ├─ skills/
│  │  ├─ assess-progress/
│  │  │  └─ SKILL.md
│  │  ├─ build-learning-material/
│  │  │  └─ SKILL.md
│  │  ├─ create-curriculum/
│  │  │  └─ SKILL.md
│  │  ├─ create-exercise/
│  │  │  └─ SKILL.md
│  │  ├─ create-lesson/
│  │  │  └─ SKILL.md
│  │  ├─ debug/
│  │  │  └─ SKILL.md
│  │  └─ review/
│  │     └─ SKILL.md
│  └─ copilot-instructions.md
├─ curriculum/
│  ├─ 00_orientation/
│  │  ├─ 01-learning-method.md
│  │  └─ 02-setup.md
│  ├─ 01_web_basics/
│  │  ├─ 01-html-css.md
│  │  ├─ 02-http.md
│  │  └─ 03-forms.md
│  ├─ 02_git_github/
│  ├─ 03_javascript/
│  ├─ 04_typescript/
│  ├─ 05_react/
│  ├─ 06_fastapi/
│  │  └─ python_basics/
│  ├─ 07_database/
│  ├─ 08_react_fastapi/
│  ├─ 09_authentication/
│  ├─ 10_testing/
│  ├─ 11_debugging/
│  ├─ 12_docker/
│  ├─ 13_practical_development/
│  └─ README.md
├─ docs/
│  ├─ assessment/
│  │  ├─ initial-assessment.md
│  │  └─ rubric.md
│  ├─ acceptance-checklist.md
│  ├─ architecture.md
│  ├─ compatibility.md
│  ├─ getting-started.md
│  ├─ learning-policy.md
│  ├─ publishing.md
│  ├─ repository-structure.md
│  ├─ session-protocol.md
│  └─ validation.md
├─ exercises/
│  ├─ database/
│  │  ├─ submissions/
│  │  └─ tasks/
│  ├─ fastapi/
│  │  ├─ submissions/
│  │  └─ tasks/
│  ├─ fullstack/
│  │  ├─ submissions/
│  │  └─ tasks/
│  ├─ javascript/
│  │  ├─ submissions/
│  │  └─ tasks/
│  ├─ python/
│  │  ├─ submissions/
│  │  └─ tasks/
│  ├─ react/
│  │  ├─ submissions/
│  │  └─ tasks/
│  ├─ typescript/
│  │  ├─ submissions/
│  │  └─ tasks/
│  ├─ web/
│  │  ├─ submissions/
│  │  └─ tasks/
│  │     ├─ ORI-001.md
│  │     ├─ ORI-002.md
│  │     ├─ WEB-001.md
│  │     ├─ WEB-002.md
│  │     ├─ WEB-003.md
│  │     ├─ WEB-004.md
│  │     ├─ WEB-005.md
│  │     └─ WEB-006.md
│  └─ README.md
├─ progress/
│  ├─ README.md
│  ├─ assessments.md
│  ├─ history.md
│  ├─ learner-profile.md
│  ├─ progress.md
│  └─ roadmap.md
├─ projects/
│  ├─ 01_todo/
│  │  ├─ backend/
│  │  ├─ docs/
│  │  │  ├─ acceptance.md
│  │  │  ├─ api-contract.md
│  │  │  ├─ data-model.md
│  │  │  └─ requirements.md
│  │  ├─ evidence/
│  │  ├─ frontend/
│  │  └─ README.md
│  ├─ 02_crud_app/
│  │  ├─ backend/
│  │  ├─ docs/
│  │  ├─ evidence/
│  │  ├─ frontend/
│  │  └─ README.md
│  ├─ final_project/
│  │  ├─ backend/
│  │  ├─ docs/
│  │  ├─ evidence/
│  │  ├─ frontend/
│  │  └─ README.md
│  └─ README.md
├─ scripts/
│  └─ validate_repository.py
├─ .gitignore
└─ README.md
```

## 保存規則
- curriculum：lesson-authorが教材を作成する。
- exercisesのtasks：exercise-designerが課題を書く。
- exercisesのsubmissions：学習者が回答・コード・証拠を保存する。
- projectsのdocs：要件と設計。frontend/backend：学習者の実装。evidence：検証とレビュー。
- progressの5ファイル：learning-coachだけが確定状態を更新する。
- docs/assessment：診断の問題と評価基準。実施結果はprogressへ記録する。

## 構成の理由
PythonとDatabaseの演習先を追加し、それぞれの基礎練習を分けています。
Python教材は06_fastapi/python_basicsに置き、標準のPhase番号を維持します。
Phase 14はprojects/final_projectを入口とし、教材の二重管理を避けます。
課題文と回答、設計と実装、診断問題と診断結果を分け、評価の根拠を追えるようにしています。

## 設定の責任
共通原則はcopilot-instructions、役割はAgent、分野ごとの判断はInstructionsに置きます。
教材作成の共通手順はbuild-learning-materialです。
Promptは対応Skillへの入口で、Local向けコマンド名にはprompt-を付けています。
Skillを使うだけで担当Agentや権限が切り替わるとは扱いません。
仕様上の理由と代替案は[互換性](compatibility.md)を参照してください。

## 命名と参照
教材はLESSON-WEB-001、課題はWEB-001、セッションはSESSION-YYYYMMDD-NN、
評価はASSESS-YYYYMMDD-NNのように識別します。
作成前に重複を確認し、タイトルを変えてもIDを維持します。
提出は課題ID/attempt-01、再提出はattempt-02とし、過去の証拠を残します。
Markdownの内部リンクはRepository内の相対パスを使用します。

## 完成範囲
Copilot設定、初期教材5本、演習8本、Todo仕様、診断、進捗初期状態を作成済みです。
詳細な後続教材とアプリの実装はこれから学習者と進めます。
ローカルGitを初期化し、[GitHub](https://github.com/luciole0112/web-app-learning)へ公開済みです。
ZIPには.git履歴を含めないため、展開した場合は[保存手順](publishing.md)で初期化します。
