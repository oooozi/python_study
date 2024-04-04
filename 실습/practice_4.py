n = int(input('Enter a positive integer: '))

def factorial(x=n, m=1):
    if x <= 0:
        print('Factorial of', n, 'is', m)
    else:
        m *= x
        factorial(x=x-1, m=m)


factorial(x=n, m=1)
        
