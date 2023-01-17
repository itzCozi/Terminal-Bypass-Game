# https://github.com/joshdentremont/fallout-terminal
# add a way to skip the boot sequence

from colorama import Fore, Style
import login as login
import boot as boot
import locked as locked
import hack as hack
import sys, signal
import time

hard = False

if boot.beginBoot(hard):
  pwd = hack.beginLogin()
  if pwd != None:
    login.beginLogin(hard, '| ADVISOR', pwd)
    print(Fore.GREEN+'ACCESS GRANTED'+Style.RESET_ALL)
    time.sleep(500)
  else:
    locked.beginLocked()
    print('Login: failed | Location: failed')