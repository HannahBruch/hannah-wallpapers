import os
import time

with open("config.yaml", "r") as f : 
    lines = f.read().split("\n")

while(True) :
    values = dict()
    for line in lines : 
        phrase = line.partition(":")
        values[phrase[0].strip()] = phrase[2].strip()

    print("fetching...")
    os.system("git fetch")
    print("sleeping... \npress ctrl+c to wake me up")
    try :
        time.sleep(5)
        # time.sleep(values["refresh_time_minutes"] * 60)
    except KeyboardInterrupt: 
        continue
    
