#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#正则表达式 + os模块：解析ifconfig并ping网关（一个脚本完成）
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import re

result = os.popen("ifconfig ens160").read()

#如果没有 Linux 环境，可以直接使用下面的字符串作为输入:
#result = """ens35: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#        inet 196.21.5.228  netmask 255.255.255.0  broadcast 196.21.5.255
#        inet6 fe80::20c:29ff:fe4d:73b3  prefixlen 64  scopeid 0x20<link>
#        ether 00:0c:29:4d:73:b3  txqueuelen 1000  (Ethernet)
#        RX packets 13573278  bytes 13853395220 (12.9 GiB)
#        RX errors 0  dropped 15  overruns 0  frame 0
#        TX packets 6514517  bytes 1749699427 (1.6 GiB)
#        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0"""

#第一步：用正则表达式提取 IP、掩码、广播地址、MAC，使用 format() 对齐打印:
ip = re.search(r"inet (\d+\.\d+\.\d+\.\d+)", result).group(1)
netmask = re.search(r"netmask (\d+\.\d+\.\d+\.\d+)", result).group(1)
broadcast = re.search(r"broadcast (\d+\.\d+\.\d+\.\d+)", result).group(1)
mac = re.search(r"ether ([0-9a-f:]+)",result).group(1)

print("IP           : {}".format(ip))
print("Netmask      : {}".format(netmask))
print("Broadcast    : {}".format(broadcast))
print("MAC          : {}".format(mac))

print()


#第二步：根据 IP 地址的前三段拼接网关地址（假设网关为 x.x.x.1），然后用 os.popen 执行 ping 测试:
ip_parts = ip.split(".")
gateway = ip_parts[0] + "." + ip_parts[1]+ "." + ip_parts[2] + ".1"

print("假设网关为: {}".format(gateway))

#测试我的网关是否可达
ping_result = os.popen("ping -c 2 " + gateway).read()

#输出网关可达与否的结果
if "0% packet loss" in ping_result:
    print("Ping {} ... reachable".format(gateway))
else:
    print("Ping {} ... unreachable".format(gateway))

