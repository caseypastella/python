st = 'print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)

mylist = [num for num in range(1, 51) if num%3 == 0]
print(mylist)

st1 = 'print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print(word)

for num in range(1,101):
    if num%3 == 0 and num%5 ==0:
        print('Fizzbuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else: 
        print(num)

st2 = 'Create a list of the first letters of every word in this string'

print([word[0] for word in st2.split()])