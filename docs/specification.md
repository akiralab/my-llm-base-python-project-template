# 設計仕様書（Blueprint）

## 1. プロジェクト概要

- 目的: MLOps用途で再利用できるPythonプロジェクトの基盤を提供する。
- 想定利用: データ処理、学習、推論、評価、運用バッチ。
- 主要原則: 再現性・可観測性・テスト容易性・チーム運用性。

## 2. アーキテクチャ方針

- ソース配置: `src/` レイアウト
- テスト配置: `tests/`
- CLI入口: `src/mlops_template/cli.py`
- 共通機能:
  - ログ基盤: `src/mlops_template/logging_utils.py`
  - 再現性基盤: `src/mlops_template/repro.py`

## 3. 品質仕様

- Lint: `ruff check .`
- 型チェック: `mypy src tests`
- テスト: `pytest`
- カバレッジ: 行カバレッジ 80%以上

## 4. 可観測性仕様

実行時に以下をログへ出力する:

- 実行日時（UTC）
- Git commit SHA
- Pythonバージョン
- OS/プラットフォーム情報
- 主要依存ライブラリバージョン
- Seed値

## 5. CLI仕様

- 引数管理は `argparse` を採用。
- 最低限の標準引数:
  - `--seed`
  - `--log-level`
- `--help` で使い方が完結すること。

## 6. 拡張指針

- 実案件では `src/mlops_template/` をドメイン名パッケージへ変更する。
- 実験追跡・データ版管理は要件確定後に段階導入する。
