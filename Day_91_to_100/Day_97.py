import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    time1=time.perf_counter()
    

#Noremal Code 
# func(4)
# func(2)
# func(1)

#Same Code Using a Thread 

    t1=threading.Thread(target=func,args=[4])
    t2=threading.Thread(target=func,args=[2])
    t3=threading.Thread(target=func,args=[1])
    t1.start()
    t2.start()
    t3.start()
    time2=time.perf_counter()   


    print("Total Time is " ,time2-time1)


def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future=executor.submit(func,3)
        # future=executor.submit(func,2)
        # future=executor.submit(func,5)
        # print(future.result())
        # print(future.result())
        # print(future.result())

        l=[3,5,1,2]
        results=executor.map(func,l)
        for result in results:
            print(result)

poolingDemo()