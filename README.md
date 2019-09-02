# pixiv_tool
Idea on visiting pixiv.net in GFW

基于pixivpy和IBM Cloud Function，不借助VPN或云主机，以可以接受的速度在墙内使用pixivpy的解决方案

我要做什么：
* 0成本：最好不使用信用卡
* 更少的代码量：不要自己搭梯子
* 可以接受的速度：能走本地走本地，如果其他方式更快另当别论

P站的图片服务器在墙内可以正常访问，因此：
* 在IBM云函数上部署request_call函数，从而保证可以正常拉取登录信息、图片信息等json数据
* 重写download函数，从本地网络直接下载图片

现在的问题：
* 想要图形界面！

pixivpy链接：https://github.com/upbit/pixivpy
IBM云函数：https://cloud.ibm.com/functions/
