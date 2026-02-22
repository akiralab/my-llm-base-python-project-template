# AGENTS.md

このファイルは `CLAUDE.md` と同義です。  
Codex / Claude いずれのエージェントも、同じ開発ルールに従います。

## 1. 参照優先順位

1. `docs/requirements.md`
2. `docs/specification.md`
3. `docs/team-rules.md`
4. `docs/docstring_ja_style.md`
5. `docs/skills.md`
6. `docs/llm-context/README.md`

## 2. エージェントへの要求

- PR前提で差分を作ること。
- `ruff` / `mypy` / `pytest` が通る状態を維持すること。
- 実装変更時は必要なドキュメント更新を同時に行うこと。
- 機密情報を扱わないこと。

## 3. 人間承認ルール

- AI生成物は人間レビュー承認なしでマージしない。
