# Python MLOps Template 要件仕様（確定版 v1.0）

最終更新日: 2026-02-22

## 1. 目的

- MLOps用途のPythonリポジトリを、再現性・品質・保守性を担保した状態で迅速に立ち上げる。
- LLM（Codex / Claude）利用時も、人間承認を中心とした安全なチーム開発を実現する。

## 2. Must（必須要件）

### 2.1 ツールチェーン

- Pythonは `3.13+` を使用する。
- Python環境・依存管理は `uv` を単独採用する（`poetry` は採用しない）。
- Lintは `ruff` を採用し、CIで必須化する。
- 型チェックは `mypy` を採用し、CIで必須化する。
- テストは `pytest` を採用し、CIで `tests/` を必ず実行する。
- カバレッジ閾値（初期値: 80%）をCIで必須化する。
- `pre-commit` でCIと同等の `ruff` / `mypy` / `pytest` を実行する。
- 標準ライブラリセットとして以下を依存管理に含める:
  - `numpy`
  - `pandas`
  - `scipy`
  - `matplotlib`
  - `seaborn`
  - `geopandas`

### 2.2 Git/GitHub運用

- `main` ブランチへの直接pushを禁止し、PR経由のみマージ可とする。
- PRマージ時に最低1名のReviewer承認を必須化する。
- Required status checksを有効化し、`ruff` / `mypy` / `pytest` を必須にする。
- 追加コミット時の再レビューを要求する（dismiss stale approvals）。
- `CODEOWNERS` を用意する。

### 2.3 開発規約

- TDD（Red -> Green -> Refactor）を基本とする。
- CLI引数管理は `argparse` を標準とする。
- ファイルパス操作は `pathlib.Path` を優先し、`os` の利用は最小化する。
- 実行環境ログ（日時・Git SHA・Python/OS・依存バージョン）を出力可能にする。
- 乱数Seedを固定可能にし、実験再現性を担保する。
- ロガーは可読性重視で `loguru` を標準採用する。

### 2.4 ドキュメント

- `README.md` を継続管理する。
- `CONTRIBUTING.md` を配置する。
- `CODE_OF_CONDUCT.md` を配置する。
- `CHANGELOG.md` を配置し、リリース時更新を必須にする。
- `CLAUDE.md` と `AGENTS.md` を同義で配置する。
- 設計仕様書 `docs/specification.md` を配置する。
- チーム運用ルール `docs/team-rules.md` を配置する。
- 日本語Docstringガイド `docs/docstring_ja_style.md` を配置する。
- LLMコンテキスト管理ガイド `docs/llm-context/README.md` を配置する。
- SKILL運用ガイド `docs/skills.md` を配置する。

### 2.5 チームテンプレート

- Issueテンプレート（`Bug` / `Feature`）を配置する。
- PRテンプレートを配置する。
- PR/Issue向けラベル体系（`docs`, `ci`, `mlops`, `bug`, `feature` 等）を運用する。
- ラベル運用ルールを `docs/label-taxonomy.md` に明記する。
- PRテンプレートに以下を含める:
  - 優先度/緊急度
  - 背景/目的
  - 影響範囲
  - テスト結果
  - リスクとロールバック方針

### 2.6 リリース

- SemVerを採用する。
- GitHubのリリースタグ発行ルールを文書化する。
- タグ発行は客観ゲート（品質・再現性・回帰・ロールバック）で判定する。

## 3. Should（推奨要件）

- セキュリティチェック（`gitleaks`, `pip-audit`）を導入する。
- `SECURITY.md` を配置する。
- カバレッジ閾値を段階的に80% -> 85% -> 90%へ引き上げる。
- ブランチ保護で `require linear history` を有効化する。

## 4. Not in Scope（現時点で除外）

- 実験追跡基盤（MLflow / W&B）
- データ・モデル版管理（DVC等）
- モデル評価レポート標準フォーマット

## 5. 受け入れ判定

以下をすべて満たすこと:

- Must要件がテンプレート内ファイルに反映されている。
- GitHub上でブランチ保護設定手順が再現できる。
- `uv sync --extra dev` 後、`ruff` / `mypy` / `pytest` が実行可能。
