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
from uwork_functions import alt_tab


def thread():
    process = td.Thread(target=alt_tab)
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
root.title("UWork Lite")
root.iconbitmap("uwork_icon.ico")
root.resizable(width=False, height=False)

window = tk.CTkFrame(root)
window.grid(padx=40, pady=40)


# %% Frame 1
frame1 = tk.CTkFrame(window)
frame1.grid(row=1, column=0, padx=20, pady=10, sticky="nswe")


def frame1_intro():
    intro1 = "UWork Lite"
    intro1 = tk.CTkLabel(frame1, anchor="w", text=intro1, font=font_intro)
    intro1.grid(row=0, padx=20, pady=4, sticky="nswe")


frame1_intro()


# %% Frame 2
frame2 = tk.CTkFrame(window)
frame2.grid(row=2, column=0, padx=20, pady=10, sticky="nswe")


def frame2_button():
    button1 = tk.CTkButton(frame2, text="Start Alt+Tab", command=thread)
    button1.grid(row=0, column=0, padx=20, pady=10, sticky="nswe")


def frame2_labels():
    label1 = tk.CTkLabel(frame2, anchor="w", text="Press Alt+Tab non-stop")
    label1.grid(row=0, column=1, padx=20, pady=10, sticky="nswe")


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

