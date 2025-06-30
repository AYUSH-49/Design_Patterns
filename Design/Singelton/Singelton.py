from multiprocessing.spawn import _main
"""import threading

class Singelton:
    __instance = None
    __lock=threading.Lock()

    def __new__(cls):
        if cls.__instance==None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)
            
        return cls.__instance
    
if __name__=="__main__":
    s1 = Singelton()
    print(s1)
    s2= Singelton()
    print(s2)
    print(s1 is s2)
    
"""
import threading

class Singleton:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)
        return cls.__instance

def create_singleton_instance(thread_id):
    singleton = Singleton()
    print(f"Thread {thread_id}: {singleton}")

if __name__ == "__main__":
    num_threads = 5
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=create_singleton_instance, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nFinal check:")
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)
    print(s1 is s2)