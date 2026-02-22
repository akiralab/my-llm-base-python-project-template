# CLAUDE.md

このリポジトリでは、AIエージェント（Claude / Codex）を補助的に利用します。  
最終意思決定とマージ承認は必ず人間が実施します。

## 1. 参照優先順位

1. `docs/requirements.md`
2. `docs/specification.md`
3. `docs/team-rules.md`
4. `docs/docstring_ja_style.md`
5. `docs/skills.md`
6. `docs/llm-context/README.md`

## 2. エージェントへの要求

- PR前提の変更のみ提案すること。
- テスト・型・lintを通す変更を優先すること。
- 仕様変更時は関連ドキュメントを同時更新すること。
- 機密情報を生成物や提案に含めないこと。

## 3. 人間承認ルール

- AI生成コードはReviewerの人間承認必須。
- 重大な設計判断はIssueまたはADR相当の記録を残す。
