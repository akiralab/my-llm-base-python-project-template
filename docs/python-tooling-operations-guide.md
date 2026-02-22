# Python開発ツール運用ガイド（uv / ruff / pytest / mypy）

## 1. 目的

本ガイドは、`uv` / `ruff` / `pytest` / `mypy` の一般的な使用方法と、開発時の留意事項をまとめたものです。  
ローカル開発・PR作成・CI確認で同じコマンド体系を使う前提とします。

## 2. uv（環境・依存・実行）

### 2.1 よく使うコマンド

```bash
# Python本体の用意（例: 3.13）
uv python install 3.13

# 依存同期（開発依存込み）
uv sync --extra dev

# 依存ロック更新
uv lock

# コマンド実行
uv run pytest
uv run mypy src tests
uv run ruff check .
```

### 2.2 留意事項

- `pyproject.toml` を変更したら `uv lock` を実行し、`uv.lock` も同時コミットする。
- CIと同じ実行経路にするため、コマンドは `uv run ...` で統一する。
- Pythonバージョン差異を避けるため、`.python-version` を常に確認する。
- Jupyter利用時は `uv sync --extra dev` 実行後、`.venv` カーネルを選択する。
- VS CodeでのNotebook環境構築は `docs/vscode-jupyter-environment-setup.md` を参照する。

## 3. ruff（Lint/Format）

### 3.1 よく使うコマンド

```bash
# 静的チェック
uv run ruff check .

# 自動修正込み
uv run ruff check . --fix

# フォーマット
uv run ruff format .
```

### 3.2 留意事項

- 自動修正で変更された差分は、意図しない修正がないか確認してからコミットする。
- Import順序や軽微な規約違反は、レビュー前に `ruff` で解消する。
- ルール除外は最小限にし、除外理由を明記する。

## 4. mypy（型チェック）

### 4.1 よく使うコマンド

```bash
uv run mypy src tests
```

### 4.2 留意事項

- 公開関数は引数・戻り値の型を明示する。
- `Any` の安易な利用を避け、型が曖昧な箇所を放置しない。
- `Optional` と `None` の分岐を明確にし、暗黙的な型変換に依存しない。
- 型回避のための無理な実装より、データ構造設計を見直す。

## 5. pytest（テスト）

### 5.1 よく使うコマンド

```bash
# テスト実行（coverage閾値含む）
uv run pytest

# 特定テストのみ
uv run pytest tests/test_cli.py
```

### 5.2 留意事項

- バグ修正時は再発防止テストを必ず追加する。
- I/Oは `tmp_path` などで隔離し、環境依存を減らす。
- テストが不安定（flaky）なら、原因を解消するまで放置しない。
- カバレッジ閾値を満たしても、重要経路の未検証を残さない。

## 6. 開発時の推奨実行順序

```bash
uv sync --extra dev
uv run pre-commit run --all-files
uv run ruff check .
uv run mypy src tests
uv run pytest
```

`pre-commit` と CI の結果が乖離した場合は、CI設定を正としてローカル設定を修正してください。
