import os
import time
from threading import Thread

introtext = "Your eye flickers open and sees red dunes extending to the south. The sky overhead is black and brilliant with stars. You are alone."

n=0

def count():
    global n
    while True:
        time.sleep(1)
        n += 1

def display(text):
    global n
    os.system("clear")
    print(text)
    print(f"time elapsed: {n}")
    time.sleep(.5)

def get_input(prompt):
    choice = input(prompt)
    return choice

while True:
    Thread(target = display(introtext)).start()
    Thread(target = count).start()
