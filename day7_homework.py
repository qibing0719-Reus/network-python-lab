import os
import shutil

#设备配置文件
files = {
    'R1_config.txt': 'hostname R1\ninterface GigabitEthernet0/0\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R2_config.txt': 'hostname R2\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'R3_config.txt': 'hostname R3\ninterface GigabitEthernet0/0\n no shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
    'SW1_config.txt': 'hostname SW1\ninterface Vlan1\n shutdown\ninterface GigabitEthernet0/1\n no shutdown\n',
}

# a.创建 backup/ 目录
os.makedirs("backup", exist_ok=True)

#写入设备配置文件
for filename, content in files.items():
    with open(f"backup/{filename}", "w") as f:
        f.write(content)
      
#b.遍历 backup/ 目录，找出含有 shutdown（排除 no shutdown）接口的配置文件，打印文件名
print("发现包含 shutdown 接口的设备配置文件:")

for filename in os.listdir("backup"):
    filepath = f"backup/{filename}"

    with open(filepath) as f:
        config = f.read()

    if "\n shutdown" in config:
        print(filename)

#c.搜索完成后，自动删除 backup/ 目录及其所有文件
shutil.rmtree("backup")
print("backup/ 目录已清理")



