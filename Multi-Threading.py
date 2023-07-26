import threading
def func():
    for i in range(30):
        print("Task1")
def func2():
    for i in range(30):
        print("Task2")
thread1=threading.Thread(target=func)
thread2=threading.Thread(target=func2)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Program Ended")