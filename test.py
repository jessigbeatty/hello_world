import threading
import time
import os

def time_elapsed():
    """Counts seconds passed since started and stores them in a global variable, t
    """
    global t
    t = 0
    running = True
    while running:
        t += 1
        time.sleep(1)

def get_input():
    """Gets input from user and prints it
    """
    running = True
    while running:
        choice = input("> ")
        print(choice)
        print(t)

def get_and_score():
    running = True
    while running:
        global score; score=0
        choice = input("Guess how many seconds I've been running: ")
        print(f"You guessed I've been running {choice} seconds??")
        print(f"Actually, I've been running {t} seconds.\n")
        
#define threads
t1 = threading.Thread(target=time_elapsed)
##t2 = threading.Thread(target=get_input)

#start threads
t1.start()
## t2.start()

get_and_score()


