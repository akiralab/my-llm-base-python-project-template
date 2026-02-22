# Contributing Guide

## 1. 開発開始手順

```bash
uv sync --extra dev
uv run pre-commit install
```

## 2. ブランチ戦略

- `main` から作業ブランチを作成する。
- 命名例:
  - `feature/<topic>`
  - `bugfix/<topic>`
  - `docs/<topic>`

## 3. 実装ルール

- 原則TDDで進める（テスト先行）。
- 変更には対応テストを追加/更新する。
- CLI引数は `argparse` に統一する。
- パス操作は `pathlib.Path` を優先し、`os` は必要最小限で使う。
- 実行ログには再現性情報（seed, 実行環境）を含める。

## 4. ローカルチェック

PR作成前に以下を実行する。

```bash
uv run ruff check .
uv run mypy src tests
uv run pytest
```

## 5. PRルール

- PRテンプレートを埋める。
- 最低1名のReviewer承認を得る。
- CI（`ruff`, `mypy`, `pytest`）を全て通す。
- ドキュメント変更を伴う場合は同一PRで更新する。
- 1PR1目的を原則とし、差分が大きい場合は分割する。
- UI変更時はスクリーンショットまたは動画をPRに添付する。
- ロジック変更と機械的変更（整形・置換）は分離する。

### レビュー依頼前のコミット整理

- `fixup` や試行錯誤コミットが多い場合は、意味のある単位に整理してからレビュー依頼する。
- コミットメッセージは「何を変えたか」と「なぜ必要か」を読み取れる表現にする。

## 6. レビューSLA

- 原則1営業日以内に初回レビュー開始。
- 停滞時は担当を再調整する。

## 7. リリース

- SemVerに従う。
- リリース時は `CHANGELOG.md` の更新を必須とする。
