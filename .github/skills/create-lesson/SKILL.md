---
name: create-lesson
description: "前提と学習目標に合わせたMarkdown教材を作成する"
---

# 前提と学習目標に合わせたMarkdown教材を作成する

## 担当確認
担当はlesson-author。Skillを呼んでもAgentは自動で切り替わらない。
現在の役割が異なる・不明なら、担当Agentを選ぶよう案内し、依頼文を作って止める。
[共通指示](../../copilot-instructions.md)を守る。

## 手順
対象、前提、到達条件、既存教材を確認する。
[共通教材手順](../build-learning-material/SKILL.md)の教材手順に従い、curriculumへ保存する。
例の予測と理解度チェックを含める。該当演習の完成解答は含めない。
パス、教材ID、検証状態、次に必要な演習をCoachへ返す。

## 不足・失敗時
必要なファイルや結果がなければ不足を明示する。推測で作業完了・評価済みにしない。
