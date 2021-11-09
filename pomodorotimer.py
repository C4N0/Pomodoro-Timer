# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 15:04:49 2021
@author: C4N0
"""
import webbrowser
import playsound
import random
import time
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%H:%M:%S") # gives you the exact time
print(f"your challenge started at {dt_string}") # tels you when the challenge starts

seconds = 1501 # pomodoro time in seconds (25*60 = 1500)

for sec in range(seconds):
    
    break_time = str(seconds - sec) 
    
    time.sleep(1) # counts the seconds down in 1 second intervals
    
    if break_time == "1": 
        webpage = webbrowser.open("Link to your website (i.e. lichess.org") # opens website to announce break time

break_sec = 401

for sec in range(break_sec): 
    break_end = str(break_sec - sec)
    
    time.sleep(1) # same as above only with your break time
    
    if break_end == "1":
        
        luffy = "path to your soundbite"
        allmight = "path to your soundbite"
        onepiece_overtake = "path to your soundbite"
        grandline = "path to your soundbite"
        eren = "path to your soundbite"
        pain = "path to your soundbite"
        ougon = "path to your soundbite"
        list_of_sounds = [luffy, allmight, onepiece_overtake, grandline, eren, pain, ougon] # saves the soundbites in a list to randomly choose from later
        
        playsound.playsound(random.choice(list_of_sounds)) # plays random soundbite
