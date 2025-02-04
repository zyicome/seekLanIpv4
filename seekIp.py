import os
import platform
import subprocess
import socket
import struct
import fcntl
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_local_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode('utf-8'))
    )[20:24])

def ping_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', '-W', '1', ip]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def scan_ip(ip):
    if ping_ip(ip):
        return ip
    return None

def scan_network(interface):
    local_ip = get_local_ip(interface)
    ip_parts = local_ip.split('.')
    base_ip = '.'.join(ip_parts[:-1]) + '.'

    active_ips = set()
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_ip, base_ip + str(i)) for i in range(1, 255)]
        for future in as_completed(futures):
            result = future.result()
            if result:
                active_ips.add(result)

    return active_ips

if __name__ == "__main__":
    interface = 'wlp0s20f3'  # 替换为你的网络接口名称
    active_ips = scan_network(interface)
    for ip in active_ips:
        print(f"Active IP: {ip}")