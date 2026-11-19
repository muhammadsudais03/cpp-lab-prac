
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        counter += 1
            

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t3 = threading.Thread(target=increment)
t4 = threading.Thread(target=increment)
t5 = threading.Thread(target=increment)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("name hisham reg 25388")
print("Final counter value without Lock:", counter)
