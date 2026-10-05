# Copilot / VS Codeの対応と制約

公式資料の確認日：2026-10-05。対象はVS CodeのGitHub Copilot。
利用者のVS Codeでの実行・モデルの応答は未検証。ファイルの静的検証とは区別する。

## 採用した形式
- Agentは.github/agents/*.agent.md。nameとdescription、ユーザー選択可能な設定を使う。
- 共通指示は.github/copilot-instructions.md。
- 分野別指示は.github/instructions/*.instructions.md。applyToで対象を指定する。
- Skillは.github/skills/<name>/SKILL.md。nameとdescriptionを持つ。
- モデルは固定しない。利用可能なモデルを選ぶ。

[Custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents)、
[Custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions)、
[Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)を参照。

## Promptの互換性
現行資料ではAgent HostはPrompt filesを読み込まない。Localでは引き続き利用可能とされている。
そのためPromptは補助入口とし、必須経路はAgent選択と自然文依頼にした。
Localでのコマンド名はprompt-create-lesson等。Skillのcreate-lessonと区別して名前衝突を避ける。
Skill呼び出しは担当Agentへ自動変更する機能として扱わない。先に担当Agentを選ぶ。
[Prompt files](https://code.visualstudio.com/docs/agent-customization/prompt-files)

## ツールと権限
実行環境ごとに利用可能なツール名が違うため、このMVPではtoolsの固定一覧を指定していない。
その結果、レビュー担当でも環境上は編集可能な場合がある。
本文の「読み取りと助言のみ」「Coachだけがprogressを更新」は行動ルールであり、強制アクセス制御ではない。
自動承認を広げず、差分を確認する。必要なファイル読み書きができない時は未保存と明示する。
厳密な保護が必要なら担当ごとのツール制限を実機で検証し、進捗更新を権限分離したサービスへ移す。
このMVPのチェックだけでは実際の書き込み主体を証明できない。

## 学習者主体を保つ限界
Custom instructionsはインライン補完には適用されないと公式資料に記載されている。
自力評価ではCopilotのコード補完を無効にし、Chatのヒントも使わず、利用した支援を記録する。
AIがルールに従うことを保証する設定ではない。完成解答が出た場合は支援ありと記録し、別類題で再評価する。

## 役割の切り替え
MVPは手動でAgentを選び、引き継ぎ情報を送る。自動の並列委譲を使わない。
Handoffsは追加可能だが、UIや対応差に依存しないことを優先し、必須設定にしていない。
