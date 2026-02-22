# Releaseタグ発行ガバナンス（MLOps）

## 1. 目的

主観や感覚でリリースタグを発行しないため、**客観的な判定基準**と**必須証跡**を定義する。  
本書の要件を満たさない場合、タグ発行は不可とする。

## 2. 対象

- Git tag（例: `v0.2.1`）
- GitHub Release
- MLOpsに関わるコード、設定、データ処理、学習・推論ロジック、運用ドキュメント

## 3. タグ種別

- 安定版: `vMAJOR.MINOR.PATCH`（例: `v1.4.2`）
- プレリリース: `vMAJOR.MINOR.PATCH-rc.N`（例: `v1.5.0-rc.1`）

注意:
- 本番投入を伴う変更は、原則として安定版タグで管理する。
- 事前検証が必要な場合のみ `-rc` を利用する。

## 4. SemVer判定基準（客観ルール）

### 4.1 MAJOR（破壊的変更）

以下のいずれかを満たす場合:

- 既存API/CLI/設定キーの互換性を壊す
- 入出力スキーマ（推論出力列、Feature schema等）の後方互換がない
- 既存運用手順で動作しない変更（移行作業が必須）

### 4.2 MINOR（後方互換あり機能追加）

以下を満たす場合:

- 後方互換を維持した機能追加
- 既存処理の利用者に強制変更を求めない
- 追加機能を使わなければ従来挙動が維持される

### 4.3 PATCH（後方互換あり修正）

以下を満たす場合:

- バグ修正、性能改善、ドキュメント改善
- 外部仕様（API/CLI/スキーマ）に互換性破壊がない

## 5. タグ発行ゲート（すべて必須）

以下を1つでも満たさない場合、タグ発行不可。

### G1. 品質ゲート

- `ruff` pass
- `mypy` pass
- `pytest` pass（カバレッジ閾値クリア）

証跡:
- 対象PRのCI結果URL

### G2. 変更管理ゲート

- Release PRが `main` にマージ済み
- `CHANGELOG.md` 更新済み（該当バージョン節あり）
- バージョン文字列（`pyproject.toml`, `__version__`）更新済み

証跡:
- マージ済みPR番号
- 該当コミットSHA

### G3. 再現性ゲート（MLOps）

ML関連変更を含む場合、以下を記録する:

- 学習・推論に使った設定ファイル識別子（パスまたはハッシュ）
- データスナップショット識別子（日時、バージョン、URIなど）
- モデル成果物識別子（ファイル名、レジストリID、ハッシュ）

証跡:
- Release PR本文、または `docs/` 内のリリースノート

### G4. 性能・回帰ゲート（MLOps）

ML関連変更を含む場合、以下を満たす:

- 主要評価指標を記録（例: AUC, F1, RMSE）
- ベースライン比較で許容範囲外の劣化がない
- 劣化がある場合はリリース可否判断と理由を明記

証跡:
- 比較表（before/after）と判断理由

### G5. 運用安全ゲート

- ロールバック手順がPRに明記されている
- 監視/アラートへの影響有無を確認済み

証跡:
- PRテンプレートの「リスクとロールバック方針」

## 6. タグ発行手順

1. Release PRを作成し、ゲート証跡を埋める  
2. CI（`ruff/mypy/pytest`）が全てpass  
3. レビュー完了後 `main` にマージ  
4. `main` のマージコミットを確認  
5. タグ作成（例: `git tag vX.Y.Z <merge_sha>`）  
6. タグpush（`git push origin vX.Y.Z`）  
7. GitHub Releaseを作成  
8. Releaseノートに証跡リンクを添付

## 7. タグ発行不可の例

- CIの一部が未通過
- `CHANGELOG.md` 未更新
- バージョン更新漏れ
- MLOps変更があるのに評価比較・再現性情報がない
- ロールバック方針が未記載

## 8. リリースノート必須項目

- バージョン（`vX.Y.Z`）
- リリース日（YYYY-MM-DD）
- 変更種別（MAJOR/MINOR/PATCH）
- 主要変更点
- 互換性影響
- MLOps証跡（該当時）
- ロールバック手順

## 9. 参考にした公開標準・ガイド

- Semantic Versioning 2.0.0: https://semver.org/
- Keep a Changelog: https://keepachangelog.com/
- GitHub Releases: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- MLOpsのCI/CD/CT（Google Cloud）: https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- TensorFlow Model Analysis（評価ゲート参考）: https://www.tensorflow.org/tfx/model_analysis
