def square(num):
    return num**2 
nums = [1,2,3,4,5]

for item in map(square,nums):
    print (item)
    

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    
names =['casey', 'tom', 'bebe']

list(map(splicer,names)) 