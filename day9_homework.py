#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#paramiko：SSH 登录 Linux 查询默认网关
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import paramiko
import re

def ssh_exec(host, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        host,
        port = 22,
        username = username,
        password = password,
        timeout = 5,
        look_for_keys = False,
        allow_agent = False
    )
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode()
    ssh.close()
    return result

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#执行 route -n, 提取并打印默认网关（Destination 为 0.0.0.0 的那一行的 Gateway 字段）：
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
try:
    route_output = ssh_exec(
        "196.21.5.228",
        "root",
        "Cisc0123",
        "route -n"
        )

    for line in route_output.splitlines():
        match = re.match(r"0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)\s+.*UG", line)
        if match:
            gateway = match.group(1)
            print("默认网关:", gateway)

except Exception as e:
    print("SSH连不上:",e)

