# 首先
为什么会有这个程序呢，主要是因为有时候老是找不到同局域网下小电脑的ip地址（用于nomachine连接），又不方面打开小电脑的桌面进行直接查看，这个时候我们就需要一个工具能够帮我们找到可能的ip并进行尝试

## 为什么是ping（耗时这么久...）而不是arp（路由器通过arp协议链接MAC地址和ip地址）？
因为用arp没有权限，无法直接发送（哭），暂时没有找到怎么开权限(已解决，用sudo身份运行)
但是arp得到的结果好像不太完整

# 使用方法(目前只在linux上测试过)
```shell
pip3 install scapy #安装必要库
sudo pip3 install scapy #在sudo身份下安装必要库

python3 checkInterface.py #找到对应的网络接口，并修改在seekIp.py的interface = "?"中
python3 seekIp.py #等待一小会即可出现结果

sudo python3 arpSeekIp.py 
```

# 吐槽
```bash
#linux先下载 sudo apt install net-tools
#发现一个更简单的方法了，直接终端输入arp -a, 直接arp操作，找找你想要的ip就行(而且是系统内置的功能，所以找到更全更准)
arp -a
```