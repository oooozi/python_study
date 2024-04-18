#1번

def login():
    trial = 0
    while True:
        trial += 1
        pw = input("비밀번호를 입력하시오: ")
        if trial == 3 and pw != "ENG11080502":
            print("오류! 비밀번호가 틀렸습니다.")
            print("최대 횟수를 초과하여 계정이 잠금되었습니다.")
            break
        elif pw == "ENG11080502":
            print("접근이 허가되었습니다.")
            break
        else:
            print("오류! 비밀번호가 틀렸습니다.")
            continue

login()


#2번

import random


def randomnumber():
    trial = 0
    x = random.randint(1,100)
    print("랜덤 숫자가 지정되었습니다.")
    while True:
        trial += 1
        y = int(input("예상되는 숫자를 입력하세요.(1~100) :"))
        if trial ==  5 and y != x:
            if y > x:
                print("그 숫자보다는 낮습니다.")
            else:
                print("그 숫자보다는 높습니다.")
            print("최대 허용 횟수를 초과하셨습니다. 답은 {}입니다.".format(x))
            break
        elif y > x:
            print("그 숫자보다는 낮습니다.")
            continue
        elif y < x:
            print("그 숫자보다는 높습니다.")
            continue
        elif y == x:
            print("숫자를 맞추셨습니다. 답은 {}입니다." .format(x))
            break


randomnumber()
            
        
    
        
    
