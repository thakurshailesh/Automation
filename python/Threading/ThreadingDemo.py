#Without Threading

#https://www.youtube.com/watch?v=IEEhzQoKtQU


import time
import threading

print("hello World")

start=time.perf_counter()

def do_something(sec):
    sec=sec
    print(f"sleep for {sec} second(s)")
    time.sleep(1)


threads=[]

for _ in range(10):
    t=threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish=time.perf_counter()

print(f"Time taken to complete program is {round(finish-start)} second(s)")
