import os
import time
from queue import Queue
from threading import Thread, Lock, RLock, BoundedSemaphore


# def print_time(threadName, counter, delay):
#     while counter:
#         time.sleep(delay)
#         print("{}: {}".format(threadName, time.ctime(time.time())))
#         counter -= 1
#
#
# class MyThread(Thread):
#     def __init__(self, name, delay):
#         super().__init__()
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print("Starting {}".format(self.name))
#         print_time(self.name, 5, self.delay)
#         print("Exiting {}".format(self.name))
#
#
# # Create new threads
# thread1 = MyThread("Thread-1", 2)
# thread2 = MyThread("Thread-2", 2)
# thread3 = MyThread("Thread-3", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
# thread3.start()
#
# print(thread1.is_alive())
# print(thread2.is_alive())
# print(thread3.is_alive())
# thread1.join()
# thread2.join()
# thread3.join()
# print(thread1.is_alive())
# print(thread2.is_alive())
# print(thread3.is_alive())


###################################
# from threading import Thread, Lock
#
# import time
#
#
# class MyThread (Thread):
#     def __init__(self, name, delay):
#         super().__init__()
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print("Starting {}".format(self.name))
#
#         # Get lock to synchronize threads
#
#         threadLock.acquire()
#         print_time(self.name, self.delay, 3)
#
#         # Free lock to release next thread
#         threadLock.release()
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("{}: {}".format(threadName, time.ctime(time.time())))
#         counter -= 1
#
#
# threadLock = BoundedSemaphore(5)
# threads = []
#
# # Create new threads
# thread1 = MyThread("Thread-1", 2)
# thread2 = MyThread("Thread-2", 2)
# thread3 = MyThread("Thread-3", 2)
# thread4 = MyThread("Thread-4", 2)
# thread5 = MyThread("Thread-5", 2)
# thread6 = MyThread("Thread-6", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
#
# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)
# threads.append(thread3)
# threads.append(thread4)
# threads.append(thread5)
# threads.append(thread6)
# # Wait for all threads to complete
# for t in threads:
#     t.join()
# print("CODE AFTER THREADS DONE")


#######################################
# from queue import Queue
# from threading import Lock, Thread
#
# import time
#
# exitFlag = 0
#
#
# class MyThread (Thread):
#     def __init__(self, name, q):
#         super().__init__()
#         self.name = name
#         self.q = q
#
#     def run(self):
#         print("Starting {}".format(self.name))
#         process_data(self.name, self.q)
#         print("Exiting {}".format(self.name))
#
#
# def process_data(thread_name, q):
#     while not exitFlag:
#         queueLock.acquire()
#         print("Waiting")
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print("{} processing {}".format(thread_name, data))
#         else:
#             queueLock.release()
#         time.sleep(3)
#
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = Lock()
# workQueue = Queue(10)
# threads = []
#
# # Create new threads
# for thread_name in threadList:
#     thread = MyThread(thread_name, workQueue)
#     thread.start()
#     threads.append(thread)
#
# # Fill the queue
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
#
# # Notify threads it's time to exit
# # exitFlag = 1
#
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
#
# # Wait for all threads to complete
# for t in threads:
#     t.join()
# print("CODE AFTER THREADS DONE")


##############################################
##############################################
from queue import Queue
from threading import Thread

# import os
# import requests
# import time
#
#
# def get_request(url):
#     resp = requests.get(url)
#     print(os.getpid())
#
#
# def main():
#     ts = time.time()
#     urls = ["https://httpbin.org/get"] * 10
#     for url in urls:
#         get_request(url)
#     print('Took {} seconds'.format(time.time() - ts))

# main()

##################### QUEUE


# class DownloadWorker(Thread):
#
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#
#     def run(self):
#         while True:
#             # Get the work from the queue and expand the tuple
#             url = self.queue.get()
#             try:
#                 get_request(url)
#             finally:
#                 self.queue.task_done()
#
#
# def main():
#     ts = time.time()
#     urls = ["https://httpbin.org/get"] * 10
#     # Create a queue to communicate with the worker threads
#     queue = Queue()
#     # Create 10 worker threads
#     for x in range(10):
#         worker = DownloadWorker(queue)
#         # Setting daemon to True will let the main thread exit even though the workers are blocking
#         worker.daemon = True
#         worker.start()
#     # Put the tasks into the queue
#     for url in urls:
#         print('Queueing {}'.format(url))
#         queue.put(url)
#     # Causes the main thread to wait for the queue to finish processing all the tasks
#     queue.join()
#     print('Took {}'.format(time.time() - ts))
#
# main()
#
# #####################PROCESS
#
#
#
# from multiprocessing.pool import Pool
#
#
# if __name__ == '__main__':
#     ts = time.time()
#     urls = ["https://httpbin.org/get"] * 10
#
#     with Pool() as pool:
#         pool.map(get_request, urls)
#
#     print('Took {} seconds'.format(time.time() - ts))

##########################

# import gevent
#
#
# def foo():
#     print('Running in foo')
#     gevent.sleep(5)
#     print('Explicit context switch to foo again')
#
#
# def bar():
#     print('Explicit context to bar')
#     gevent.sleep(0)
#     print('Implicit context switch back to bar')
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

#############################

# Sharing status between process
# Shared memory
#
# Data can be stored in a shared memory map using Value or Array. For example, the following code


# from multiprocessing import Process, Value, Array
#
#
# def my_func(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
#
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#
#     p = Process(target=my_func, args=(num, arr))
#     p.start()
#     p.join()
#
#     print(num.value)
#     print(arr[:])


# import gevent
# from gevent.queue import Queue
# #
# tasks = Queue()
#
#
# def worker(n):
#     while not tasks.empty():
#         task = tasks.get()
#         print('Рабочий {} получил задание {}'.format(n, task))
#         gevent.sleep(0)
#
#     print('Пора заканчивать!')
#
#
# def boss():
#     for i in range(1, 25):
#         tasks.put_nowait(i)
#
#
# gevent.spawn(boss).join()
#
# gevent.joinall([
#     gevent.spawn(worker, 'steve'),
#     gevent.spawn(worker, 'john'),
#     gevent.spawn(worker, 'nancy'),
# ])
# #
#

# import threading
#
# class SharedCounter:
#     '''
#     Объёкт счётчика, который может быть общим (shared) для нескольких потоков.
#     '''
#     def __init__(self, initial_value = 0):
#         self._value = initial_value
#         self._value_lock = threading.Lock()
#
#     def incr(self,delta=1):
#         '''
#         Инкрементирует счётчик с блокировкой.
#         '''
#         with self._value_lock:
#             self._value += delta
#
#     def decr(self,delta=1):
#         '''
#         Декрементирует счётчик с блокировкой.
#         '''
#         with self._value_lock:
#             self._value -= delta
# import requests
#
#
# def get_request(url):
#     resp = requests.get(url)
#     print(os.getpid())
#
#
# def main():
#     ts = time.time()
#     urls = ["https://httpbin.org/get"] * 10
#     for url in urls:
#         get_request(url)
#     print('Took {} seconds'.format(time.time() - ts))
#
# main()
# #
# # Create new threads
# thread1 = Thread(target=main)
# thread2 = Thread(target=main)
#
# # Start new Threads
# thread1.start()
# thread2.start()
#
# # print(thread1.is_alive())
# # print(thread2.is_alive())
# thread1.join()
# thread2.join()
# # print(thread1.is_alive())
# # print(thread2.is_alive())
