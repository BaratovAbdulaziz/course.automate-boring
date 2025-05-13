import os
import time

counter = 0
while True:
    counter += 1
    print(counter)
    time.sleep(1)
    os.system('clear')
    # os.system('cls')