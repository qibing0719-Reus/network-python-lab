###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###1.f-string：打印一条Syslog告警
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down"
print(f"{date} {hostname} {level} {message}")



###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###2.切片：提取接口类型和编号
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
interface = "GigabitEthernet0/0/1"

interface_type = interface [:15]
interface_number = interface [15:]

print("接口类型:", interface_type)
print("接口编号:", interface_number)



###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###3.字符串方法：处理show version输出
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

#去掉首尾空格（strip）
version_strip = version_raw.strip()
print("去掉空格:", version_strip)

#转成大写
version_upper = version_strip.upper()
print("转大写:", version_upper)

#替换版本号
version_replace = version_strip.replace ("17.03.04", "17.06.01")
print("替换版本:", version_replace)



###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###4.format格式化：打印接口状态巡检报告
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
intf1, status1, speed1 = "Gi0/0", "up", "1G"
intf2, status2, speed2 = "Gi0/1", "down", "1G"
intf3, status3, speed3 = "Gi0/2", "up", "10G"

print("\n接口      状态    速率")
print("--------------------")
print("{:<10}{:<8}{}".format(intf1, status1, speed1))
print("{:<10}{:<8}{}".format(intf2, status2, speed2))
print("{:<10}{:<8}{}".format(intf3, status3, speed3))


