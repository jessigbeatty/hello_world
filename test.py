import threading
import time
import os

def time_elapsed():
    """
    Counts seconds passed since started and stores them in a global variable, t
    """
    global t
    t = 0
    running = True
    while running:
        t += 1
        time.sleep(1)

def get_time():
    print(t)

def get_input():
    """
    Gets input from user and prints it
    """
    running = True
    while running:
        choice = input("> ")
        print(choice)
        print(t)

#define threads
t1 = threading.Thread(target=time_elapsed)
t2 = threading.Thread(target=get_input)

#start threads
t1.start()
## t2.start()
get_input()

t1.join()
t2.join()
