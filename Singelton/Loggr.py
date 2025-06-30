import threading


class FileBasedConfigurationManagerImpl:
    __instance = None
    __lock = threading.Lock()

    #def __init__(self):
      #  super().__init__()

    @staticmethod
    def get_instance( ):
        if FileBasedConfigurationManagerImpl.__instance is None:
            with FileBasedConfigurationManagerImpl.__lock:
                if FileBasedConfigurationManagerImpl.__instance is None:
                    FileBasedConfigurationManagerImpl.__instance = FileBasedConfigurationManagerImpl()

        return FileBasedConfigurationManagerImpl.__instance9i8
    print(s1)
    s2=FileBasedConfigurationManagerImpl()
    print(s2)
