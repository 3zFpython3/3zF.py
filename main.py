import requests, os

# Colors
P = '\033[95m'
G = '\033[92m'
R = '\033[91m'
W = '\033[0m'

os.system('clear')

# 3zF Logo
logo = f"""{P}
 ██████╗ ███████╗███████╗
 ╚════██╗╚══███╔╝██╔════╝
  █████╔╝  ███╔╝ █████╗  
  ╚═══██╗ ███╔╝  ██╔══╝  
 ██████╔╝███████╗██║     
 ╚═════╝ ╚══════╝╚═╝{W}
{G}=============================={W}
{R}      Dev by 3zF | v1.0{W}
{G}=============================={W}"""

print(logo)

# Logic
try:
    url = input(f"{P}[+]{W} URL: ")
    msg = input(f"{P}[+]{W} MSG: ")
    
    print(f"\n{P}[*]{W} Sending...")
    
    r = requests.post(url, json={'content': msg})
    
    if r.status_code == 204:
        print(f"{G}[✔] Success{W}")
    else:
        print(f"{R}[✘] Failed: {r.status_code}{W}")
        
except KeyboardInterrupt:
    print(f"\n{R}[!] Stopped{W}")
except Exception as e:
    print(f"\n{R}[!] Error: {e}{W}")
