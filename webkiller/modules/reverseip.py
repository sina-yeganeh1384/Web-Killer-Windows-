import sys, requests, json, os
from colorama import Fore

def __start__():
    try:
        print(Fore.RED + ' [*] Enter The Ip/Domain \n')
        target = input(Fore.BLUE + ' [@] Enter The Ip/Domain: >>>')

        my_site = {'remoteAddress' : target}
        link = requests.post('https://domains.yougetsignal.com/domains.php', my_site)
        sou = json.loads(link.content)

        #print(sou)

        for data in sou['domainArray']:
            print(Fore.GREEN + data[0] + '\n')
        try:
            input(Fore.LIGHTBLUE_EX + ' [#] Back To Mneu(Press Enter...)')
        except:
            print('')
            sys.exit()
    except:
        print('')

__start__()
