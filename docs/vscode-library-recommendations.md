# VS Code ライブラリ推奨設定

## 1. 目的

本ドキュメントは、VS Code上で本リポジトリのPython開発を行う際の推奨設定を定義します。  
対象ライブラリ（`ruff` / `mypy` / `pytest` / `numpy` / `pandas` / `scipy` / `matplotlib` / `seaborn` / `geopandas`）を安定運用することを目的とします。

## 2. 推奨VS Code拡張

- `ms-python.python`
- `ms-python.vscode-pylance`
- `charliermarsh.ruff`
- `ms-python.mypy-type-checker`
- `ms-toolsai.jupyter`

## 3. 推奨ワークスペース設定

`.vscode/settings.json` の推奨例:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.diagnosticMode": "workspace",
  "mypy-type-checker.importStrategy": "fromEnvironment",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },
  "jupyter.askForKernelRestart": false
}
```

注記:
- macOS/Linux前提のインタープリタパスです。Windowsは `.venv\\Scripts\\python.exe` を使用してください。
- CIの正判定は `ruff` / `mypy` / `pytest` です。IDE表示と不一致がある場合はCI結果を優先してください。

## 4. ライブラリ別の推奨運用

### 4.1 `ruff` / `mypy` / `pytest`

- ローカル保存時は `ruff` で素早く整形・静的検査を行う。
- 型の最終判定は `uv run mypy src tests` で確認する。
- テストは `python.testing.pytestEnabled=true` でIDE実行とCLI実行を揃える。

### 4.2 `numpy` / `pandas` / `scipy`

- データ処理・統計計算はNotebookとスクリプトで同一の仮想環境を利用する。
- 型補完はPylanceを利用し、最終的な整合性は `mypy` で確認する。

### 4.3 `matplotlib` / `seaborn`

- Notebook用途では `ms-toolsai.jupyter` を利用する。
- 出力画像は再現性確保のため、保存先パスを `pathlib.Path` で明示する。

### 4.4 `geopandas`

- `geopandas` はネイティブ依存を含むため、`uv sync --extra dev` 実行直後にimport確認を行う。
- 大きな地理データを扱う際は、IDEフリーズ防止のため必要最小限のプレビューに留める。

## 5. 運用ルール

- ワークスペース設定を変更した場合は、PRで本ドキュメントも更新する。
- 推奨拡張の追加・削除はチーム合意のうえで反映する。
- Notebook環境構築とトラブル対応は `docs/vscode-jupyter-environment-setup.md` を参照する。
