#Without Threading
import time
print("hello World")

start=time.perf_counter()

def do_something():
    sec=1
    print(f"sleep for {sec} second(s)")
    time.sleep(1)

for _ in range(10):
    do_something()

finish=time.perf_counter()

print(f"Time taken to complete program is {round(finish-start)} second(s)")
