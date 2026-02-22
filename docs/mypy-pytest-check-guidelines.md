# mypy / pytest チェックガイド

## 1. 目的

本ドキュメントは、`mypy` と `pytest` のチェック内容を明確化し、開発者が設計段階で品質要件を満たせるようにするためのガイドです。  
`pre-commit` と GitHub Actions（CI）で同じ観点を確認します。

## 2. mypy チェック内容

実行コマンド:

```bash
uv run mypy src tests
```

現在の基本設定（`pyproject.toml`）:

- `strict = true`
- `python_version = "3.13"`
- `mypy_path = "src"`
- `tests.*` のみ一部厳格設定を緩和

`strict = true` で主に確認される観点:

- 関数引数・戻り値の型注釈不足
- `Optional` / `None` の扱い不備
- 型不整合な代入・返却
- 不正な属性アクセスや呼び出し
- 到達不能・曖昧な型推論による不安全な処理

設計時チェックポイント:

- 公開関数は引数と戻り値の型を明示する
- 返却型が分岐で変わらないように設計する
- `Any` の安易な利用を避ける
- データ構造は `TypedDict` や dataclass を検討する

## 3. pytest チェック内容

実行コマンド:

```bash
uv run pytest
```

現在の基本設定（`pyproject.toml`）:

- `testpaths = ["tests"]`
- `--cov=src`
- `--cov-report=term-missing`
- `--cov-fail-under=80`

確認される観点:

- `tests/` 配下のテストがすべて成功すること
- 変更による回帰がないこと
- 行カバレッジが 80% 未満でないこと

設計時チェックポイント:

- 新規機能には正常系と異常系のテストを用意する
- バグ修正には再発防止テストを必ず追加する
- I/O 依存処理は `tmp_path` などで分離して検証する
- 実行時間の長いテストは分割し、失敗時の原因が追える構成にする

## 4. pre-commit と CI の整合

`pre-commit` は以下の順で実行されます。

1. `ruff-check`
2. `mypy-check`
3. `pytest-check`

CIでも同等のチェック（`ruff` / `mypy` / `pytest`）を必須化しています。  
ローカルで `pre-commit` を通してからPRを作ることで、CI失敗を最小化できます。

## 5. 推奨ローカル運用

```bash
uv sync --extra dev
uv run pre-commit install
uv run pre-commit run --all-files
```
