# -*- coding: utf-8 -*-
"""
@author: chengmarc
@github: https://github.com/chengmarc

"""
import os
script_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_path)

from uwork_libraries import sys
from uwork_libraries import threading as td
from uwork_libraries import customtkinter as tk
from uwork_functions import stop_execution
from uwork_functions import alt_tab, excel, word


def thread1():
    process = td.Thread(target=alt_tab)
    process.start()
    
    
def thread2():
    process = td.Thread(target=excel)
    process.start()


def thread3():
    process = td.Thread(target=word)
    process.start()
    
    
def stop():
    process = td.Thread(target=stop_execution)
    process.start()


def exit():
    root.destroy()
    sys.exit()    


# %% Set Window Appeareance and Fonts
tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

#from tkinter import Tk, font
#root = Tk()
#print(font.families())

font_intro = ("Segoe UI Black", 18)
font_instr = ("Segoe UI", 14)

    
# %% Initialize Window
root = tk.CTk()
root.title("UWork v1.0")
root.geometry("800x600")
root.iconbitmap("uwork_icon.ico")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

window = tk.CTkFrame(root)    
window.grid(row=0, column=0, sticky="")


# %% Frame 1
frame1 = tk.CTkFrame(window)
frame1.grid(row=1, column=0, padx=20, pady=10, sticky="nswe")


def frame1_intro():
    intro1 = "UWork is your perfect partner while working from home!"
    intro2 = "It does all the work for you so you don't need to."
    
    intro1 = tk.CTkLabel(frame1, anchor="w", text=intro1, font=font_intro)
    intro2 = tk.CTkLabel(frame1, anchor="w", text=intro2, font=font_intro)
    
    intro1.grid(row=0, padx=20, pady=4, sticky="nswe")
    intro2.grid(row=1, padx=20, pady=4, sticky="nswe")
    

def frame1_instruction():    
    instr1 = "1. Switch to English keyboard before starting."
    instr2 = "2. Close MS Word and MS Excel prior to execution."
    instr3 = "3. Click the Stop button or move you mouse to screen corners to stop."

    text1 = tk.CTkLabel(frame1, anchor="w", text=instr1, font=font_instr)
    text2 = tk.CTkLabel(frame1, anchor="w", text=instr2, font=font_instr)
    text3 = tk.CTkLabel(frame1, anchor="w", text=instr3, font=font_instr)
    
    text1.grid(row=2, padx=20, pady=3, sticky="nswe")
    text2.grid(row=3, padx=20, pady=3, sticky="nswe")
    text3.grid(row=4, padx=20, pady=3, sticky="nswe")
    

frame1_intro()
frame1_instruction()
    

# %% Frame 2
frame2 = tk.CTkFrame(window)
frame2.grid(row=2, column=0, padx=20, pady=10, sticky="nswe")


def frame2_button():
    button1 = tk.CTkButton(frame2, text="Start Alt+Tab", command=thread1)
    button2 = tk.CTkButton(frame2, text="Start Excel", command=thread2)
    button3 = tk.CTkButton(frame2, text="Start Word", command=thread3)

    button1.grid(row=0, column=0, padx=20, pady=10, sticky="nswe")
    button2.grid(row=1, column=0, padx=20, pady=10, sticky="nswe")
    button3.grid(row=2, column=0, padx=20, pady=10, sticky="nswe")


def frame2_labels():
    label1 = tk.CTkLabel(frame2, anchor="w", text="Press Alt+Tab non-stop")
    label2 = tk.CTkLabel(frame2, anchor="w", text="Pretend you are working on some spreadsheet")
    label3 = tk.CTkLabel(frame2, anchor="w", text="Pretend you are writing some report")

    label1.grid(row=0, column=1, padx=20, pady=10, sticky="nswe")
    label2.grid(row=1, column=1, padx=20, pady=10, sticky="nswe")
    label3.grid(row=2, column=1, padx=20, pady=10, sticky="nswe")


frame2_button()
frame2_labels()


# %% Frame 3
frame3 = tk.CTkFrame(window)
frame3.grid(row=3, column=0, padx=20, pady=10, sticky="nswe")

frame3.columnconfigure(0, weight=1)
frame3.columnconfigure(1, weight=1)


def frame3_button():
    button1 = tk.CTkButton(frame3, text="Stop", command=stop)
    button2 = tk.CTkButton(frame3, text="Exit", command=exit, fg_color="#AB400C")

    button1.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    button2.grid(row=0, column=1, padx=20, pady=10, sticky="e")


frame3_button()


# %% Launch User Interface
root.mainloop()

