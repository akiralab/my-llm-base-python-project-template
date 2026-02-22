# GitHub開発の基本手順（pre-commit / git fetch / commit / pull / push）

## 1. 標準フロー

```bash
# 1) 最新取得
git fetch origin
git checkout main
git pull --ff-only origin main

# 2) 作業ブランチ作成
git checkout -b feature/<topic>

# 3) 実装・テスト
uv sync --extra dev
uv run pre-commit run --all-files

# 4) コミット
git add <files>
git commit -m "feat: <what and why>"

# 5) 共有
git push -u origin feature/<topic>
```

## 2. コマンド解説

### 2.1 `git fetch`

- リモートの最新情報を取得する（ローカルブランチは更新しない）。
- 作業前に必ず実行して差分の前提を揃える。

### 2.2 `git pull --ff-only`

- `fetch + fast-forward merge` をまとめて実行する。
- 不要なマージコミットを避けるため `--ff-only` を推奨する。

### 2.3 `git commit`

- 1コミット1目的を意識する。
- メッセージは「何を変えたか」「なぜ必要か」を含める。
- ノイズの多い試行錯誤コミットは、レビュー前に整理する。

### 2.4 `git push`

- 初回は `git push -u origin <branch>` で追跡設定する。
- push前に `pre-commit` とテストを実行し、CI失敗を減らす。

## 3. pre-commit の使い方

```bash
# 初回セットアップ
uv run pre-commit install

# 全ファイル検査
uv run pre-commit run --all-files

# 変更ファイルのみ検査
uv run pre-commit run
```

本リポジトリでは `pre-commit` で以下を実行します。

- `ruff-check`
- `mypy-check`
- `pytest-check`

## 4. PR作成時の基本

- PRテンプレートを埋める。
- 変更の背景・影響範囲・テスト結果・ロールバック方針を明記する。
- ラベル（`docs` / `ci` / `mlops` / `bug` / `feature` など）を適切に設定する。
- UI変更時はスクリーンショットまたは動画を添付する。

## 5. Issue作成時の基本

- Bug/Featureテンプレートを使い、再現情報と受け入れ条件を明記する。
- 内容に応じたラベルを設定する（例: `bug`, `feature`, `mlops`, `docs`, `ci`）。
