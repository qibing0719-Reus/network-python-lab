import paramiko
import time

def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    """
    参数说明：
      cmd_list  : 要执行的命令列表，例如 ['terminal length 0', 'show version']
      enable    : enable 密码，若设备无需 enable 则保持默认空字符串
      wait_time : 每条命令发送后等待设备响应的秒数
      verbose   : True 则打印每条命令的返回结果，False 则静默执行
    """

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,
                port=22,
                username=username,
                password=password,
                timeout=5,
                look_for_keys=False,
                allow_agent=False)

    chan = ssh.invoke_shell()
    time.sleep(1)

    all_output = chan.recv(4096).decode()

    if enable:
        chan.send(b'enable\n')
        time.sleep(1)
        chan.recv(2048)

        chan.send((enable + '\n').encode())
        time.sleep(1)
        chan.recv(2048)

    for cmd in cmd_list:
        chan.send((cmd + '\n').encode())
        time.sleep(wait_time)

        result = ''

        while chan.recv_ready():
            result += chan.recv(65535).decode()

        all_output += result
        
        if verbose:
            print(f"---{cmd}---")
            print(result)

    ssh.close()

    return all_output

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#最终运行主函数
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    cmd_list = [
            'terminal length 0',
            'show version',
            'config ter',
            'router ospf 1',
            'network 10.0.0.0 0.0.0.255 area 0',
            'end',
    ]
    output = qytang_multicmd(
        ip = '192.168.56.101',
        username = 'admin',
        password = 'Cisc0123',
        cmd_list = cmd_list
    )

    print("\n==== 汇总输出 ====")
    print(output)
