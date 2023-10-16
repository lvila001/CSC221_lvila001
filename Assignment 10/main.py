import functions

if __name__ == '__main__': 
    '''This function will test all posiibilities for functions.py'''
    print(f'Functions.py test: \n')
    
    print('Both numbers are ints and Verbose was chosen to be true')
    print(functions.numbers(3,2,True))

    print('\nNumber 1 is provided. number2 and verbose are not')
    print(functions.numbers(6))

    print('\nOnly number 1 and verbose=True are provided.')
    print(functions.numbers(1,verbose=True))

help(functions)