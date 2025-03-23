import time
from playwright.sync_api import sync_playwright


def run(playwright):
    # 指定chromium浏览器的路径
    executable_path = r"C:\Users\Administrator\Desktop\指纹浏览器\chrome116.beta\chrome\Chrome-bin\chrome.exe"
    # 定义启动参数
    browser_args = [
        "--timezone=Asia/Shanghai",
        "--fingerprints=12312341",
    ]

    # 启动浏览器时添加启动参数
    browser = playwright.chromium.launch_persistent_context(
        executable_path=executable_path,
        args=browser_args,
        headless=False,
        user_data_dir="c:/1111/3339",
        ignore_default_args=['--disable-field-trial-config'],
        # proxy={
        #     'server': 'http://106.58.208.106:27005',  # 代理服务器地址和端口
        #     'username': '5998',  # 代理用户名
        #     'password': '8899'  # 代理密码
        # }
    )
    page = browser.new_page()
    page.goto('https://www.browserscan.net/')
    print(page.title())
    time.sleep(999)
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
