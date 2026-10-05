# Web App Learning

**GitHub Copilotと一緒に、自分でWebアプリを完成させる力を育てる学習環境です。**

Web開発初心者を対象に、基礎・設計・実装・テスト・デバッグ・レビューを段階的に学びます。
教材、演習、実践プロジェクト、学習記録、Copilotの設定をこのRepositoryで管理します。

AIは質問、ヒント、説明、レビューを担当します。学習者は自分で考え、コードを書き、動作を確かめます。

## まずはここから

### 1. フォルダーを開く

ZIPを入手した場合は展開し、VS Codeの「フォルダーを開く」で **web-app-learning** を開いてください。
このREADME.mdと.githubが同じ階層に見えれば、正しい場所です。

### 2. Copilotでlearning-coachを選ぶ

GitHub CopilotのChatを使える状態にし、Agent一覧で **learning-coach** を選択します。
見つからない場合は[開始ガイド](docs/getting-started.md)を確認してください。

### 3. 最初のメッセージを送る

次の文章をコピーして送れます。

> 今日の学習を始めたいです。progressの5ファイルを確認し、未診断なら初回スキル診断を一問ずつ進めてください。私が回答する前に正解や完成コードを出さず、最初に取り組む課題を1つ決めてください。

使える時間や経験を聞かれたら、自分の状況を答えてください。
知らないことは「分からない」で構いません。診断は、適切な開始地点を決めるために行います。

次回は同じAgentに「前回の続きから始めたい」と伝えます。

## 最初に必要なもの

| 道具 | 用途 |
| --- | --- |
| VS Code | 教材を読み、ファイルを編集する |
| Webブラウザー | 作ったページと通信を確認する |
| GitHub Copilotを利用できる環境 | Coachや専門Agentと学習する |

教材を読むだけならCopilotがなくても始められます。Agentによる指導にはCopilotが必要です。
Git、Node.js、Python、PostgreSQL、Dockerは、使う段階で導入します。
HTTPの実習にはPython 3、Repositoryの形式確認にはPython 3.10以上が必要です。

具体的な設定は[開始ガイド](docs/getting-started.md)を参照してください。
学習環境そのものを使うために、ReactやFastAPIのサーバーを起動する必要はありません。

## 1回の学習の流れ

1. **現在地を確認する**：Coachが進捗と前回の未解決点を読む。
2. **今日の目標を決める**：読む教材と完了条件を1つずつ確認する。
3. **理解を確かめる**：予想や説明を自分の言葉で伝える。
4. **演習・実装を行う**：必要な時だけCopilotの支援を使う。
5. **テストとデバッグを行う**：期待と実際の違いを調べる。
6. **レビューを受ける**：改善が必要な理由を説明できるようにする。
7. **評価と記録を行う**：Coachが根拠を確認して進捗を更新する。

理解が不足していれば、補足説明・追加演習・再評価へ戻ります。
教材を読んだことだけで、習得したとは判定しません。

## 最初に使う教材と演習

| 順序 | 教材 | 対応する演習 |
| --- | --- | --- |
| 1 | [AIと一緒に学ぶ方法](curriculum/00_orientation/01-learning-method.md) | [支援の依頼と記録](exercises/web/tasks/ORI-001.md) |
| 2 | [環境と最初のHTML](curriculum/00_orientation/02-setup.md) | [自分のHTMLを開く](exercises/web/tasks/ORI-002.md) |
| 3 | [HTMLとCSS](curriculum/01_web_basics/01-html-css.md) | [趣味の紹介ページ](exercises/web/tasks/WEB-002.md) |
| 4 | [HTTPの観察](curriculum/01_web_basics/02-http.md) | [通信の予測](exercises/web/tasks/WEB-001.md)・[200と404の観察](exercises/web/tasks/WEB-003.md) |
| 5 | [フォームと入力](curriculum/01_web_basics/03-forms.md) | [申込フォーム](exercises/web/tasks/WEB-004.md) |

[演習一覧](exercises/README.md)には、JavaScript学習後に取り組むL4・L5の課題もあります。
番号順にすべて急いで終わらせず、Coachと前提知識を確認して進めてください。

## 学習ロードマップ

| Phase | 学ぶこと |
| --- | --- |
| 0 | 環境構築・AIとの学習方法 |
| 1 | HTML / CSS、ブラウザー、HTTPなどのWeb基礎 |
| 2 | Git / GitHub |
| 3 | JavaScript |
| 4 | TypeScript |
| 5 | React |
| 6 | Pythonの基礎 → FastAPI / Pydantic |
| 7 | SQL / PostgreSQL |
| 8 | React + FastAPIの連携 |
| 9 | 認証・認可 |
| 10 | テスト |
| 11 | デバッグ |
| 12 | Docker / Docker Compose |
| 13 | 実践的なWebアプリ開発 |
| 14 | 自分で要件を考える最終プロジェクト |

テストとデバッグは初期の演習から少しずつ行い、Phase 10・11で体系的に学びます。
診断後の個人向け計画は[roadmap.md](progress/roadmap.md)に記録します。

## Agentの使い分け

Agentは、Copilotに担当する役割と進め方を伝える設定です。

| Agent | 相談すること |
| --- | --- |
| **learning-coach** | 学習開始、理解度確認、評価、次の課題 |
| curriculum-designer | 学習順序、前提知識、難易度の調整 |
| lesson-author | 新しい教材、分かりにくい説明の改善 |
| exercise-designer | 練習問題、補強課題、応用問題 |
| debugger | エラーの再現、原因の調査、再テスト |
| code-reviewer | コードの問題点、改善の理由、確認方法 |

通常はlearning-coachから始めます。
専門Agentを使う時は手動で選び、Coachが整理した情報を渡してください。
専門担当の報告をCoachへ戻し、評価と次の課題を決めます。

**進捗を最終決定・更新するAgentはlearning-coachだけです。**
このルールは指示による運用であり、ファイルへの書き込みを強制的に禁止する仕組みではありません。
更新内容は学習者も確認してください。

## Copilotへの相談例

| 場面 | 依頼の例 |
| --- | --- |
| 方針に迷った | 「この要件に対して私はこう考えました。足りない観点を質問してください」 |
| コードを理解したい | 「この処理を説明してください。その後、理解度を確認する質問を1つください」 |
| エラーが出た | 「期待は○○、実際は△△です。原因候補を教えてください。修正コードはまだ出さないでください」 |
| 手が止まった | 「実装するためのヒントを1段階ずつ出してください」 |
| 実装を確かめたい | 「要件と照らしてレビューし、改善が必要な理由を説明してください」 |

「このアプリ全部作って」と依頼する前に、自分の目標・予想・迷っている点を整理します。

支援の量は次の5段階です。基本はH1〜H3を使います。

| 支援 | 内容 |
| --- | --- |
| H1 | 質問で考える |
| H2 | 着目点のヒント |
| H3 | 設計案・疑似コード |
| H4 | 部分コード |
| H5 | 完成例 |

演習の難易度L1〜L5とは別に記録します。
H4・H5を使った場合は、後で別の類題を自力で解いて確認します。
自力評価中はAIのヒントやインライン補完も使わず、参照した資料を記録してください。

## 回答と実装の保存先

課題文はexercisesのtasks、学習者の回答はsubmissionsに置きます。
例えばWEB-002の最初の提出は次の構成です。

```text
exercises/web/submissions/WEB-002/attempt-01/
├─ answer.md       # 予想・方針・自分の説明
├─ evidence.md     # 手順・期待・実際・使ったAI支援
└─ site/           # 自分で作ったHTMLやCSS
```

再提出はattempt-02などを追加し、前の試行を残します。
実践プロジェクトのコードは各プロジェクトのfrontendとbackendに保存します。

## 進捗は3つの軸で確認する

| 軸 | 確認する力 |
| --- | --- |
| Knowledge | 概念と理由を説明できる |
| Practice | 実装・テスト・デバッグができる |
| Independent | 支援なしで判断し、別の条件にも応用できる |

各軸を0〜5で評価します。共通の目安は、0＝未学習、1＝用語を知る、
2＝説明があれば理解、3＝例を参考に実装、4＝自力で実装、5＝説明・レビューができる、です。
軸ごとの具体的な観察方法は[評価基準](docs/assessment/rubric.md)にあります。

初期値の0は未評価の仮値であり、能力がないと判定したものではありません。
回答、成果物、実行結果、AI支援量を根拠にCoachが評価します。

| ファイル | 記録する内容 |
| --- | --- |
| [learner-profile.md](progress/learner-profile.md) | 目標、経験、学習時間、環境 |
| [roadmap.md](progress/roadmap.md) | 個人向けの学習計画 |
| [progress.md](progress/progress.md) | 現在のスキル状態 |
| [assessments.md](progress/assessments.md) | 評価の根拠と点数の変更理由 |
| [history.md](progress/history.md) | 各回の学習内容と次回の開始位置 |

## 実践プロジェクト

| プロジェクト | 内容 |
| --- | --- |
| [Todoアプリ](projects/01_todo/README.md) | Reactのstate → FastAPI接続 → DB保存の3段階 |
| [CRUD Web Application](projects/02_crud_app/README.md) | 要件・DB・API・UI設計から実装・テスト・レビューまで |
| [Final Project](projects/final_project/README.md) | 自分の要件で認証・認可・テスト・Dockerを含むアプリを完成させる |

FrontendはReact / TypeScript / Vite、BackendはFastAPI / Pydantic、
DBはPostgreSQLを基本にします。初期の小さな課題ではSQLiteも使用できます。
テストにはVitest / React Testing Library / pytestを使います。

完成解答のアプリは同梱していません。学習者が段階的に実装します。

## Repository構成

```text
web-app-learning/
├─ README.md
├─ .github/       # Copilotの共通指示・Agent・Instructions・Prompts・Skills
├─ curriculum/    # Markdown教材
├─ exercises/     # 課題と学習者の回答
├─ projects/      # 実践課題の仕様・設計・実装・証拠
├─ progress/      # 学習者情報・計画・評価・履歴
├─ docs/          # 設計・診断・運用手順
└─ scripts/       # Repositoryの形式確認
```

詳細は[全ディレクトリ構成](docs/repository-structure.md)と[全体設計](docs/architecture.md)を参照してください。

## 現在の完成範囲

MVP（学習を始めるための最小構成）として、次を作成済みです。

- 共通指示、6つのAgent、5つのInstructions、6つのPrompts、7つのSkills
- progressの5ファイル、評価基準、初回スキル診断
- orientationとweb_basicsの具体教材5本
- L1〜L5を含む演習8本
- Todoの要件・API・DB・受け入れ条件
- CRUDアプリと最終プロジェクトの到達条件

Phase 2以降の詳細教材は、必要になった段階でlesson-authorが作成します。
利用者のVS CodeでのCopilotの認識・応答は未検証です。
[検証記録](docs/validation.md)と[初回の手動確認表](docs/acceptance-checklist.md)を参照してください。
GitHub上への公開はまだ行っていません。

## 困ったとき

| 状況 | 確認すること |
| --- | --- |
| learning-coachが見つからない | 開いたフォルダーと設定の認識状態を[開始ガイド](docs/getting-started.md)で確認 |
| Promptが使えない | 対象Agentを選び、同じ依頼を自然文で送る |
| AIが完成解答を出してしまった | 支援ありとして記録し、別の類題で自力確認 |
| コードが動かない | 期待・実際・エラー・再現手順を揃えてdebuggerへ |
| どこから再開するか分からない | Coachにhistoryとroadmapの確認を依頼 |
| 評価に疑問がある | 対象範囲と根拠をCoachに確認し、必要なら訂正評価を残す |

Promptの対応範囲やツール制限などは[仕様上の制約と代替案](docs/compatibility.md)にまとめています。

## Repositoryの形式確認

Python 3.10以上が使える場合、このREADMEがあるフォルダーで実行します。

```sh
python scripts/validate_repository.py
```

追加パッケージは不要です。必須ファイル、内部リンク、見出し、設定の限定形式を確認します。
この検査だけでCopilotの動作や学習者の実装が正しいと判定することはできません。

## GitHubで管理する

[GitHubへの保存手順](docs/publishing.md)に従い、自分のRepositoryへ接続できます。
ZIPにはGit履歴を含まないため、展開して使う場合は初期化から行います。
アップロード前に公開範囲を選び、パスワード・APIキー・個人情報が含まれないことを確認してください。

最初の学習は、[AIと一緒に学ぶ方法](curriculum/00_orientation/01-learning-method.md)から始められます。
