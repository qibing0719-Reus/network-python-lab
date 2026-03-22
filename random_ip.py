#随机生成IP地址
import random
ip = str (random.randint(1,255)) + "." + \
     str (random.randint(0,255)) + "." + \
     str (random.randint(0,255)) + "." + \
     str (random.randint(1,254))
print("随机生成IP地址:" , ip)



