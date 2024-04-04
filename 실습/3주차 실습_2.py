import math

p = math.pi
float(p)

a = input("a각을 입력하세요 : ")
b = input("b각을 입력하세요 : ")
c = input("c각을 입력하세요 : ")

float(a)
float(b)
float(c)


x = a / 180 * p
y = b / 180 * p
z = c / 180 * p

q = math.sin(x) + math.sin(y) + math.sin(z)

if a+b+c==180:
    print("sin(a)+sin(b)+sin(c) = ", q)

else:
    print("삼각형의 세 각의 합이 180도가 아닙니다")
