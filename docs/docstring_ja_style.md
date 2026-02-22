# 日本語Docstringスタイルガイド

本プロジェクトでは、日本語Docstringを推奨します（努力目標）。  
可読性と保守性を優先し、最低限以下の形式を参考にしてください。

## 1. classのDocstring例

```python
class PredictionService:
    """推論処理を統括するサービスクラス。

    Attributes:
        model_path: 学習済みモデルのファイルパス。
        threshold: 判定に使用する閾値。
    """
```

## 2. 単一関数のDocstring例

```python
def load_dataset(path: str) -> pd.DataFrame:
    """データセットを読み込んで前処理済みDataFrameを返す。

    Args:
        path: 入力CSVファイルのパス。

    Returns:
        前処理後のDataFrame。

    Raises:
        FileNotFoundError: 指定パスにファイルが存在しない場合。
    """
```

## 3. YAML記載時の説明例

YAMLそのものにDocstringは書けないため、`description` またはコメントで説明を残します。

```yaml
training:
  seed: 42  # 乱数シード（再現性のため固定）
  description: "本設定はベースライン学習用。評価指標はF1を採用。"
```

## 4. 運用ルール

- 公開関数・クラスはDocstring記載を推奨。
- 意図が読み取りにくい処理は、短く具体的に説明する。
- AI生成コードでもDocstring不足はレビューで指摘対象とする。
