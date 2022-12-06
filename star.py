import time


loading = 1

print("Loading : ")
while loading<10:
    time.sleep(0.3)
    print("█", end = '')
    loading += 1