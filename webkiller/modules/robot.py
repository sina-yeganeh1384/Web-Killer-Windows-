import requests, sys, time
from colorama import Fore

search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']


def __start__():
    try:
        print(Fore.RED + ' [*] Enter The Domain \n')
        url = input(Fore.BLUE + ' [@] Enter The Address: >>> ')

        if 'http' in url:
            pass
        elif 'http' not in url:
            url = ('http://' + url)

        for i in search:
            time.sleep(0.3)

            ur = (url + '/' + i)
            request = requests.get(ur)
            if request.status_code == 200 or request.status_code == 405:
                print(Fore.GREEN + ' [+] ' + ur)
            else:
                print(Fore.LIGHTRED_EX + ' [-] ' + ur)

        try:
            input(Fore.LIGHTBLUE_EX + ' [#] Back To Menu(Press Enter...)')
        except:
            print('')
            sys.exit()
    except:
        print('')

__start__()
