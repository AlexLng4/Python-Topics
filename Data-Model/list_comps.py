#important!! Any operation that appears to modify these objects actually creates a new object with the modified value

symbols = '$#%*&!'
elemnts_splited_1 = []

for symbol in symbols:
    elemnts_splited_1.append(ord(symbol))

#comprehensions and readability
elemnts_splited_2 = [ord(symbol) for symbol in symbols]

#comprehensions with condition
elemnts_splited_3 = [ord(symbol) for symbol in symbols if ord(symbol)>35]

# tuple unpacking expample
coordinates = (33.2, -11.234)
x_coordinate, y_coordinate = coordinates

# using * to grab excess items
a,b, *rest = [1, 2, 3, 4, 5]
#rest will store a list with the excess variables [4, 5]
#always, when unpacking, we need to have the correct number (never less or more) 
#but with *, we can have more arguments
#if you have a different order but with less numebers, it will work the same 
a, *rest, b = [1, 2] 
*rest, a, b = [1, 2] 
#if you have different oreder but more arguments, the order will be applied
a, *rest, b = [1, 2, 3 ,4, 5] # order applide

#nested tuple unpacking
meteo = [
    ('Tokyo', 'JP',(35, 139)),
    ('Mexico', 'IN', (28, 77)),
    ('Sao Paulo', 'BR', (19, -23)),
]
for name, cc,(lat, long) in meteo:
    print(name, cc, lat, long)

# create a list with * operand
[1,2,3]*5
# create a list of lists
list = [['_','_',"_"] for _ in range(3)]
list_with_operand = [['_']*3 for _ in range(3)]

# create a list of lists but with the same reference
# !! difference is that you are refeenring to the same object or a different object
list_same_ref = ['_' *3] *3

# other example for the same object
lists_new_way=[]
row = ['_'] *3
for _ in range(3):
    lists_new_way.append(row)

# for a different object
for _ in range(3):
    row_new = ['_']*3
    lists_new_way.append(row_new)


# an example of an operand on a mutable sequence and a immutable one:
# for mutable elements, the reference will be the same
# for immutable, a new object will be created
list = [1,2,3]
val_1 = id(list)
list *= 2
val_2 = id(list)
if val_1 == val_2:
    print("mutable element")

tuple = (1,2,3)
val_1 = id(tuple)
tuple *= 2
val_2 = id(tuple)
if val_1 != val_2:
    print("immutable element")

#curiosity
raw=["2"]
list_test = []
for _ in range(3):
    list_test.append(raw)
print(list_test)
list_test[0] = ["0"]
print(list_test)


print("stop")
