#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
          
while True:
    snum = input('Enter a number: ')
    if snum.lower() == 'done':
         break
    try:
        int_num = int(snum)
    except ValueError:
        print('Invalid input')
        continue
    if smallest is None or int_num < smallest:
            smallest = int_num
    if largest is None or int_num > largest:
            largest = int_num
    
if largest is not None and smallest is not None:
    print('Maximum is', largest)
    print('Minimum is ', smallest)