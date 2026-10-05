# Project 1：Todoアプリ

プロジェクトID: PROJ-TODO-001。
Reactのstate→API→DBの順に、同じ機能を育てます。完成解答は含みません。
実装者は学習者です。Coachは前提と完了条件を確認し、小さな作業を1つずつ案内します。

## 目的と前提
CRUD、フォーム、state、HTTP、API契約、DB永続化を学びます。
Stage AはTypeScript・React、BはPython・FastAPI・HTTP、CはSQLを前提にします。
テストは各Stageに含め、テスト教材の全修了まで後回しにしません。

## 進め方
1. [要件と段階](docs/requirements.md)を読み、最初の1操作の方針を説明する。
2. [API契約](docs/api-contract.md)はStage B開始前に説明できるようにする。
3. [DB設計](docs/data-model.md)はStage Cで学ぶ。
4. [確認表](docs/acceptance.md)を使い、結果をevidenceに残す。
5. debuggerとcode-reviewerの指導後、Coachに評価を依頼する。

## 保存先
frontend：React / TypeScript / Vite。backend：FastAPI / Pydantic。
docs：要件と設計。evidence：テスト・デバッグ・レビューと支援量。
パッケージや起動コードは学習者が該当Stageで作成し、実際のバージョンを固定します。

## 最初の依頼
「TodoのStage Aを始めたい。追加したTodoの状態をどこに置くか、自分の案を説明するので質問で確認してください。」

## 起動・テスト
現時点で実行するアプリはありません。実装時にfrontend/backendのREADMEへ、
依存関係の導入、起動、型検査、テスト、DB準備の実際のコマンドを記載します。
例えばnpm testが存在すると推測して実行しないでください。
学習用の単一利用者・ローカル実行が範囲です。公開や複数利用者対応は後続課題です。
