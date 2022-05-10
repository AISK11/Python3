#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################
## Demo example how to use multiprocessing in Python3.


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
- https://www.youtube.com/watch?v=fKl2JW_qrso
'''


################################################################################
##                                  Modules                                   ##
################################################################################
## Docs: https://docs.python.org/3/library/time.html
import time
## Docs: https://docs.python.org/3/library/multiprocessing.html
import multiprocessing


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


## Program starting function.
def main():
    ## Start time of the program.
    program_start = time.perf_counter()

    ## Create process to execute function_1() in 7 seconds instead.
    p1 = multiprocessing.Process(target=function_1, args=(7,))
    ## Create process to execute function_2() in 5 seconds instead.
    p2 = multiprocessing.Process(target=function_2, args=(5,))
    ## Create process to execute function_3().
    p3 = multiprocessing.Process(target=function_3, args=())

    processes = [p1, p2, p3]

    ## Start processes.
    p1.start()
    p2.start()
    p3.start()

    ## Show PIDs of processes.
    i = 0
    while i < len(processes):
        print(f"Process {i+1}: {processes[i]}")
        i += 1

    ## Wait until each process finished execution.
    p1.join()
    p2.join()
    p3.join()

    ## Show PIDs of processes.
    i = 0
    while i < len(processes):
        print(f"Process {i+1}: {processes[i]}")
        i += 1

    ## Show how many seconds the program took to execute.
    program_finish = time.perf_counter()
    print(f"Program finished in {round(program_finish-program_start, 2)} second(s).")


## Python3 program start execution.
if __name__ == "__main__":
    main()
