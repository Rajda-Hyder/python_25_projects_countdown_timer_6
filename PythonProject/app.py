#imports
import time

#function for countdown Timer
def countdown(t, display = True):
    """Countdown timer from t seconds. If display=False, skips printing."""

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}' .format(mins, secs)
        if display:
            print(timer, end = "\r")
        time.sleep(1)
        t -= 1
    if display:    
        print("Timer completed successfully!")

#  prevents input() from running during test import
if __name__ == "__main__":
    t = input("Enter Time in seconds: ")
    countdown(int(t))