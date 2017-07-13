import sys
import os
import time
import random
from multiprocessing import Process, Pool

sys.exit(0)


def run_process(name):
    print('run child {}({})'.format(name, os.getpid()))


print('parent process is {}'.format(os.getpid()))
p = Process(target=run_process, args=('test',))
print('child process will start.')
p.start()
print('child is processing.')
p.join()
print('child is end')

print('process start at {}'.format(os.getpid()))  # process start at 5483

pid = os.fork()

if pid == 0:
    print('I am child process {}, and parent process is {}'.format(
        os.getpid(), os.getppid()))
    # I am child process 5484, and parent process is 5483
else:
    print('I {} just create process {}'.format(os.getpid(), pid))
    # I 5483 just create process 5484
