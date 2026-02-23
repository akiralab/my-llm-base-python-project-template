# Python MLOps Template

LLM（Codex / Claude）との協調開発を前提にした、チーム開発向けPythonテンプレートです。  
`uv` を単独で採用し、`ruff` / `mypy` / `pytest` をGitHub Actionsで必須化します。

## 特徴

- Python 3.13+ 前提
- `uv` による環境・依存・実行管理（`poetry` 不使用）
- 標準データ分析スタックを同梱（`numpy` / `pandas` / `scipy` / `matplotlib` / `seaborn` / `geopandas`）
- `ruff`（lint）/ `mypy`（型）/ `pytest`（テスト + カバレッジ）をCI必須
- `pre-commit` でCIと同種の `ruff` lintをローカル実行
- `argparse` ベースのCLI雛形
- `loguru` による実行環境ログ出力
- パス操作は `pathlib.Path` を優先（`os` 利用を最小化）
- TDD前提の運用ドキュメント同梱

## クイックスタート

```bash
uv python install 3.13
uv sync --extra dev
uv run pre-commit install
uv run pytest
uv run mypy src tests
uv run ruff check .
uv run mlops-template --help
```

## 主要ドキュメント

- 要件仕様（Must/Should）: `docs/requirements.md`
- 設計仕様書: `docs/specification.md`
- チーム運用ルール: `docs/team-rules.md`
- レビューしやすいPR運用: `docs/reviewer-friendly-pr-rules.md`
- リリースタグ発行ガバナンス: `docs/release-tag-governance.md`
- Notebook運用ルール: `docs/notebook-policy.md`
- Pythonツール運用（uv/ruff/pytest/mypy）: `docs/python-tooling-operations-guide.md`
- GitHub開発基本（fetch/commit/pull/push/pre-commit）: `docs/github-development-basics.md`
- ラベル（タグ）運用: `docs/label-taxonomy.md`
- ブランチ保護設定手順: `docs/github-branch-protection.md`
- mypy/pytestチェックガイド: `docs/mypy-pytest-check-guidelines.md`
- VS Code推奨設定: `docs/vscode-library-recommendations.md`
- 日本語Docstringガイド: `docs/docstring_ja_style.md`
- LLMコンテキスト管理: `docs/llm-context/README.md`
- SKILL運用ルール: `docs/skills.md`

## リポジトリ構成

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── docs/
├── src/mlops_template/
└── tests/
```

## リリース運用

- バージョニング: SemVer (`MAJOR.MINOR.PATCH`)
- リリース時は `CHANGELOG.md` 更新を必須化
- GitHub Release Tag発行を標準運用（詳細は `docs/team-rules.md`）
