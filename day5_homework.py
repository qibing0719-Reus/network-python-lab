#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#1.正则表达式练习：从 route -n 输出中查找网关
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import re

#获取路由表
route_n_result = os.popen("route -n").read()

#或直接将下面的内容赋值给变量
"""
route_n_rusult = '''
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.214.2   0.0.0.0         UG    100    0        0 eno16777984
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
192.168.214.0   0.0.0.0         255.255.255.0   U     100    0        0 eno16777984
202.100.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eno33554944
'''
"""

#查找网关
match = re.search(r'0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)', route_n_result)
gateway = match.group(1)
print("网关为: {}".format(gateway))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2. 列表引用与拷贝：对比 l2 = l1 和 l2 = l1.copy()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#l1列表
l1 = [100, 1000, 10, 400, 25, 40, 0]

#从l1拷贝并且排序l2
l2 = l1.copy()
l2.sort()

result = zip(l1, l2)

print(f"{'l1':<10}{'l2':<10}")
for i in result:
    print(f"{i[0]:<10}{i[1]:<10}")

