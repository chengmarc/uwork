# -*- coding: utf-8 -*-
"""
@author: chengmarc
@github: https://github.com/chengmarc

"""
import uwork_libraries as ulib


def start_execution():
    global should_run
    should_run = True
    ulib.debug_start()


def stop_execution():
    global should_run
    should_run = False
    ulib.debug_end()
    

def alt_tab():
    start_execution()
    
    iteration = 0    
    while should_run:
        
        """
        Docstring
        """
        try:
            ulib.ui.hotkey("alt", "tab")
            ulib.ui.sleep(5)
            iteration += 1
            
        except KeyboardInterrupt:
            ulib.debug_interrupt()
            break
    
    ulib.debug_complete()


def word():
    start_execution()
    ulib.intialize_word()    

    iteration = 0
    while should_run:
        
        """
        Docstring
        """
        try:
            selection = ulib.text_select()
            string = ulib.read_selection(selection)            
            batch = ulib.split_string(string)
            
            count = 0
            while should_run:            
                ulib.ui.write(batch[count], interval=0.01)
                count += 1
                
            iteration += 1
            
        except KeyboardInterrupt:
            ulib.debug_interrupt()
            break
    
    ulib.debug_complete()
    
            
def excel():
    start_execution()    
    ulib.intialize_excel()
    
    count = 0
    while should_run:
        
        """
        Docstring
        """
        try:
            selection = ulib.pool_select()
            iteration = 0
            
            if selection == "number":
                digits = ulib.random.randint(3, 14)
                count = 0
                while should_run:
                    ulib.enter_number(digits)
                    count += 1
                    if count == 30: break
                
            elif selection == "code":   
                length = ulib.random.randint(6, 10)  
                count = 0
                while should_run:
                    ulib.enter_code(length)
                    count += 1
                    if count == 30: break
                
            elif selection == "country":  
                count = 0
                while should_run:
                    ulib.enter_country()
                    count += 1
                    if count == 30: break
            elif selection == "time":
                count = 0
                while should_run:
                    ulib.enter_time()
                    count += 1
                    if count == 30: break
            elif selection == "boolean":
                count = 0
                while should_run:
                    ulib.enter_boolean()
                    count += 1
                    if count == 30: break
                            
            ulib.tab_up()
            iteration += 1
            if iteration == 7:
                iteration = 0
                
        except KeyboardInterrupt:
            ulib.debug_interrupt()
            break
    
    ulib.debug_complete()
            
