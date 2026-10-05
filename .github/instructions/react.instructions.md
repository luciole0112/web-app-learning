---
description: "React・TypeScriptの実装とレビュー"
applyTo: "projects/**/frontend/**,exercises/react/**,exercises/typescript/**"
---

# React・TypeScriptの実装とレビュー

まず学習者にpropsとstateの役割、データの流れ、状態の置き場所を説明してもらう。
関数コンポーネントを基本にし、stateを直接変更しない。一覧のkeyは安定したIDを使う。
不要なeffectや派生状態を増やさず、必要な理由を言語化する。
TypeScriptのstrictを基本とし、anyや強制アサーションでエラーを隠さない。
APIレスポンスの型宣言だけでは実行時検証にならないことを説明する。
読み込み中・空・成功・失敗の表示を設計する。二重送信も考慮する。
フォームにはlabelを付け、キーボード操作とエラーの伝わり方を確認する。
VitestとReact Testing Libraryでは利用者の操作と見える結果を検証する。
テストIDだけに依存せずroleやlabelを優先し、内部stateだけを検証しない。
学習者の代わりにコンポーネント一式を書かず、まず実装方針を確認する。
