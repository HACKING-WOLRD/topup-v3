import os
import time
import sys

# Colors
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
P = '\033[95m'

def banner():
    os.system('clear')
    print(f"""{G}
██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗██╗ ██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██║██╔═══██╗
██████╔╝█████╗  ███████║██║  ██║██╔████╔██║██║██║   ██║
██╔═══╝ ██╔══╝  ██╔══██║██║  ██║██║╚██╔╝██║██║██║   ██║
██║     ███████╗██║  ██║██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝ 
{P}HACKING WORLD™ - FREE FIRE DIAMOND HACK VIP TOOL
{Y}---------------------------------------------------
""")

def loading_animation(text, duration=4):
    spinner = ['|', '/', '-', '\\']
    sys.stdout.write(Y + text + " ")
    for i in range(duration*4):
        sys.stdout.write(spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write('\b')
    print(G + "✓")

def main():
    banner()
    uid = input(f"{C}[+] Enter Free Fire UID: {W}")
    loading_animation("Connecting to Garena Server", 3)
    print(f"{G}[✓] UID Verified: {uid}")
    time.sleep(1.5)
    print(f"{Y}[!] Injecting Diamonds Package...")
    loading_animation("Processing", 5)
    print(f"\n{R}[X] ERROR: Your Phone is in Full Security Mode.")
    print(f"{Y}[!] Please Disable Security Mode to Continue.")
    input(f"\n{W}Press Enter to Exit...")

main()