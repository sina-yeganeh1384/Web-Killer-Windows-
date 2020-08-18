import requests, builtwith, sys, time
from colorama import Fore

def __start__():
    print(Fore.RED + ' [*] ENTER DOMAIN TO FIND INFORMATIONS TECNOLOGY \n')
    target = input(Fore.BLUE + ' [@] Plase Enter Domain: >>> ')

    if target == '':
        try:
            print(Fore.BLUE + '  \n [!] Please Enter Domain :) \n')
            time.sleep(5)
            sys.exit()
        except:
            return

    if not 'https://' in target or not 'http://' in target:
        target = 'http://' + target

    info = builtwith.parse(target)
    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val)
        print(Fore.GREEN+"\n"+ Fore.GREEN + ' [!] ' + name +':'+value)
    try:
        input(Fore.LIGHTBLUE_EX +" [#] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()
__start__()
