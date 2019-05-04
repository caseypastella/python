#Statements Test

#Use for, .split(), and if to create a statement that will print
#out words that start with s 
st = 'print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)
        

        
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = [num for num in range(1, 51) if num%3 == 0]
print(mylist)

#Go through the string below and if the length of a word is even print "even!"
st1 = 'print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print(word)

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1,101):
    if num%3 == 0 and num%5 ==0:
        print(f'{num} FizzBuzz')
    elif num%3 == 0:
        print(f'{num} Fizz')
    elif num%5 == 0:
        print(f'{num} Buzz')
    else: 
        print(num)
#Use List Comprehension to create a list of the first letters of every word in the string below:
st2 = 'Create a list of the first letters of every word in this string'

print([word[0] for word in st2.split()])