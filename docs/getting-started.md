# 学習の始め方

## 1. 学習ルートを開く
VS Codeでweb-app-learningフォルダーを開きます。
README.mdと.githubが同じ階層に見えることを確認します。
このファイルはdocsの中にあります。

## 2. Copilotを使えることを確認する
GitHubアカウントでサインインし、Copilot Chatを利用できる環境を用意します。
利用できるプラン、組織ポリシー、画面の名称は環境で異なります。
[公式のセットアップ手順](https://code.visualstudio.com/docs/setup/copilot)を確認してください。
このRepositoryがアカウントや有料契約を作成することはありません。

## 3. learning-coachを選ぶ
Chatで使用する実行環境をCopilotにし、Agent一覧からlearning-coachを選びます。
見つからなければChat: Open Customizationsを開き、Agentsに6つのファイルが認識されているか確認します。
選択した実行環境で使えるカスタマイズが表示されます。
認識されなければ、開いたルート、ファイル名、診断エラーを確認します。
通常のChatにAgent本文を貼る方法は暫定代替であり、自動読込が検証できたとは扱いません。

## 4. 初回の依頼
以下をそのまま送れます。

> 今日の学習を始めたいです。progressの5ファイルを確認してください。未診断なら初回スキル診断を一問ずつ進めてください。私が回答する前に正解や完成コードを出さず、今日は最初の課題を1つ決めたいです。

環境や使える時間を聞かれたら、自分の状況を答えます。
初期の0は未評価の仮値です。できないと判定されたわけではありません。

## 5. 学ぶ・実装する
Coachが示す教材を読み、予想と説明を自分で書きます。
exercisesの課題に従ってsubmissionsへ自分の回答・コードを保存します。
エラーは「期待・実際・全文・再現手順・試したこと」を揃えて相談します。
必要に応じて専門Agentに切り替え、[引き継ぎ手順](session-protocol.md)の内容を送ります。
専門担当の返答をCoachへ戻して評価を依頼します。

## 6. 終了
Coachが示すprogressの差分と根拠を確認します。
次回は同じフォルダーを開き、「前回の続き」と伝えます。
チャット履歴がなくてもファイルから再開する設計です。

## 設定を確かめる
[手動受け入れ確認](acceptance-checklist.md)を実施します。
特に共通指示の認識と、担当外のprogress更新がないことを確認してください。
自力評価の時はインライン補完も無効にします。[制約](compatibility.md)を参照してください。

## 後から必要になる道具
Git、Node.js、Python、PostgreSQL、Dockerは該当段階で導入します。
React開始時は[Vite公式](https://vite.dev/guide/)でNode.js要件を確認し、
FastAPI開始時は[公式チュートリアル](https://fastapi.tiangolo.com/tutorial/)を参照します。
導入した実際の版と起動コマンドをプロジェクトREADMEに残します。

## GitHubで管理する
ローカルのGit管理を使い、まず変更を確認してからコミットします。
自分のGitHubに空のRepositoryを作り、公開範囲を選んで接続する手順は[GitHubへの保存](publishing.md)にあります。
