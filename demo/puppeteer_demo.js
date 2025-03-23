const puppeteer = require('puppeteer');

(async () => {
  const browserPath = "C:/src/chromium/src/out/Default/chrome.exe"; // 指定Chrome浏览器的路径，根据实际情况修改
  const url = 'https://www.browserscan.net/'; // 替换成你想访问的网页地址
  //const url = 'https://zfcsoftware.github.io/selenium-detector/'; // 替换成你想访问的网页地址

  const browser = await puppeteer.launch({
    executablePath: browserPath, // 使用指定的Chrome浏览器执行路径
    headless: false, // 非无头模式，可以看到浏览器界面
    args:[
        // "--headless=old",
        "--timezone=Asia/Shanghai",
        "--fingerprints=123123123",
        "--ignores=useragent,tls"
    ]
  });

  const page = await browser.newPage();
  await page.goto(url);

  //await page.waitForTimeout(999000); // 等待999秒
  await new Promise(function(resolve) {
      setTimeout(resolve, 999000); // 等待999秒
  });
  await browser.close(); // 关闭浏览器
})();
