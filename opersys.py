# from multiprocessing import Process
# from multiprocessing import Pipe

# def child(conn):
#     conn.send("Hello Parent")
#     print("Child received:", conn.recv())
#     conn.close()

# def parent(conn):
#     print("Parent received:", conn.recv())
#     conn.send("Hello from parent!")
#     print("Parent sent: Hello from parent!")

# if __name__ == "__main__":
#     p_conn, c_conn = Pipe()

#     p = Process(target=child, args=(c_conn,))
#     p.start()

#     parent(p_conn)
#     p.join()

# from multiprocessing import Process 
# from multiprocessing import Queue

# def child(q, msg):
#     q.put(msg)
# def parent(q):
#     msg1 = q.get()
#     msg2 = q.get()
#     msg3 = q.get()


#     print("Parent recived:", msg1)

#     print("Parent received:", msg2)
#     print("Parent receved:", msg3)


# if __name__ == "__main__":
#     q = Queue()

#     p1 = Process(target=child, args=(q, "Msg 1"))
#     p2 = Process(target=child, args=(q, "Msge 2"))
#     p3 = Process(target=child, args=(q, "Msg 3"))



#     p1.start()
#     p2.start()
#     p3.start()

#     parent(q)
#     p1.join()
#     p2.join()
#     p3.join()

# from multiprocessing import Process
# from multiprocessing import Queue


# def producer(q):
#     items = ["itm 1", "itm 2", "itm 3", "itm 4", "itm 5"]

#     for i in items:
#         q.put(i)

#     q.put("stop")



# def consumer(q):
#     while True:
#         msg = q.get()

#         if msg == "stop":
#             break

#         print("Consumr recived:", msg)

# if __name__ == "__main__":
#     q = Queue()

#     p1 = Process(target=producer, args=(q,))
#     p1.start()

#     consumer(q)

#     p1.join()




# import threading

# counter = 0

# def increment():
#     global counter
#     for _ in range(100000):
#         counter += 1



# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)
# t3 = threading.Thread(target=increment)
# t4 = threading.Thread(target=increment)
# t5 = threading.Thread(target=increment)

# t1.start()

# t2.start()
# t3.start()
# t4.start()
# t5.start()



# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

# print("Finl countr value: ", counter)


# import threading

# counter = 0

# def increment():
#     global counter
#     for _ in range(1000000):
#         counter += 1

# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)
# t3 = threading.Thread(target=increment)
# t4 = threading.Thread(target=increment)
# t5 = threading.Thread(target=increment)

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()


# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()


# print("Final counter value:", counter)





# import threading
# import time

# counter = 0
# lock = threading.Lock()

# def increment():
#     global counter
#     for _ in range(100000):
#         lock.acquire()
#         counter += 1
#         lock.release()

# start_time = time.time()            

# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)
# t3 = threading.Thread(target=increment)
# t4 = threading.Thread(target=increment)
# t5 = threading.Thread(target=increment)

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

# end_time = time.time()

# print("Final counter value without Lock:", counter)
# print("Execution time with Lock:", end_time - start_time)



from multiprocessing import Process, Value, Lock, Semaphore

def increment(shared_counter, shared_counter2, lock, sem):
    for _ in range(100000):

        lock.acquire()
        shared_counter.value += 1
        lock.release()

        sem.acquire()
        shared_counter2.value += 1
        sem.release()

if __name__ == "__main__":
    counter = Value('i', 0)
    counter2 = Value('i', 0)

    lock = Lock()
    semaphore = Semaphore(1)

    p1 = Process(target=increment, args=(counter, counter2, lock, semaphore))
    p2 = Process(target=increment, args=(counter, counter2, lock, semaphore))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final counter value with Lock:", counter.value)
    print("Final counter value with Semaphore:", counter2.value)
