import os
import time

with open("config.yaml", "r") as f :
    lines = f.read().split("\n")

files = set(next(os.walk('..'))[2])
while True :
    values = dict()
    for line in lines :
        phrase = line.partition(":")
        values[phrase[0].strip()] = phrase[2].strip()

    os.system("git pull")
    os.system("git add .")
    os.system(f"git commit -a --allow-empty-message -m ''")
    os.system("git push")    
    print("sleeping... \npress ctrl+c to wake me up")
    try :
        # time.sleep(5)
        time.sleep(int(values["refresh_time_minutes"]) * 60)
    except KeyboardInterrupt:
        continue
