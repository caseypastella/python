#Functions Homework

def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)

def rancheck(num,low,high):
    if num in range(low,high):
        print(f' {num} is in the range')
    else: 
        print(f' {num} is not in the range')
        

def up_low(mystring):
    countlower = 0 
    countupper = 0
    for letter in mystring:
        if letter.isupper():
            countupper+= 1
            return countupper
        elif letter.islower():
            countlower+= 1
            return countlower
        else:
            pass
        
def palindrome(mystring):
    if mystring == mystring[::-1]: 
        return True
    else:
        return False
        
        
        