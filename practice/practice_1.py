#function that draws a*a grid

def repeat(p,q):
    for num in range(0,q):
            print(p,end='')
    print(p)

x = ' - - - - +'
y = '         |'

def row(m):
    for num in range(0,4):
        print('|',end='')
        repeat(y,m-1)
    print('+',end='')
    repeat(x,m-1)



def grid(n):
    print('+',end='')
    repeat(x,n-1)
    for num in range(0,n):
        row(n)

grid(4)