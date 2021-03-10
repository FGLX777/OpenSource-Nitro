import requests, os, colorama, random, string, threading
from os import system
from colorama import Fore, Style
colorama.init()


def logo():
    msg = Fore.LIGHTBLUE_EX +"""
___________             .__                   __             .___  _______  .__  __                 
\_   _____/ ____   ____ |  |__ _____    _____/  |_  ____   __| _/  \      \ |__|/  |________  ____  
 |    __)_ /    \_/ ___\|  |  \ __  \  /    \   __\/ __ \ / __ |   /   |   \|  \   __\_  __ \/  _ \ 
 |        \   |  \  \___|   Y  \/ __ \|   |  \  | \  ___// /_/ |  /    |    \  ||  |  |  | \(  <_> )
/_______  /___|  /\___  >___|  (____  /___|  /__|  \___  >____ |  \____|__  /__||__|  |__|   \____/ 
        \/     \/     \/     \/     \/     \/          \/     \/          \/
    """
    print(msg)

def menu():
    os.system("cls")
    system("title " + "Enchanted Nitro by FGLX#9999")
    logo()
    print("")
    print("{} ╔═══Main Menu═════════════════╗{}".format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX))
    print(Fore.LIGHTMAGENTA_EX + " ║" + Fore.LIGHTBLUE_EX + "[1] -" + Fore.RESET + " Nitro AutoPilot " + Fore.LIGHTMAGENTA_EX + "       ║" + Fore.RESET)
    print("{} ╚═════════════════════════════╝{}".format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX))


hit = 0
check = 0
bad = 0
proxies = 0

def nitroNormal():
    global check
    global hit
    global bad
    global proxies
    while True:
        with open(txt) as f:
            for line in f:
                prox = line.strip("\n")
                proxy = {
                    'https' : f'http://{prox}'
                }
                system("title " + "Hits:" + f'{hit}' + " Bad:" + f'{bad}' + " Checked:" + f'{check}' + " Dead Proxies:" + f'{proxies}')
                code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
                try:
                    r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/"+code+"?with_application=false&with_subscription_plan=true", proxies=proxy, timeout=timeouttime)
                    if r.status_code == 200:
                        check += 1
                        hit += 1
                        print(Fore.GREEN+"Valid"+Fore.LIGHTWHITE_EX+" | "+Fore.BLUE+"fdiscord.gift/{code} ")
                        print(Fore.YELLOW+"Proxy in use "+Fore.LIGHTWHITE_EX+" | "+Fore.GREEN+f"{prox}")
                        with open("Results/Good.txt", "a+") as (k):
                            k.writelines(f"discord.gift/{code}" + " | GOOD | \n")
                    else:
                        check += 1
                        bad += 1
                        print(Fore.RED+"Invalid"+Fore.LIGHTWHITE_EX+" | "+Fore.BLUE+f"discord.gift/{code} ")
                        print(Fore.YELLOW+"Proxy in use "+Fore.LIGHTWHITE_EX+"|"+Fore.GREEN+f" {prox}")
                        with open("Results/Bad.txt", "a+") as (f):
                            f.writelines(f"discord.gift/{code}" + " | BAD | \n")
                except:
                    print(Fore.RED+"Proxy Dead"+Fore.LIGHTWHITE_EX+" |"+Fore.RED+f" {prox}")
                    proxies += 1
                    pass


menu()
print(Fore.LIGHTBLUE_EX)
option = int(input("[?]"))

while option != 0:
    if option == 1:
        os.system("cls")
        logo()
        txtname = input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +"import Https Proxys:"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX)
        txt = f"{txtname}.txt"
        timeouttime = int(input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +"Proxy Timeout Time:"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX))
        print("Dont use more then 100 if you dont have HQ proxies")
        threads = int(input(Fore.LIGHTWHITE_EX+"["+Fore.YELLOW +"Amount of Threads:"+Fore.LIGHTWHITE_EX+"]"+Fore.LIGHTBLUE_EX))
        os.system("cls")
        for x in range(threads):
            x = threading.Thread(target=nitroNormal)
            x.start()
        pass
    else:
        print("Invalid Option")
        os.system("cls")
        menu()
        print(Fore.LIGHTBLUE_EX)
        option = int(input("[?]"))


