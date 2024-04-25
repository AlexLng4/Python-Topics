# have the same state and the changes are apply on both
#have the same behav but diff objects

class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass
b = Borg()
b1 = Borg()
b1.x = 4
print("Stop")