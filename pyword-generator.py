import curses
import random
from classes.dimension import tuplexy as tp


def main(stdscr):
    ###################################
    ## Set up the curses environment ##
    ## remove the blinking cursor    ##
    ###################################
    h, w = stdscr.getmaxyx()
    scrWidth = tp(w, h)
    curses.curs_set(0)
    currentRow = 0
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    #######################################
    ## Create variables to store options ##
    #######################################
    specialCharacters = False
    upperCaseChars = False
    lowerCaseChars = True
    useNumbers = True
    wordLength = 16
    generatedPassword = "Press g to generate a new password"
    generateNewPassword = False

    ##############################
    ## Generate the two windows ##
    ##############################
    generatedPassword = printMainViewToScreen(scrWidth, specialCharacters, upperCaseChars, lowerCaseChars, useNumbers, wordLength, generatedPassword, generateNewPassword)
    generateNewPassword = False

    #######################
    ## Main Program Loop ##
    #######################
    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP:
            wordLength = wordLength + 1
        elif key == curses.KEY_DOWN:
            wordLength = wordLength - 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            #print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            #tmp = 1
            #tmp += 1
            # if user selected last row, exit the program
            #if currentRow == len(menu)-1:
                #break
            a = 1
        elif key == ord('q'):
            break
        elif key == ord('s'):
            if specialCharacters == False:
                specialCharacters = True
            else:
                specialCharacters = False
        elif key == ord('u'):
            if upperCaseChars == False:
                upperCaseChars = True
            else:
                upperCaseChars = False
        elif key == ord('l'):
            if lowerCaseChars == False:
                lowerCaseChars = True
            else:
                lowerCaseChars = False
        elif key == ord('n'):
            if useNumbers == False:
                useNumbers = True
            else:
                useNumbers = False
        elif key == ord('g'):
            if generateNewPassword == False:
                generateNewPassword = True
            else:
                generateNewPassword = False
        
        generatedPassword = printMainViewToScreen(scrWidth, specialCharacters, upperCaseChars, lowerCaseChars, useNumbers, wordLength, generatedPassword, generateNewPassword)
        generateNewPassword = False
    
def printMainViewToScreen(screenWidth, specials, upper, lower, numbers, length, password, generateNew):
    optionsView = createOptionsView(screenWidth, specials, upper, lower, numbers, length)
    optionsView.refresh()
    passwordView, genedPassword = createPasswordView(screenWidth, password, generateNew, specials, upper, lower, numbers, length)
    passwordView.refresh()
    return genedPassword

def createOptionsView(screenWidth, specials, upper, lower, numbers, length):
    listWindow = curses.newwin(screenWidth.gety(), screenWidth.getx25(), 0, 0)
    listWindow.addstr(1, 1, "Key | Selected | Description")
    if specials == True:
        listWindow.addstr(2, 1, "s | T | Special Characters")
    else:
        listWindow.addstr(2, 1, "s | F | Special Characters")
    if upper == True:
        listWindow.addstr(3, 1, "u | T | Upper Case Characters")
    else:
        listWindow.addstr(3, 1, "u | F | Upper Case Characters")
    if lower == True:
        listWindow.addstr(4, 1, "l | T | Lower Case Characters")
    else:
        listWindow.addstr(4, 1, "l | F | Lower Case Characters")
    if numbers == True:
        listWindow.addstr(5, 1, "n | T | Use Numbers")
    else:
        listWindow.addstr(5, 1, "n | F | Use Numbers")
    listWindow.border(1)
    listWindow.addstr(6, 1, "g |   | Generate")
    listWindow.addstr(8, 1, "Password Length = " + str(length))
    listWindow.addstr(9, 1, "Up arrow to increase")
    listWindow.addstr(10, 1, "Down arrow to decrease")

    return listWindow

def createPasswordView(screenWidth, password, generateNew, specials, upper, lower, numbers, length):
    wordWindow = curses.newwin(screenWidth.gety(), screenWidth.getx75(), 0, screenWidth.getx25())
    if generateNew == False:
        wordWindow.addstr(1, 1, password)
    else:
        password = genNewPassword(specials, upper, lower, numbers, length)
        wordWindow.addstr(1, 1, password)

    return wordWindow, password

def genNewPassword(specials, upper, lower, numbers, length):
    if checkSelectedOptions(specials, upper, lower, numbers):
        selectionString = ""
        if lower == True:
            selectionString = selectionString + "abcdefghijklmnopqrstuvwxyz"
        if upper == True:
            selectionString = selectionString + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if numbers == True:
            selectionString = selectionString + "0123456789"
        if specials == True:
            selectionString = selectionString + "=-_+/?!@#$%^&*()\\|"
        
        p =  "".join([random.choice(selectionString) for _ in range(length)])
        return p
    else:
        return "Please select at least one option"

def checkSelectedOptions(specials, upper, lower, numbers):
    #If one or more options are selected, return true else return false because no options are selected
    if specials == False and upper == False and lower == False and numbers == False:
        return 0
    else:
        return 1

curses.wrapper(main)