from datetime import datetime
import time

while True:
    print("► ", datetime.now().strftime("%H:%M:%S"), " ◄", end="\r")
    time.sleep(0.5)
