#Challenge problems

def spygame(intlist):
    
    code = [0,0,7,"x"]
    for num in intlist:
        if num == code[0]:
            code.pop(0)
        
    return len(code) == 1

spygame([1,0,3,2,0,7])


#countprimes

def count_primes(num):
    if num == 0 or num == 1:
        return 0 

    primes = [2] 
    x = 3 
    while x <= num:
        for y in primes: 
            if x%y == 0:
                x+= 2
                break 
            
        else: 
            primes.append(x)
            x+=2
    print(primes)
    return len(primes)

count_primes(100)


            
    

    