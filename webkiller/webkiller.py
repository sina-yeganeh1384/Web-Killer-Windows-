import os, sys, socket, time
from helplist import help
from moduls import *

while True:

    try:
        help.banner()
        help.infolist1()
        number = input(Fore.BLUE + ' [^] Enter The Number: ')
    except:
        print('\n By By !')
        sys.exit()

    if number == '4':

        print('')
        sys.exit()

    elif number == '3':

         help.infolist4()

    elif number == '':

        print('')
        input(Fore.BLUE + ' [^] Number!!!')

    elif number == '1':
