import sys, requests, time, os
from colorama import Fore

def __start__():
    print(Fore.WHITE + ' [!] Befor Use It, Turn On Your VPN...')

    print(Fore.RED + ' [*] ENTER THE IP/DOMAIN \n ')
    target = input(Fore.BLUE + ' [@] Enter The Ip/Domain: >>> ')

    if target == '':
        try:
            print(Fore.WHITE + ' \n [!] Enter The Ip/Domain :) ')
            time.sleep(5)
            sys.exit()
        except:
            return

    result = requests.get('https://api.hackertarget.com/dnslookup/?q=' + target).text
    print(Fore.GREEN + result)

    try:
        input(Fore.LIGHTBLUE_EX + ' [#] Back To Menu(Press Enter...)')
    except:
        print('')
        sys.exit()

__start__()
