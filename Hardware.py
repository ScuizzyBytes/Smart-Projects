import os
import platform

import psutil

processor = platform.processor()
ram = psutil.virtual_memory().total // (1024 ** 3)
disk = psutil.disk_usage('/').total // (1024 ** 3)

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def get_cpu_info(percent):
    if percent < 50:
        return GREEN
    elif percent < 80:
        return YELLOW
    else:
        return RED

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

psutil.cpu_count()
psutil.cpu_percent(interval=1)

cpu_color = GREEN
ram_color = RED
disk_color = YELLOW

print(f"{cpu_color}CPU: {processor}")
print(f"{ram_color}RAM: {ram} ")
print(f"{disk_color}Disk: {disk}")

