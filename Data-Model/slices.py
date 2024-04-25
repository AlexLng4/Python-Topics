#some examples of slices
#first is from where you want to start, second where you stop and third is the step
#important!!! 
# in expresion seq[start, stop, step], python calls the seq.__getitem__(slice(start, stop, step))

l = [10, 20, 30, 40, 50, 60]

l[:2] #first 2 elements
l[2:] #all elements begin with the second
l[2:3] # the third element
l[2:2] # nothing
l[2:4] # third and fourth

# example with the third
s = 'bicycle' 
s[::3] #output: bye, step=3
s[::-1] # reverse output
s[::-2] # reverse with step=2
print("Stop")