# 実践プロジェクト

| プロジェクト | 学習内容 |
| --- | --- |
| [Todo](01_todo/README.md) | Reactの状態管理からAPI・DBへ段階的に拡張 |
| [CRUDアプリ](02_crud_app/README.md) | 要件、DB、API、UIの設計からテストまで |
| [最終プロジェクト](final_project/README.md) | 自分の要件から認証・Dockerを含む完成まで |

各プロジェクトのdocsは要件・設計、frontendとbackendは学習者の実装、
evidenceはテスト・デバッグ・レビューの証拠を保存する場所です。
backendのテストはbackend/tests、frontendのテストは対象ソースの近くに置く方針です。
実装時に必要な構成を作成し、今は動かない空のアプリ設定を作りません。

Dockerfileやcompose.yamlはDocker導入時にプロジェクトごとに追加します。
依存関係と起動手順もプロジェクトごとに管理し、ルートに共通アプリを作りません。

