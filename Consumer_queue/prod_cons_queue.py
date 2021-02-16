import threading
import random

maxLen = 10
buffer = []
mutex = threading.Lock()
iterations = 10

def producer():
    global maxLen, buffer, iterations, mutex
    for i in range(iterations):
        product = random.randint(1, 10)
        mutex.acquire()
        if len(buffer) < maxLen: buffer.append(product)
        mutex.release()
        print(f"PRODUCT {i}: {product}")
        print(f"BUFFER LENGTH: {len(buffer)}")

def consumer():
    global maxLen, buffer, iterations, mutex
    for i in range(iterations):
        mutex.acquire()
        if len(buffer) > 0: product = buffer.pop(0)
        mutex.release()
        print(f"CONSUMPTION {i}: {product}")
        print(f"BUFFER LENGTH: {len(buffer)}")

threadPool = []
threadPool.append(threading.Thread(target=producer, daemon=True))
threadPool.append(threading.Thread(target=consumer, daemon=True))

for thread in threadPool:
    thread.start()

for thread in threadPool:
    thread.join()