import requests, sys, os, time
from colorama import Fore

def __start__():
    try:
        print(Fore.WHITE + ' [!] Befor Use It, Turn On Your VPN... \n')

        print(Fore.RED + ' [*] Enter THe Domain/Address')
        target = input(Fore.BLUE + ' [@] Enter The Address: >>>')

        result = requests.get('http://api.hackertarget.com/findsharedns/?q=' + target).text
        print(Fore.GREEN + result)

        try:
            input(Fore.LIGHTBLUE_EX + ' [#] Back To Menu(Press Enter)')
        except:
            print('')
            sys.exit()
    except:
        print('')

__start__()
