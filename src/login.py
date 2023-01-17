import curses
from colorama import Fore, Style
from functions import slowWrite
from functions import INPUT_PAUSE
from functions import TYPE_DELAY
from functions import upperInput
from functions import HIDDEN_MASK
################## text strings ######################

HEADER_TEXT = 'WELCOME TO THE-COMBINE (TM) TERMLINK'

PASSWORD_PROMPT = 'ENTER PASSWORD'

PASSWORD_CORRECT = Fore.GREEN+'ACCESS GRANTED...'

PASSWORD_ERROR = 'INCORRECT PASSWORD, PLEASE TRY AGAIN'

################## global "constants" ################

ENTRY = 'LOGON '

################## functions #########################

def runLogin(scr, hardMode, username, password):
    """
    Start the login process

    hardMode - boolean indicating whether the user has to enter the username 
               and password or if they are entered automatically
    username - the username to log in
    password - the password to log in
    Returns true if hardMode == false or if the user entered the correct string
    """
    curses.use_default_colors()
    scr.erase()
    scr.move(0, 0)

    curses.noecho()
    scr.scrollok(True)

    slowWrite(scr, HEADER_TEXT + '\n\n')
    slowWrite(scr, PASSWORD_PROMPT + '\n\n')

    if hardMode:
        print("HardMode")
    else:
      #FUCTION RAN
         # user must enter the correct text to proceed
        entry = ''
        while entry.upper() != password.upper():
            if entry:
                slowWrite(scr, PASSWORD_ERROR + '\n\n')
            
            slowWrite(scr, '> ')
            entry = upperInput(scr, True)

    curses.napms(500)

def beginLogin(hardMode, username, password):
    """
    Initialize curses and start the login process

    hardMode - boolean indicating whether the user has to enter the username
               and password or if they are entered automatically
    username - the username to log in
    password - the password to log in
    Returns true if hardMode == false or if the user entered the correct string
    """
    res = curses.wrapper(runLogin, hardMode, username, password)
    return res
