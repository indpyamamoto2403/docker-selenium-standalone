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

driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)

driver.get("https://www.google.co.jp/")

driver.save_screenshot("screenshot.png")

print(driver.title)
sleep(2)
driver.quit()