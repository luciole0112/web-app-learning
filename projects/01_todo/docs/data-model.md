# Todo：データモデル

Stage Cで使う設計。SQLやORMの完成実装は学習者が作成する。

| 項目 | PostgreSQLの型の方針 | 制約 |
| --- | --- | --- |
| id | integer identity等 | 主キー、サーバーが採番 |
| title | varchar(100) | NOT NULL、空白だけを許可しない |
| completed | boolean | NOT NULL、初期値false |
| created_at | timestamptz | NOT NULL、作成日時 |

APIで前後空白を除去し、長さを検証する。DBにも長さと空文字の制約を設ける。
DBの空白判定とPythonのstripの範囲は同一とは限らないため、API境界で正規化を揃える。
通常の作成・更新はトランザクション単位で確定し、失敗時はrollbackする。

SQLiteでは型・日時・booleanの扱いが異なる。PostgreSQLへ移ったら同じテストだけでなく制約も確認する。
新しい空DBからスキーマを再現する手順をREADMEに残す。
マイグレーションの導入はCoachと行い、既存データの削除を代替手順にしない。
テストDBは学習用DBと分ける。テストが本番や学習データを消さないことを確認する。

学習者の説明課題：
主キーが必要な理由、同じタイトルを許可できる理由、
DB保存前の検証とDB制約の両方を使う理由、再起動後も残る仕組みを説明する。
