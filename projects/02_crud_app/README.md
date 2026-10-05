# Project 2：CRUD Web Application

テーマ例は蔵書管理。本人の題材へ変更してよいが、Coachとスコープを先に固定する。
React / TypeScript / Vite、FastAPI / Pydantic、PostgreSQLを使用する。

## 開始条件
TodoのAPI・DB接続、Git、基本のUI/APIテストを説明・実演できる。
利用者ごとのデータを扱う場合は認証・認可の学習を先に行う。

## 必須成果物
1. docs/requirements.md：利用者、目的、ユーザーストーリー、受け入れ条件、対象外。
2. docs/design.md：画面の状態、関連のある2テーブル以上、制約、API契約、失敗時の動作。
3. frontendとbackend：学習者自身の実装。既存Todoの丸写しではなく差分の理由を説明する。
4. evidence：正常・異常・境界テスト、DB整合性、バグの調査記録、レビュー対応。
5. README：再現手順、設定例、テスト、依存関係、制約。
6. Git/GitHub：小さなコミット、Issueまたは課題記録、PRとレビューの練習。

## 進め方
要件を1つ選び、DB→API→画面→テストの一連の動きを小さく完成させる。
関連データの削除方針と失敗時の整合性を設計する。
各区切りでCoachが評価し、不足すれば追加課題へ戻る。

## 完了条件
新規のPostgreSQLで再現でき、要求と検証が対応し、本人が設計理由を説明できる。
公開は任意。GitHubへ送る前に秘密と個人情報を確認する。
アプリの完成コードはこのRepositoryにはあらかじめ含めない。
