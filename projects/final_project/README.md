# Final Project：自分の要件で完成させる

Phase 14 / プロジェクトID: PROJ-FINAL-001。
テーマは学習者が決める。誰のどんな困りごとを解くかから始める。
使用技術：React / TypeScript / Vite、FastAPI / Pydantic、PostgreSQL、
Vitest / React Testing Library / pytest、Docker Compose、Git / GitHub。

## 設計から完成まで
| 段階 | 学習者の提出物 | 通過条件 |
| --- | --- | --- |
| 要件 | docs/requirements.md | 利用者、目的、ストーリー、優先度、対象外、受け入れ条件 |
| 画面 | docs/ui.md | 一覧・入力・詳細と、読み込み・空・失敗状態 |
| データ | docs/database.md | 関連、制約、所有者、移行方法、削除方針 |
| API | docs/api.md | メソッド、入力、応答、ステータス、認証・認可 |
| 実装 | frontend、backend | 学習者が小さな差分で説明できる |
| 認証 | docs/auth.md | ログイン、ログアウト、失効、保存方式、所有者チェック |
| 検証 | evidence/tests.md | 正常・異常・境界、他人のデータ操作拒否、実DB連携 |
| デバッグ | evidence/debug.md | 再現、仮説、調査、根拠、修正、回帰確認 |
| レビュー | evidence/review.md | 指摘の理由、対応、残る制約 |
| 再現 | Dockerfileとcompose.yaml、README | 別の新規環境で起動でき、DBデータが残る |
| 完成 | docs/completion.md | 受け入れ条件と証拠の対応、未解決事項、自己評価 |

## 認証の設計
認証は本人確認、認可は何を操作できるかの判定。UIでボタンを隠すだけでは認可にならない。
方式は脅威と要件から選び、Cookie方式ならCSRF等、トークン方式なら保管・失効等を確認する。
暗号やパスワード保存方式を独自に発明しない。
実装時に[FastAPI公式のセキュリティ教材](https://fastapi.tiangolo.com/tutorial/security/)など、
採用方式の公式資料を確認して選定理由を書く。チュートリアルをそのまま本番品質と見なさない。

## 完成の判定
- 本人が要件からテストまで一貫して説明できる。
- 全必須条件の証拠があり、未確認を成功としない。
- 認証済みの他利用者による閲覧・更新・削除拒否をAPIテストで確認する。
- Docker起動とDB永続化、設定例、依存関係固定、秘密情報の除外を確認する。
- GitHubで変更とレビューを追える。公開リポジトリやインターネット公開は必須ではない。
- Coachが主要スキルのIndependent 4以上を別類題の変更・デバッグで確認する。
- H4/H5を使った箇所も正直に記録し、それだけで自立認定しない。

最初の質問：「誰が、今どんな不便を感じ、どの操作ができれば役に立ちますか。」
最初から全ファイルをAIに生成させず、最初のストーリーを自分で選ぶ。
