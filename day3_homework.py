import re
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#1.正则表达式测试 1：解析MAC地址表
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

match = re.search(r'(\d+)\s+([\da-f.]+)\s+(\w+)\s+(\S+)',mac_table)

vlan = match.group(1)
mac = match.group(2)
type_ = match.group(3)
port = match.group(4)

print("VLAN     : {}".format(vlan))
print("MAC      : {}".format(mac))
print("Type     : {}".format(type_))
print("port     : {}".format(port))

print()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2.正则表达式测试 2：解析ASA防火墙连接表
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
conn = 'TCP server  172.16.1.101:443 localserver  172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

match = re.search(r'(\w+)\s+\w+\s+([\d.]+):(\d+)\s+\w+\s+([\d.]+):(\d+)', conn)

protocol = match.group(1)
server_ip = match.group(2)
server_port = match.group(3)
client_ip = match.group(4)
client_port = match.group(5)

print("Protocol     : {}".format(protocol))
print("Server IP    : {}".format(server_ip))
print("Server Port  : {}".format(server_port))
print("Client IP    : {}".format(client_ip))
print("Client Port  : {}".format(client_port))

