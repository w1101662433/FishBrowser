from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# 指定chromedriver的路径
s = Service(r"chromedriver.exe")  # 请将这里替换为你的chromedriver路径

# 初始化Chrome选项
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\src\chromium\src\out\Default\chrome.exe"  # 替换为你的Chrome浏览器路径

chrome_options.add_argument("--fingerprints=11199921")
chrome_options.add_argument("--timezone=Asia/Shanghai")
# chrome_options.add_argument("--headless=old")
chrome_options.add_argument("--ignores=useragent,tls")

# 使用Service对象初始化driver
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.delete_all_cookies()
driver.error_handler.check_response = lambda x: None

driver.get("https://www.browserscan.net/")
# driver.get("https://fingerprintjs.github.io/BotD/main/")
# driver.get("https://zfcsoftware.github.io/selenium-detector/")


time.sleep(999999)
