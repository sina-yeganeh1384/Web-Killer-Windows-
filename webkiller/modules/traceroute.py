import sys, requests
from colorama import Fore

def __start__():
    try:
        print(Fore.RED + ' [*] Enter The Address \n')
        target = input(Fore.BLUE + ' [@] Enter The Address: >>>')

        result = requests.get('http://api.hackertarget.com/mtr/?q=' + target).text
        print(Fore.GREEN + result)

        try:
            input(Fore.LIGHTBLUE_EX + ' [#] Back TO Menu(Press Enter...)')
        except:
            priint('')
            sys.exit()
    except:
        print('')

__start__()
