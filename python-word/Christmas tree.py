import time
import os
import random

height = 8  # 樹高
symbols = ["o", "O"]  # 樹葉裝飾符號

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # 清螢幕
        for i in range(height):
            line = ""
            for j in range(2*i + 1):
                line += random.choice(symbols)
            print(" " * (height - i - 1) + line)
        for _ in range(2):
            print(" " * (height - 1) + "|")  # 樹幹
        time.sleep(0.5)  # 閃爍間隔
except KeyboardInterrupt:
    print("\nMerry Christmas! 🎄")
