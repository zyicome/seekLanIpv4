from scapy.all import ARP, Ether, srp

def scan_network(network):
    # 创建ARP请求包
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # 发送包并接收响应
    result = srp(packet, timeout=2, verbose=False)[0]

    # 解析响应
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    network = '192.168.10.171/24'  # 替换为你的网络地址
    devices = scan_network(network)

    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")