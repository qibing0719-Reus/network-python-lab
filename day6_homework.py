#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#1.字典课堂作业:把防火墙状态信息表存为字典
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import re
asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

conn_dict = {}
for line in asa_conn.split('\n'):
    match = re.match(
            r".* (\d+\.\d+\.\d+\.\d+):(\d+) .* (\d+\.\d+\.\d+\.\d+):(\d+),.*bytes (\d+), flags (\w+)",
            line
    )
    if match:
        src_ip = match.group(1)
        src_port = match.group(2)
        dst_ip = match.group(3)
        dst_port = match.group(4)
        bytes_num = match.group(5)
        flags = match.group(6)

        key = (src_ip,src_port,dst_ip,dst_port)
        value = (bytes_num, flags)

        conn_dict[key] = value

print(conn_dict)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#格式化打印输出（使用 format() 对齐，用 | 分隔各列）
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for key,value in conn_dict.items():

    src,src_port,dst,dst_port = key
    bytes_num,flags = value

    print("src      : {:<15} | src_port : {:<6} | dst       : {:<15} | dst_port : {:<6}".format(src,src_port,dst,dst_port))
    print("bytes    : {:<15} | flags        : {}".format(bytes_num,flags))
    print("="*84)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2.接口排序
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

port_list.sort(key=lambda x: list(map(int, x.split()[1].split('/'))))
print(port_list)

