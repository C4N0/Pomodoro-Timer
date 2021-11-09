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
dt_string = now.strftime("%H:%M:%S")
print(f"your challenge started at {dt_string}")

seconds = 1500

for sec in range(seconds):
    
    break_time = str(seconds - sec) 
    
    time.sleep(1)
    
    if break_time == "1": 
        chess = webbrowser.open("Link to your website (i.e. lichess.org")

break_sec = 401

for sec in range(break_sec): 
    break_end = str(break_sec - sec)
    
    time.sleep(1)
    
    if break_end == "1":
        
        luffy = "path to your soundbite"
        allmight = "path to your soundbite"
        onepiece_overtake = "path to your soundbite"
        grandline = "path to your soundbite"
        eren = "path to your soundbite"
        pain = "path to your soundbite"
        ougon = "path to your soundbite"
        list_of_sounds = [luffy, allmight, onepiece_overtake, grandline, eren, pain, ougon]
        
        playsound.playsound(random.choice(list_of_sounds))