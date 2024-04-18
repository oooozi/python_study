def prime(a,b):

    sum_prime = 0
    
    for x in range(a, b+1):
        isprime=True
        for m in range(2, x):
            if x % m == 0:
                isprime=False
                break
        if isprime:
            sum_prime+=x

        
    print(sum_prime)

prime(10,100)
