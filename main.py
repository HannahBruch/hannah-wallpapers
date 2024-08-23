import os
import time

with open("config.yaml", "r") as f : 
    lines = f.read().split("\n")

while(True) :
    values = dict()
    for line in lines : 
        phrase = line.partition(":")
        values[phrase[0].strip()] = phrase[2].strip()

    os.system("git stash")
    os.system("git pull")
    print("sleeping... \npress ctrl+c to wake me up")
    try :

        time.sleep(values["refresh_time_minutes"] as int * 60)
    except KeyboardInterrupt: 
        continue
    
