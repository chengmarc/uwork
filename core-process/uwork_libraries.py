# -*- coding: utf-8 -*-
"""
@author: chengmarc
@github: https://github.com/chengmarc

"""
import os, sys, time, string, random, getpass, threading
script_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_path)

try:
    import customtkinter
    import pyautogui as ui
    from colorama import init, Fore
    init()
    print(Fore.GREEN + "Core modules imported.")

except ImportError as e:
    print(f"The module '{e.name}' is not found, please install it using either pip or conda.")
    getpass.getpass("Press Enter to quit in a few seconds...")
    sys.exit()


# %% Word related functions


def intialize_word():
    ui.hotkey("win", "r")
    ui.sleep(2)
    ui.write('winword', interval=0.1)
    ui.sleep(2)
    ui.press('enter') #Start Word
    ui.sleep(3)
    ui.press('enter') #Select blank sheet
    

def text_select():
    text = ["uwork_report.txt"]    
    num = random.randint(0, len(text)-1)
    return text[num]


def read_selection(selection):    
    with open(selection, "r") as f:
        string = f.read()
        f.close()
    return string


def split_string(string):
    chunks, chunk_size = len(string), len(string)//10
    batch = [string[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    return batch


# %% Excel related functions

    
def intialize_excel():
    ui.hotkey("win", "r")
    ui.sleep(2)
    ui.write('excel', interval=0.1)
    ui.sleep(2)
    ui.press('enter') #Start Excel
    ui.sleep(3)
    ui.press('enter') #Select blank sheet
    

def pool_select():
    pool = ["number", "number", "number", "number", 
            "code", "code", "code", "code", "code", "code", 
            "boolean", "boolean", "boolean", 
            "country", "country",
            "time"]
    num = random.randint(0, len(pool)-1)
    return pool[num]


def enter_number(digits):
    lowerbound = 10**digits
    upperbound = 10**(digits+1)-1
    num = random.randint(lowerbound, upperbound)
    string = str(num)
    ui.write(string, interval=0.01)
    ui.press("enter")


def enter_code(length):
    characters = string.ascii_uppercase + string.digits
    randcode = ''.join(random.choice(characters) for _ in range(length))
    ui.write(randcode, interval=0.01)
    ui.press("enter")


def enter_boolean():
    boolean = random.randint(0, 1)
    if boolean == 0:
        ui.write("FALSE", interval=0.01)
        ui.press("enter")
    else:
        ui.write("TRUE", interval=0.01)
        ui.press("enter")


def enter_country():    
    boolean = random.randint(0, 8)
    if boolean == 0:
        ui.write("China", interval=0.01)
        ui.press("enter")
    elif boolean == 1:
        ui.write("Canada", interval=0.01)
        ui.press("enter")
    elif boolean == 2:
        ui.write("Germany", interval=0.01)
        ui.press("enter")
    elif boolean == 3:
        ui.write("France", interval=0.01)
        ui.press("enter")
    elif boolean == 4:
        ui.write("England", interval=0.01)
        ui.press("enter")
    elif boolean == 5:
        ui.write("Japan", interval=0.01)
        ui.press("enter")
    else:
        ui.write("United States", interval=0.01)
        ui.press("enter")
    
    
def enter_time():
    """
    Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime("1/1/2021 1:30 PM", '%m/%d/%Y %I:%M %p'))
    etime = time.mktime(time.strptime("10/31/2023 4:50 AM", '%m/%d/%Y %I:%M %p'))
    ptime = stime + random.random() * (etime - stime)

    timestr = time.strftime('%m/%d/%Y %I:%M %p', time.localtime(ptime))
    ui.write(timestr, interval=0.01)
    ui.press("enter")
    

def tab_up():
    ui.press("tab")
    ui.sleep(1)
    for i in range(50):
        ui.press("up")


# %% Functions for debug notice    
    
    
def debug_start():
    print(Fore.GREEN + "Global value set to true")
    
    
def debug_end():
    print(Fore.RED + "Global value set to false")


def debug_interrupt():
    print(Fore.YELLOW + "Keyboard Interrupt")
    
    
def debug_complete():
    print(Fore.YELLOW + "Execution completed")
    
