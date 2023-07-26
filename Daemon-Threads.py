import threading
import time
num=0
def daemon_func():
    global num
    while(True):
        num+=1
        time.sleep(1)
def non_daemon_func():
    global num
    for i in range(20):
        print(num)
        time.sleep(1)

daemon_thread=threading.Thread(target=daemon_func,daemon=True)
non_daemon_thread=threading.Thread(target=non_daemon_func)
non_daemon_thread.start()
daemon_thread.start()

# Wait for thread1 to complete
non_daemon_thread.join()
print("Non-Daemonic Thread has completed.")