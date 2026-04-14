import socket
import struct
import hashlib
import pickle

def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    version = 1
    pkt_type = 1 
    seq_id = 1

    for x in data_list:
        send_data = pickle.dumps(x)  #数据排序
        data_len = len(send_data)

        md5 = hashlib.md5(send_data).digest()  #计算MD5

        header = struct.pack("!HHIQ", version, pkt_type, seq_id, data_len)  #构建头部

        packet = header + send_data + md5  #拼接完整报文

        s.sendto(packet, address)  #发送UDP
        print(f"[客户端] 已发送 seq={seq_id}, 数据={x}")
        seq_id +=1

    s.close()

  #主运行函数
if __name__ == "__main__":
    from datetime import datetime
    

    user_data = [
        '乾颐堂',
        [1, 'qytang', 3],
        {'qytang': 1, 'test': 3},
        {'datetime': datetime.now()}
    ]
    udp_send_data('127.0.0.1', 6666, user_data)
