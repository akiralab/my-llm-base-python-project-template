# GitHub ブランチ保護設定手順（main）

対象ブランチ: `main`

## 1. 設定画面を開く

1. GitHubリポジトリを開く
2. `Settings` -> `Branches`
3. `Branch protection rules` で `Add rule`

## 2. ルール設定

`Branch name pattern` に `main` を入力し、以下を有効化します。

- `Require a pull request before merging`
- `Require approvals` を `1`
- `Dismiss stale pull request approvals when new commits are pushed`
- `Require status checks to pass before merging`
- `Require branches to be up to date before merging`
- `Do not allow bypassing the above settings`（運用に応じて推奨）

## 3. Required status checks の登録

CI実行後に以下チェック名を選択します。

- `ruff`
- `mypy`
- `pytest`

## 4. 補助設定（推奨）

- `Require linear history`
- `Require conversation resolution before merging`

## 5. CODEOWNERSの反映確認

- `CODEOWNERS` がデフォルトブランチ上に存在することを確認
- 必要なら `Require review from Code Owners` を有効化

## 6. 動作確認

1. テスト用PRを作成
2. 承認なしではマージ不可であることを確認
3. CI失敗時にマージ不可であることを確認
4. 追加コミット後、承認が再取得必要になることを確認
