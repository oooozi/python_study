def signin():
    trial = 0
    a = input("회원가입 or 로그인 ")
    if a == "회원가입":
        id = input("ID를 입력하세요 ")
        pw = input("password를 입력하세요 ")
        while True:
            pw2 = input("password를 다시 한번 입력하세요 ")
            if pw != pw2:
                pw2 = input("password가 일치하지 않습니다. 다시 한번 입력하세요 ")
                break
            else:
                break
        print("회원가입 되었습니다")
    else:
        id = input("ID를 입력하세요 ")
        while True:
            if id == "user123":
                if trial == 3:
                    print("계정이 잠금되었습니다")
                    break
                else:
                    pw = input("password를 입력하세요 ")
                    while True:
                        trial += 1
                        if trial == 3:
                            break
                        elif pw != "123456":
                            pw = input("password가 일치하지 않습니다. 다시 한번 입력하세요 ")
                            continue
                        else:
                            print("회원가입 되었습니다")
            else:
                id = input("존재하지 않는 ID입니다. ID를 다시 입력하세요 ")
                continue

signin()
signin()