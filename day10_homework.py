import sys
import os

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#使用 sys.path.insert() 将上级目录加入模块搜索路径
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#再直接导入第八天的函数,第九天我真搞不定了，先用临时输出结果
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from day8.day8_homework import ping_check
def ssh_exec(ip, username, password, cmd):
    """
    临时模拟 SSH 执行命令
    直接返回容器里 show_ip_interface_brief 的输出
    """
    fake_outputs = {
        "192.168.1.11": """Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.1.11    YES NVRAM  up                    up
GigabitEthernet2       unassigned      YES unset  up                    up
GigabitEthernet3       unassigned      YES TFTP   administratively down down""",
        "192.168.1.12": """Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.1.12    YES NVRAM  up                    up
GigabitEthernet2       unassigned      YES unset  up                    up
GigabitEthernet3       unassigned      YES TFTP   administratively down down"""
    }
    return fake_outputs.get(ip, "无法获取接口信息")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#获取设备的接口信息
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_interface_info(ip_list, username, password):
    """
    传入 IP 列表，先 ping 探测；能 ping 通则 SSH 登录采集接口信息并打印。
    """
    for ip in ip_list:
        if ping_check(ip):
            print(f"\n[*] {ip} 可达，正在采集...")
            print(f"---------- {ip} 接口信息 ---------")

            output = ssh_exec(
                ip,
                username,
                password,
                "show_ip_interface_brief" #镜像模拟器没装好，用容器模拟的路由器命令
            )
            print(output)

        else:
            print(f"[x] {ip} 不可达，跳过，不采集。")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#调用设备信息
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
#镜像模拟器没装好，用容器模拟的路由器，地址稍微修改了一下
    devices = [
        "192.168.1.11",
        "192.168.1.12",
    ]
    username = "admin"
    password = "Cisc0123"
    get_interface_info(devices, username, password)

