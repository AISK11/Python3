#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################


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
- each time we create new separate thred.


Additional resources:
- https://www.youtube.com/watch?v=3dEPY3HiPtI
'''
################################################################################
##                                  Modules                                   ##
################################################################################
## Docs: https://docs.python.org/3/library/threading.html
import threading
import time


################################################################################
##                                 Functions                                  ##
################################################################################
## Function, that takes (5) seconds to finish execution.
def function_1(exec_time: int = 5):
    time.sleep(exec_time)
    print(f"Function 1 finished after {exec_time} seconds.")


## Function, that takes (3) seconds to finish execution.
def function_2(exec_time: int = 3):
    time.sleep(exec_time)
    print(f"Function 2 finished after {exec_time} seconds.")


## Function, that takes always 6 seconds to finish execution.
def function_3():
    time.sleep(6)
    print(f"Function 3 finished after 6 seconds.")


## Function, that prints out how many threads are currently running.
def show_active_threads():
    print(f"Currently are running {threading.active_count()} threads.")


## Starting function.
def main():
    ## Create thread to execute function_1() in 4 seconds instead.
    thd_1 = threading.Thread(target=function_1(), args=(4))
    ## Start thread thd_1.
    thd_1.start()

    ## Create thread to execute function_2() in 5 seconds instead.
    thd_2 = threading.Thread(target=function_2(), args=(5))
    ## Start thread thd_2.
    thd_2.start()

    ## Create thread to execute function_3().
    thd_3 = threading.Thread(target=function_1(), args=())
    ## Start thread thd_3.
    thd_3.start()

    ## Execute function, that shows how many threads are running.
    ## (executed with Main Thread)
    show_active_threads()


## Python3 program start execution.
if __name__ == "__main__":
    main()
