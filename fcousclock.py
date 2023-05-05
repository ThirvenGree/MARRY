# MARRY
import time
from os import system

while True:
    现在时间 = time.strftime("%H:%M:%S", time.localtime())
    system('cls' if os.name == 'nt' else 'clear')  # 清除屏幕
    print("当前时间:", 现在时间)
    time.sleep(1)  # 暂停一秒钟
