import threading


class Singelton:
    __instance = None
    __lock = threading.Lock()

    def get_instance(self):
        if  Singelton.__instance== None:
            with Singelton.__lock:
                if Singelton.__instance is None:
                    Singelton.__instance =Singelton()
        return Singelton.__instance

if __name__ == '__main__':
    s1=Singelton()
    print(s1)
    s2=Singelton()
    print(s2)
    print(s1 is s2)