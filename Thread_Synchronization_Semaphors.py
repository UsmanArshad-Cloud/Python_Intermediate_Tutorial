import threading
import time

semaphors=threading.Semaphore(3)

def Print_Document(number):
    with semaphors:
        print(f"Printing the Document {number}")
        time.sleep(2)
        print(f"Document {number} Printed")

for thread_number in range(1,6):
    t=threading.Thread(target=Print_Document,args=(thread_number,))
    t.start()


