#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################
## Demo example how to use sockets in Python3.

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
- https://www.youtube.com/watch?v=fKl2JW_qrso
'''
