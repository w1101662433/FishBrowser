# pip install DrissionPage --upgrade
import time
from DrissionPage import Chromium, ChromiumOptions

# 创建配置对象（默认从 ini 文件中读取配置）
co = ChromiumOptions().set_browser_path(r"C:/src/chromium/src/out/Default/chrome.exe")

# 设置启动时最大化
co.set_argument('--start-maximized')
co.set_argument('--fingerprints=123123')
co.set_argument('--timezone=Asia/Singapore')

# 以该配置创建页面对象
browser = Chromium(addr_or_opts=co)

tab = browser.latest_tab
# 访问网页
tab.get('https://www.browserscan.net/zh')
# tab.get("https://fingerprintjs.github.io/BotD/main/")
# tab.get("https://zfcsoftware.github.io/selenium-detector/")
time.sleep(7777)
