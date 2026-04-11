#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#1. While 循环：监控 TCP/80 HTTP 服务是否开放
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import time

def check_tcp_80():
    while True:
        result = os.popen("ss -tulnp").read()
        found = False
        for line in result.splitlines():
            #使用 os.popen('ss -tulnp').read() 获取端口信息，逐行判断是否同时包含 tcp 和 :80 （注意 避免误匹配 :8080 或 :8000），使用 import time; time.sleep(1) 控制间隔。
            if "tcp" in line and ":80 " in line:
                found = True
                break

        if found:
            print("[!] 告警: TCP/80 已开放！请检查是否为授权服务。")
            break
        else:
            print("[*] 检测中... TCP/80 未监听")
        
        time.sleep(1)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2.pythonping：批量探测网关可达性
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ping_check(host):
    from pythonping import ping
    result = ping(host, count=1, timeout=2)
    if result.success():
        rtt = result.rtt_avg_ms
        return True, rtt
    else:
        return False, None


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#封装一个 ping_check(host) 函数，接收一个 IP 地址，返回 True（可达）或 False（不可达）；在 if __name__ == '__main__'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    print("开始检测 TCP/80 端口状态...\n")
    check_tcp_80()
    print("\n开始检测网关可达性...\n")
    gateways = ['192.168.58.2', '10.0.0.1', '172.16.1.1']
    for gw in gateways:
        status, rtt = ping_check(gw)
        if status:
            print("{:<15}: 可达 | RTT: {:.2f} ms".format(gw, rtt))
        else:
            print("{:<15}: 不可达".format(gw))

