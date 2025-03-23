免安装，解压即用，启动文件是chrome.exe

任何问题和建议，都可以在我的博客下留言：https://blog.csdn.net/w1101662433

或者联系作者QQ1101662433，期待你的建议，指纹浏览器可以做的更好


# 成品功能

**`主要功能`**：
- 启动chrome时，传入参数`--fingerprints=12341234`(正整数，最大值为9个9，不传的话默认传值为当前时间戳)，每个不同值都对应一个不同的指纹。
- 过cdp检测。

**`可选参数`：**

`--noimage` 抹除图片的访问请求。

`--lang=en-US` 修改语言。

`--timezone=Asia/Tokyo` 修改时区。

`--webrtc-ip=8.8.8.8` 强制修改webrtc公网ip，默认禁用webrtc。

`--platform=mac` 模拟其他操作系统。目前可选mac，linux，win。默认为win。

`--http-proxy=http://username:password@ip:port`  http代理需要认证时可以代替`--proxy-server`

`--socks5-proxy=socks5://username:password@ip:port`  socks5代理需要认证时可以代替`--proxy-server`

`--ignores=fonts,screen` 不要修改我的fonts指纹和屏幕信息，多值用逗号分隔，可选值有：fonts,webgpu,plugins,webgl,canvas,audio,clientrect,screen,tls,useragent

----

- 注意：成品仅供个人学习使用，如需商用，请联系作者授权。




指纹和修改：
- canvas指纹
- plugins指纹
- webGL指纹
- webRTC禁用
- audio指纹
- ClientRects指纹
- tls/ja4指纹
- fonts指纹
- webGPU指纹
- 浏览器屏幕指纹
- 浏览器版本和UserAgent
- 时区和语言
- 可绕过cdp检测
- 可绕过常见无头检测
- creepjs跑分为 D-

=========================================================================

版本号：
chromium 116.0.5845.163

注意：成品仅供个人使用和学习，如需商用，请联系作者授权。
