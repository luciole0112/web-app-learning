---
description: "FastAPI・PydanticとPythonの実装・検証"
applyTo: "projects/**/backend/**/*.py,exercises/fastapi/**,exercises/python/**"
---

# FastAPI・PydanticとPythonの実装・検証

Pythonの関数、型ヒント、例外、仮想環境を先に確認する。
入力用と出力用のPydanticモデルを区別し、秘密情報をレスポンスに含めない。
HTTPメソッド、ステータス、入力検証、存在しないIDをAPI契約に記載する。
asyncは速くなる魔法と説明せず、同期DB呼び出しとの組合せを確認する。
CORSは認証や認可ではない。開発用originを限定する。
pytestでは正常系だけでなく、無効入力・不存在・権限違反を確認する。
テスト用DBを分離し、利用者の学習データを消さない。
依存関係を固定し、対象バージョンの公式ドキュメントを確認してAPIを提案する。
学習者が原因と修正方針を説明するまで完成実装を出さない。
