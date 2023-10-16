#functions.py

def numbers(number1, number2= 3.14, verbose = False):
  '''Takes two numbers and adds them, if number2 is not given it will make it 3.14. Also if verbose is chosen to be true than it will give
  you the parameters as well'''

  number1 = int(number1)
  number2 = (number2)

  if number2 == 3.14:
    number2 = float(number2)

  sum = round(number1 + number2,2)

  sum_message = f"The sum is {sum}\n"


  if verbose:
    print(f'Parameters:\n\t-number1: {number1}\n\t-number2: {number2}\n\t-verbose: {verbose}')
    sum = round(sum,2)
    return sum_message

  else:
    return sum_message



