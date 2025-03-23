package org.example;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;


//   <dependencies>
//        <dependency>
//            <groupId>org.seleniumhq.selenium</groupId>
//            <artifactId>selenium-java</artifactId>
//            <version>4.11.0</version>
//        </dependency>
//    </dependencies>

public class Main {
    public static void main(String[] args) {
        System.out.println("开始!");

        // 设置ChromeDriver路径
        System.setProperty("webdriver.chrome.driver", "./chromedriver.exe");
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--fingerprints=123123123");
        // 指定Chrome浏览器的路径
        options.setBinary("C:/src/chromium/src/out/Default/chrome.exe");
        WebDriver driver = new ChromeDriver(options);

        driver.get("https://fingerprintjs.github.io/BotD/main/");
        try {
            // 让当前线程暂停10000毫秒（10秒）
            Thread.sleep(10000);
            System.out.println("10秒已经过去，程序继续执行");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        driver.quit();
    }
}