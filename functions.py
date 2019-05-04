def name_function(
    name = 'NAME'
):
    '''
    DOCSTRING: INFORMATION ABOUT FUNCTION
    Input: none
    Output: hello
   '''
#*args
def func(*args): 
    #Returns 5% op the sum of a and b
    for item in args:
        print(item)
 
func(50,60,50)
 


#**kwargs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit'])) 
    else: 
        print('I did not find and fruit')
myfunc(fruit = 'apple', veggie = 'lettuce')

#Both
def myfunc1(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format((args[0]),kwargs['food']))
    
myfunc1(10,20,30, fruit = 'apple', food = 'eggs', animals = 'dog') 

        