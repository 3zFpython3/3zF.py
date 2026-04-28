import os
import time
from colorama import Fore

def startup():
    os.system('clear')
    print(f"{Fore.MAGENTA}--- 3zF.py IS STARTING ---")
    print(f"{Fore.CYAN}Checking requirements...")
    time.sleep(1)
    print(f"{Fore.GREEN}System Ready!")
    print(f"{Fore.WHITE}--------------------------")

if __name__ == "__main__":
    startup()
