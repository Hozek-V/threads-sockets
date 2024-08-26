import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Vlákno {threading.current_thread().name}: {i}")


def sum_numbers():
    result = 0
    for i in range(5):
        time.sleep(1)
        result += i
        print(f"Vlákno {threading.current_thread().name}: {result}")


thread1 = threading.Thread(target=print_numbers, name="Vlákno 1")
thread2 = threading.Thread(target=sum_numbers, name="Vlákno 2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Hlavní vlákno skončilo.")
