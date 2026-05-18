import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

R, G, Y, B, P, W = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.WHITE

def clear():
    os.system("clear")

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


clear()


print(f"""{R}
 █     █░▓█████  ██▓     ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████ 
▓█░ █ ░█░▓█   ▀ ▓██▒    ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒█░ █ ░█ ▒███   ▒██░    ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ 
░░██▒██▓ ░▒████▒░██████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░
  ░   ░     ░     ░ ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░   
    ░       ░  ░    ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░
                                ░                                  
""")

try:
    umur = int(input(f"\n{R}[?] Sila masukkan umur: {W}"))
    
    if umur >= 18:
        slowprint("[+] Umur mencukupi...")
        slowprint("[!] DISINI TIADA LAGI ETIKA.")
        slowprint("[!]JAGA DIRI DENGAN BAIK")
        time.sleep(1)
        
        # Pindah ke station.py
        clear()
        os.system("cd train && python3 station.py")
        
    else:
        print(f"{R}\n[!] UMUR TIDAK MENCUKUPI. ACCESS DENIED.")
        sys.exit() 

except ValueError:
    
    print(f"{R}\n[!] Masukkan nombor lah, jangan main-main!")
    sys.exit()
