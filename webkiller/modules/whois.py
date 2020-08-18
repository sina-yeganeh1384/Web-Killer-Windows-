import sys, requests
from colorama import Fore

def __start__():
    try:

        print(Fore.LIGHTRED_EX + ' [*] Enter The Address \n')
        target = input(Fore.BLUE + ' [@] Enter The Address: >>> ')

        result = requests.get('http://api.hackertarget.com/whois/?q=' + target).text
        print(Fore.GREEN + result)

        try:
            input(Fore.LIGHTBLUE_EX + ' [#] Back To Menu(Press Enter...)')
        except:
            print('')
            sys.exit()

    except:
        print('')

__start__()
