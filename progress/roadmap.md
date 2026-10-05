# 個人向けロードマップ

状態：診断前の暫定版。個人の学習時間・既知の内容は未確認。
最初の作業：[初回診断](../docs/assessment/initial-assessment.md)をCoachと実施する。
学習時間や修了日を現時点で保証しない。

| Phase | 内容 | 前提Phase | 到達条件 |
| --- | --- | --- | --- |
| 0 | 環境と学習方法 | なし | H1〜H5と提出方法を説明しHTMLを開く |
| 1 | Web基礎 | 0 | HTML/CSSを変更しHTTPの通信を説明する |
| 2 | Git / GitHub | 0・1 | 差分、コミット、ブランチ、PRの目的を実演 |
| 3 | JavaScript | 1 | 関数・配列・DOM・非同期と失敗処理を実装 |
| 4 | TypeScript | 3 | 型と実行時検証を区別しstrictで小課題を実装 |
| 5 | React | 4 | props/state、フォーム、一覧、非同期状態を実装 |
| 6 | Python基礎 → FastAPI | 3・HTTP | Pythonの関数・型・例外を確認しAPIを実装 |
| 7 | SQL / PostgreSQL | 6 | CRUD、制約、関連、トランザクションを検証 |
| 8 | React + FastAPI | 5・6・7 | TodoをAPIとDBに接続し失敗表示を検証 |
| 9 | 認証 / 認可 | 8 | ログインと所有者によるアクセス制限を検証 |
| 10 | Testing | 8・9 | UI/API/DBの正常・異常・境界テストを自分で設計 |
| 11 | Debugging | 10 | 再現→仮説→調査→修正→回帰確認を実演 |
| 12 | Docker | 8・10 | Composeで再現しDB永続化と設定を確認 |
| 13 | Practical Development | 8〜12 | CRUDアプリで要件からレビューまで完了 |
| 14 | Final Project | 13 | 本人の要件で主要スキルの独立実装を確認 |

## MVPで利用できる教材
- [学習方法](../curriculum/00_orientation/01-learning-method.md)
- [環境と最初のHTML](../curriculum/00_orientation/02-setup.md)
- [HTMLとCSS](../curriculum/01_web_basics/01-html-css.md)
- [HTTPの観察](../curriculum/01_web_basics/02-http.md)
- [フォームと入力](../curriculum/01_web_basics/03-forms.md)
- [Web演習の入口](../exercises/README.md)
- [Todo仕様](../projects/01_todo/README.md)

Phase 2以降の詳細教材は必要時にlesson-authorが作成する。フォルダーがあるだけで教材完成とは扱わない。
Python基礎はcurriculum/06_fastapi/python_basicsに追加する。
テスト・デバッグはPhase 1から観察・確認として導入し、後のPhaseで体系化する。

## 個別調整
現在の優先目標：初回診断と環境確認。
短縮する単元：未決定。実演の根拠がある場合のみCoachが決定する。
補強する単元：未決定。
次へ進む条件：対象範囲の必須課題と評価基準のreadyを確認する。
不足時：説明→小課題→類題の順で再評価する。
