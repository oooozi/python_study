def prime_list(a,b):

    prime_list =  []
    
    for x in range(b, a-1, -1):
        isprime=True
        for m in range(2, x):
            if x % m == 0:
                isprime=False
                break
        if isprime:
            prime_list.append(x)
    
    print(prime_list)

prime_list(10,100)
