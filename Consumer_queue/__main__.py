import threading
import time
import random

maxLen = 10
buffer = []

def producer():
    while True:
        global buffer, maxLen
        if len(buffer) < maxLen:
            buffer.append(random.randint(1,10))
        time.sleep(1)

def consumer():
    while True:
        global buffer
        if len(buffer) > 0:
            data = buffer.pop(0)
        time.sleep(1)

prod = threading.Thread(target=producer, daemon=True)
cons = threading.Thread(target=consumer, daemon=True)
prod.start()
cons.start()
while True:
    print(buffer)