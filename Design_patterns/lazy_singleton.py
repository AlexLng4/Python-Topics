#sometimes by accedent we create an object by import
#lazy singleton ensure us that, we create when needed

class LazySingleton:

    __instance = None
    def __init__(self):
        if not LazySingleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance

s = LazySingleton()
print("Object created", LazySingleton.getInstance())
s1 = LazySingleton()