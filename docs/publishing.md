# GitHubへの保存

配布元は[公開Repository](https://github.com/luciole0112/web-app-learning)です。自分の学習記録を管理する場合は、保存先・公開範囲・認証を自分で選びます。
学習記録を含むので、まず非公開で始めることを検討してください。公開は必須ではありません。

## ローカルで記録する
web-app-learningを作業場所にします。Gitは先にインストールします。
ZIPから展開した場合、.gitは含まれないため最初に次を実行します。
```sh
git init -b main
```
すでにGit管理されている場合は再初期化せず、次で状態を確認します。
```sh
git status
git add .
git diff --cached --stat
git diff --cached
git commit -m "Add learning environment MVP"
```
コミット前に秘密と個人情報が含まれないことを確認します。
ユーザー名・メールが未設定ならGitが案内します。自分で使う値を決め、他人の名義を設定しないでください。
依存パッケージや.envが無視されても、すでに追跡中の秘密は.gitignoreだけでは除外されません。

## GitHubへ接続する
GitHubで空のRepositoryを作成し、READMEなどを追加せず、表示されたRepository URLを確認します。
次はURLを本人のものへ置き換えて実行する手順例です。
```sh
git remote add origin YOUR_REPOSITORY_URL
git remote -v
git push -u origin main
```
すでにoriginがある場合は上書きせず接続先を確認してください。
この手順を読むだけでは公開やpushは行われません。
認証情報をURLに埋め込んで教材や履歴に保存しないでください。
GitHubでファイルと公開範囲を確認すれば完了です。
