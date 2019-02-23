# Subdomain-blasting
功能：
- [x] 子域名爆破   
- [x] 接口查询
- [x] 获取网页标题
- [x] web指纹识别 
- [x] 指定端口扫描
- [x] 网页截图
- [x] 国外DNS记录查询接口

测试结果如下：
![](https://s2.ax1x.com/2019/02/15/krmn3D.png)

![](https://s2.ax1x.com/2019/02/15/krmQud.md.png)

![](https://s2.ax1x.com/2019/02/15/krmlDA.png)

![](https://s2.ax1x.com/2019/02/15/krm8Et.png)



抓取的接口是：http://sbd.ximcx.cn/?#

PS:请在脚本同目录下创建img文件夹

## 注意 ##
- - -
此工具适用于windows。如果是Linux用户请自行下载Chrome的驱动和浏览器

扔到脚本目录，驱动下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads

## 更新 ##
- - -
修复了一些BUG，子域名爆破新增加了端口扫描和网页截图

2019/2/9 By 九世

- - -
修复了一下逻辑上的错误，可以选择不爆破，并且新加了国外某DNS记录查询接口
https://dns.bufferover.run/dns?q=

2019/2/15 by 九世

- - -
今天有位朋友和我说国外的那个dns接口不行了，我打开一看发现加了反爬机制。。怪不得会报错

解决思路：https://www.zhihu.com/question/55642280

https://blog.csdn.net/u013553529/article/details/52134529

2019/2/24 by 九世
