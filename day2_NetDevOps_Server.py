import socket
import sys
import struct
import hashlib
import pickle

address = ('0.0.0.0', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器就绪！等待客户数据！')
while True:
    try:
        recv_source_data = s.recvfrom(544)  #接收数据(512)+报头(16)+MD5(16)
        rdata, addr = recv_source_data  #源地址+源端口

        header = rdata[:16]  #报头（16）
        data = rdata[16:-16]  #接收的数据
        md5_recv = rdata[-16:]  #MD5(16)

        version, pkt_type, seq_id, length = struct.unpack('!HHIQ', header)  #解报头

        md5_value = hashlib.md5(data).digest()  #MD5校验

#判断并且输出结果
        if md5_recv == md5_value:
            print('=' * 80)
            print("{0:<30}:{1:<30}".format("数据源自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序列号", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))
        else:
            print('MD5校验错误！')
    except KeyboardInterrupt:
        sys.exit()
