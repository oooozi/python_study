
import math

    
def triangle():
    a = int(input("a각을 입력하세요 : "))
    b = int(input("b각을 입력하세요 : "))
    c = int(input("c각을 입력하세요 : "))

    x = a / 180 * math.pi
    y = b / 180 * math.pi
    z = c / 180 * math.pi

    p = math.sin(x) + math.sin(y) + math.sin(z)
    
    if a+b+c==180:
        print("sin(a)+sin(b)+sin(c) = ",p)

    else:
        print("삼각형의 세 각의 합이 180도가 아닙니다")

triangle()
