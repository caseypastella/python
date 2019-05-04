def find33(list1):
    
    for num in range(0,len(list1) -1): 
        if list1[num] == 3 and list1[num +1] == 3: 
            return True
        else:
            return False
    
find33([1,3,3])



    