# Todo：API契約 v1

Stage B以降。ベースURL例はhttp://127.0.0.1:8000。JSONを使用する。
Todoはid（正の整数）、title（正規化済み文字列）、completed（boolean）、
created_at（UTCのRFC3339日時）を持つ。IDと日時はサーバーが発行する。

| 操作 | メソッドとパス | 入力 | 成功 |
| --- | --- | --- | --- |
| 一覧 | GET /todos | なし | 200、Todo配列。空は[] |
| 1件取得 | GET /todos/{id} | 正の整数ID | 200、Todo |
| 作成 | POST /todos | title | 201、Todo。completed=false |
| 部分更新 | PATCH /todos/{id} | titleとcompletedの一方または両方 | 200、更新後Todo |
| 削除 | DELETE /todos/{id} | 正の整数ID | 204、本文なし |

一覧はcreated_at降順、同時刻はid降順。フィルターはFrontendで行う。
PATCHで省略した項目は保持し、nullは受け付けない。空オブジェクトは422。
completedはJSONのtrue/falseだけを受け付け、文字列や数値への暗黙変換はしない。
titleは文字列だけを受け付ける。前後空白を除去後1〜100 Unicodeコードポイント。
余分なフィールドは422。学習者はPydantic設定がこの条件を満たすか確認する。

## 失敗
- 不正な入力、無効なID形式、正の整数でないID：422。
- 有効な形式だが対象が存在しないID：404。
- 予期しない内部失敗：500。秘密やスタックトレースをレスポンスに出さない。
- 404の本文は {"detail":"Todo not found"}。
- 422はFastAPIの検証エラー形式を基本にする。項目名と理由を表示できるか確認する。
- 500の本文は {"detail":"Internal server error"}。詳しい原因は秘密を除いたサーバーログで調べる。
- 通信自体の失敗はHTTPステータスが得られない場合もある。

削除の204をJSONとして解析しない。失敗した更新は画面で成功扱いにしない。
例の値を固定するテストだけでなく、無効値と存在しないIDを確認する。

## 契約例（解答コードではない）
作成入力：{"title":"  読書する  "}
応答の例：{"id":1,"title":"読書する","completed":false,"created_at":"2026-10-05T00:00:00Z"}
IDと日時の値は例であり、固定値として実装しない。

## 変更
契約を変える場合は理由、影響する画面、テスト、データへの影響をdocsに記録する。
FrontendとBackendが別々の都合で契約を変えない。
