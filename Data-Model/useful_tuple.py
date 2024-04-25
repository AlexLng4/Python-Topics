# example of a nametuple usage
from collections import namedtuple

City = namedtuple('City', 'name population coordinates')

#data should be passed as positional arguments
Tokyo = City('Tokyo', '999', '80 49' )

print('Stop')