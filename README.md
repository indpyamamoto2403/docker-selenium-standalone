# Docker Selenium プロジェクト

このプロジェクトは、SeleniumをDockerコンテナ内で実行するための設定を提供します。
ブラウザの自動化テストを簡単にセットアップし、実行することができます。

## 特徴

- ChromeベースのDocker-selenium環境およびstandalone公式イメージを用いた
- 簡単なセットアップと実行
- コンテナ化による一貫したテスト環境

## セットアップ

1. Dockerをインストールします。
2. このリポジトリをクローンします。
    ```bash
    git clone https://github.com/yourusername/docker-selenium.git
    ```
3. Dockerコンテナをビルドして起動します。
    ```bash
    cd docker-selenium
    docker-compose up -d
    ```

## 使用方法

1. テストスクリプトを作成し、`tests`ディレクトリに配置します。
2. 以下のコマンドでテストを実行します。
    ```bash
    docker-compose run test
    ```

## webdriverインスタンス設定およびoption設定

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Selenium サーバー (Remote WebDriver) の設定
selenium_url = "http://selenium:4444/wd/hub"
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# ブラウザを表示するための設定
chrome_options.add_argument("--start-maximized")  # ブラウザを最大化
chrome_options.add_argument("--disable-infobars")  # 情報バーを無効化
chrome_options.add_argument("--disable-extensions")  # 拡張機能を無効化
#
driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)

```

## VNCでのSeleniumのリモート閲覧方法

1. Dockerコンテナが起動していることを確認します。
2. VNCクライアントを使用して、以下の情報で接続します。
    - ホスト: `localhost`
    - ポート: `7900`
    - パスワード: `secret`（デフォルトのパスワードを使用している場合）


## ライセンス

このプロジェクトはMITライセンスの下で提供されています。詳細については、`LICENSE`ファイルを参照してください。