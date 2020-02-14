#Import Libraries
import concurrent.futures
import time


start=time.perf_counter()

def do_something(sec):
    sec=sec
    #try:
    #    a=1/0
    #except ZeroDivisionError:
    #    print('error')
    print(f"sleeping  for {sec} second(s)..")
    time.sleep(sec)

    #print("Done Sleeping")
    return f'Done Sleeping for {sec} second(s)'

'''
#Use context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    #f1=executor.submit(do_something,1)
    #print(f1.result())
    #Lets use list comprehension
    results=[executor.submit(do_something,sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
'''

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    #f1=executor.submit(do_something,1)
    results=executor.map(do_something,secs) # return in the order they were started. Note Exceptions can be handled only at result set
    for result in results:
        print(result)










finish=time.perf_counter()
print(f"Time taken to complete program is {round(finish-start)} second(s)")
