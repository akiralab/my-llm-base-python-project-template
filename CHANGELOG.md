# Changelog

このファイルは [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) と SemVer に従います。

## [Unreleased]

### Added

- （なし）

## [0.0.0] - 2026-02-22

### Added

- `uv` 単独運用のPythonテンプレート構成
- `ruff` / `mypy` / `pytest` を含むCI品質ゲート
- PR/Issueテンプレート、`CODEOWNERS`、ブランチ保護運用ドキュメント
- `CLAUDE.md` / `AGENTS.md` を含むLLM協調開発ルール
- VS Code向けの推奨ライブラリ設定ドキュメント

### Changed

- 実行環境要件を Python 3.13+ に更新
- 標準依存に `numpy` / `pandas` / `scipy` / `matplotlib` / `seaborn` / `geopandas` を追加
- `Pathlib.Path` 優先方針へ更新し、CLIで `--output-dir` を標準化
