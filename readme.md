免安装，解压即用，启动文件是chrome.exe

主要参数：
启动chrome时，传入参数--fingerprints=123123123(正整数)，则指纹固定不变。当正整数更换，则获得一个新指纹。
启动chrome时，不传参数--fingerprints，则每个访问请求的指纹全部随机生成。

其他参数：
--noimage 抹除图片的访问请求。
--lang="en-US" 修改语言。
--timezone="Asia/Tokyo" 修改时区。
--proxy-server="socks5://127.0.0.1:10808"  加代理(不支持账号密码认证)


=========================================================================
版本更新：

v1.0.1：
修复了pixelscan中webgl指纹不变的bug
给 WebGL vendor 追加了随机数
给 WebGL renderer 追加了随机数
修改了无头模式下的WebGL renderer
增加了无头模式下的UA随机变化。

v1.0.2：
修复了selenium无头模式下版本不匹配导致卡死bug
新增--timezone参数，可自定义修改时区。
