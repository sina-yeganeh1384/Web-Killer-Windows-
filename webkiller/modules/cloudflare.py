import socket
import sys
import time
from colorama import Fore
def __start__():
    try:
        print(Fore.RED + " [*] PLASE ENTER THE TARGET WEBSITE ADDERES\n")
        subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

        site = input(Fore.BLUE + ' [@] Plase Enter Adress: >>> ')
        if site == "":
            try:
                print(Fore.BLUE+" [!] Please Enter Address :) \n")
                time.sleep(5)
                sys.exit()
            except:
                return
        site = site.replace('https://', '').replace('http://', '')
        for sub in subdom:
            try:
                hosts = str(sub) + "." + str(site)
                bypass = socket.gethostbyname(str(hosts))
                #print('Cloudflare Bypassed ! Real IP Address => '+ bypass)
                print (Fore.GREEN + " \n [!] CloudFlare Bypass " + Fore.GREEN + str(bypass) + Fore.GREEN + ' | ' + Fore.GREEN + str(hosts))
            except Exception:
                pass
        print('')
        try:
            input(Fore.LIGHTBLUE_EX +" [#] Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print('')
__start__()
