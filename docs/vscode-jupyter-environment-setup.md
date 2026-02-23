# VS Code向け Jupyter環境構築ガイド

## 1. 目的

VS Code上でNotebookを実行する際に、`ModuleNotFoundError`（例: `loguru`）を防ぐための再現可能な手順を定義します。

## 2. 前提

- OS: macOS / Linux / Windows
- Python: 3.13系（`.python-version` に合わせる）
- VS Code拡張:
  - `ms-python.python`
  - `ms-toolsai.jupyter`

## 3. 初期セットアップ（プロジェクト直下で実行）

```bash
# 1) Pythonの準備
uv python install 3.13

# 2) 依存同期（loguru含む）
uv sync --extra dev

# 3) Notebookカーネル用パッケージを仮想環境へ導入
uv pip install ipykernel jupyterlab

# 4) .venv をJupyterカーネルとして登録
uv run python -m ipykernel install --user \
  --name my-llm-base-python-project-template \
  --display-name "my-llm-base-python-project-template (.venv)"
```

## 4. VS Code側の設定

1. Notebook（`.ipynb`）を開く  
2. 右上の `Select Kernel` をクリック  
3. `my-llm-base-python-project-template (.venv)` を選択  
4. 以後、そのNotebookでは同カーネルを使用する

## 5. 動作確認セル

以下セルを先頭で実行し、環境が正しいか確認してください。

```python
import sys
from pathlib import Path

import geopandas
import loguru
import matplotlib
import numpy
import pandas
import scipy
import seaborn

print("python:", sys.executable)
print("cwd:", Path.cwd())
print("loguru:", loguru.__version__)
```

期待値:
- `sys.executable` がプロジェクト配下の `.venv` を指す
- `ModuleNotFoundError` が発生しない

## 6. 典型的なエラーと対処

### 6.1 `ModuleNotFoundError: No module named 'loguru'`

原因候補:
- VS Codeで別カーネル（システムPython等）を選択している
- `uv sync --extra dev` を未実行

対処:

```bash
uv sync --extra dev
uv run python -c "import loguru; print(loguru.__version__)"
```

その後、NotebookのKernelを `.venv` に再設定します。

### 6.2 Kernelが選択肢に出ない

対処:

```bash
uv pip install ipykernel jupyterlab
uv run python -m ipykernel install --user \
  --name my-llm-base-python-project-template \
  --display-name "my-llm-base-python-project-template (.venv)"
```

## 7. 運用メモ

- 依存更新後は `uv sync --extra dev` を再実行する。
- Notebookで必要な新規ライブラリを追加した場合は、`pyproject.toml` / `uv.lock` に反映する。
