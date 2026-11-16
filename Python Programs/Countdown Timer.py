# Countdown Timer:
import time


seconds = int(input("Enter seconds to start countdown: "))

if seconds < 0:
    print("Error! Invalid Time!")

else:
    while seconds > 0:

        mins, secs = divmod(seconds, 60)

        print(f"\rTime Countdown: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)

        seconds -= 1

    print("\nTime's up!")
