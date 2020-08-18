import sys, requests, ipapi, os, socket
from colorama import Fore

def __start__():

    print(Fore.RED + ' [!] Enter Ip Address Or You Dont Know That I Do That :) \n')
    target = input(Fore.BLUE + ' [?] Are You Want To Enter Ip Or Address[ip/ad] ?')

    if target == 'ip':
        target = input(Fore.WHITE + ' [@] Enter The Ip: >>> ')
    elif target == 'ad':
        target = input(Fore.WHITE + ' [@] Enter The Address: >>>')
        target = socket.gethostbyname(target)
    else:
        target = input(Fore.WHITE + ' [@] Enter To Get Information Abot Your PC: >>>')

    sou = ipapi.location(ip=target, key=None)
    print(Fore.LIGHTGREEN_EX + ' [+] See Your Info : ')
    try:
        print(Fore.GREEN + ' [!] ip = ' + sou['ip'])
        print(Fore.GREEN + ' [!] city = ' + sou['city'])
        print(Fore.GREEN + ' [!] region = ' + sou['region'])
        print(Fore.GREEN + ' [!] id country = ' + sou['country'])
        print(Fore.GREEN + ' [!] country = ' + sou['country_name'])
        print(Fore.GREEN + ' [!] calling code = ' + sou['country_calling_code'])
        print(Fore.GREEN + ' [!] language = ' + sou['language'])
        print(Fore.GREEN + ' [!] org = ' + sou['org'])
        try:
            input(Fore.LIGHTBLUE_EX + ' [#] Back To Mneu(Press Enter...)')
        except:
            print('')
            sys.exit()
    except:
        print('')

__start__()
