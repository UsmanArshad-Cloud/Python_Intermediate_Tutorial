import threading
import time

def Racer(event,racer_no):
    print(f"Racer {racer_no} is waiting for the race to start")
    event.wait()
    print(f"Runner {racer_no} started racing")
event=threading.Event()
threads=[threading.Thread(target=Racer,args=(event,i)).start() for i in range(3)]
print("Race is about to start")
time.sleep(3)
event.set()
print("Race Started")
print("Race Fininshed")