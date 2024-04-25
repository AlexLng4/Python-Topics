import collections

class Vector():

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __add__(self, other_vector):
        x_new = self.x + other_vector.x
        y_new = self.y + other_vector.y
        
        return Vector(x_new, y_new)
    
    def __mul__(self, other_vector):
        return Vector(self.x * other_vector.x, self.y *other_vector.y)
    
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

print("Stop")