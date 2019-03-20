#! /usr/bin/python3

import time

input('Press enter to start the timer.')
startTime = time.time()
input('Press enter again to stop the timer.')
endTime = time.time()
print('Time:', (endTime - startTime), 'seconds.')
