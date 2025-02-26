# Day 1 :
"making live working clock using datetime module"

import datetime
import time

print("Live Time")
while True:
    now = datetime.datetime.now()
    print("\r", now.strftime("%H:%M:%S"), flush=True, end="")
    time.sleep(1)