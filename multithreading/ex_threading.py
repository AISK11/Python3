#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################
## Demo example how to use threading in Python3.


################################################################################
##                                  Theory                                    ##
################################################################################
'''
Multithreading or Multiprocessing?
- CPU bound -> program spends most of the time waiting for internal events,
               (CPU intensive), use multiprocessing.

- I/O bound -> program spends most of the time waiting for external events,
               (user input, web scraping...), use multithreading.


Threads:
- 1st thread is main thread for the program.
- each time we create new separate thread.


Additional resources:
- https://www.youtube.com/watch?v=3dEPY3HiPtI
- https://www.youtube.com/watch?v=IEEhzQoKtQU&list=RDCMUCCezIgC97PvUuR4_gbFUs5g
'''


################################################################################
##                                  Modules                                   ##
################################################################################
## Docs: https://docs.python.org/3/library/time.html
import time
## Docs: https://docs.python.org/3/library/threading.html
import threading


################################################################################
##                                 Functions                                  ##
################################################################################
## Function, that takes (5) seconds to finish execution.
def function_1(exec_time: int = 5):
    print(f"Function 1 started.")
    time.sleep(exec_time)
    print(f"Function 1 finished after {exec_time} seconds.")


## Function, that takes (3) seconds to finish execution.
def function_2(exec_time: int = 3):
    print(f"Function 2 started.")
    time.sleep(exec_time)
    print(f"Function 2 finished after {exec_time} seconds.")


## Function, that takes always 6 seconds to finish execution.
def function_3():
    print(f"Function 3 started.")
    static_seconds = 6
    time.sleep(static_seconds)
    print(f"Function 3 finished after {static_seconds} seconds.")


## Function, that prints out how many threads are currently running.
def show_active_threads():
    print(f"Current threads running: {threading.active_count()}")


## Program starting function.
def main():
    ## Start time of the program.
    program_start = time.perf_counter()

    ## Create thread to execute "target" function and optionally pass arguments.
    t1 = threading.Thread(target=function_1, args=(7,))
    t2 = threading.Thread(target=function_2, args=(5,))
    t3 = threading.Thread(target=function_3, args=())

    ## Start threads.
    t1.start()
    t2.start()
    t3.start()

    ## Shows how many threads are running (executed with Main Thread).
    show_active_threads()

    ## Wait until each thread finished execution.
    t1.join()
    t2.join()
    t3.join()

    ## Shows how many threads are running (executed with Main Thread).
    show_active_threads()

    ## Show how many seconds the program took to execute.
    program_finish = time.perf_counter()
    print(f"Program finished in {round(program_finish-program_start, 2)} second(s).")


## Python3 program start execution.
if __name__ == "__main__":
    main()
