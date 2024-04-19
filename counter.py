import time

def countdown_timer(seconds):
    while seconds > 0:
        mins= int(seconds/60)
        secs = int(seconds%60)
        print(f'{mins}:{secs}', end = "\r")
        time.sleep(1)
        seconds = seconds - 1
    
    print("Time Up! ")

countdown_timer(5)