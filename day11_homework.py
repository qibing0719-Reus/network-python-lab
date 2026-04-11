import hashlib
import time
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#函数一：获取设备配置
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_router_config(ip):

    config = """
hostname router1
!
interface GigabitEthernet1
 ip address 192.168.1.11 255.255.255.0
!
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
!
end
"""

    return config
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#函数二：每 5 秒监控一次配置变化
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_md5(config):
    
    md5 = hashlib.md5()
    md5.update(config.encode())
    
    return md5.hexdigest()

def monitor_config(ip, interval=5):
    print(f"开始监控路由器 {ip} 配置...")
    old_md5 = None

    while True:
        config = get_router_config(ip)
        new_md5 = get_md5(config)

        if old_md5 is None:
            print(f"[*] 当前配置 MD5: {new_md5}")

        elif new_md5 != old_md5:
            print("[!] 检测到配置变化!")
            print(f"旧 MD5: {old_md5}")
            print(f"新 MD5: {new_md5}")

        else:
            print(f"[*] 当前配置 MD5: {new_md5}")

        old_md5 = new_md5

        time.sleep(interval)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#监控程序
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    router_ip = "192.168.1.11"

    monitor_config(router_ip)

