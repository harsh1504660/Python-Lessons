#EX-9 : ALARM CLOCK

#PROBLEM : MAKE A ONE TIME USABLE ALARM CLOCK :

#SOLUTION:

from datetime import datetime,timedelta,time
import time
import schedule
import pygame as py
import time


query = input('press 1 to create new alarm : ')

def sound(t):
    py.init()
    py.mixer.init()
    sounda= py.mixer.Sound(r"C:\Users\Mrunmay\Downloads\file_example_WAV_1MG.wav")
    sounda.play()
    s=input("press s for stop")
    if s=='s':
        sounda.stop()
        print("thanks for using alarm")
        exit()
    time.sleep (20)
    return
        

def new_alarm():
    set_time = input("set time in form [hrs:min]")
    
    schedule.every().day.at(set_time).do(sound,'hello word')
    while True:
        schedule.run_pending()
        time.sleep(10)

if query =='1':
    new_alarm()
else :
    print("try again")
        



