import threading
import time
import os

### A game where you try to guess how much time has passed since you started running the game.

def time_elapsed():
    """Counts seconds passed since started and stores them in a global variable, t
    """
    global t
    global running
    t = 0
    while running:
        t += 1
        time.sleep(1)
        if t == 30:
            running = False

def get_guess():
    choice = input("Guess how many seconds I've been running: ")
    try:
        os.system('clear')
        value = int(choice)
        print(f"You guessed I've been running {choice} seconds?")
        print(f"Actually, I've been running {t} seconds.")
        diff = t - value 
        print(f"You were off by {diff} seconds.\n")
        return diff
    except ValueError:
        print("Please enter an integer number of seconds.\n")

def calculate_score(diff):
    global score
    try:
        score += round((1/abs(diff))*100)
    except ZeroDivisionError:
        score += 250
    except TypeError:
        pass

# declaring global vars (mostly for clarity)
global t; global running; global score

# Start clock, set running to True, initialize score
running = True
t1 = threading.Thread(target=time_elapsed)
score = 0

t1.start()

while running:
    diff = get_guess()
    calculate_score(diff)
    print(f"Your score is: {score}\n")

t1.join()
