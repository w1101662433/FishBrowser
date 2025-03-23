import asyncio
from pyppeteer import launch


async def main():
    execute_path = r"C:\src\chromium\src\out\Default\chrome.exe"
    browser_args = [
        # "--headless=old",
        "--timezone=Asia/Shanghai",
        "--fingerprints=123123123",
        "--ignores=useragent,tls",
    ]
    browser = await launch(executablePath=execute_path, args=browser_args, headless=False)
    page = await browser.newPage()
    await page.goto("https://www.browserscan.net/zh")
    await asyncio.sleep(99)
    await page.screenshot({'path': './example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
