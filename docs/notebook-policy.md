# Notebook運用ルール

## 1. 基本方針

- `.ipynb` は原則としてGit管理しない。
- 例外として、テンプレート用の1ファイルのみ管理する。
  - 管理対象: `notebooks/template.ipynb`

## 2. 目的

- Notebook差分のノイズを減らし、レビュー容易性を維持する。
- 共有すべき最小限の初期構成（PATH設定・標準import）だけをテンプレート化する。

## 3. ローカルNotebookの作成方法

```bash
mkdir -p notebooks/local
cp notebooks/template.ipynb notebooks/local/my-analysis.ipynb
```

- `notebooks/local/*.ipynb` は `.gitignore` により追跡されない。
- 解析Notebookは原則ローカル運用し、成果は `.py` / `.md` / 画像などで共有する。

## 4. テンプレートNotebookに含める内容

- `src` 配下をimportできるPATH設定
- 基本ライブラリのimport（`numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn`, `geopandas`）
- 最小限の可視化サンプル

## 5. 更新ルール

- テンプレートNotebookの変更はPRで管理する。
- 変更時は本ドキュメントも同時更新する。
