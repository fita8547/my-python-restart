'''
#숙제------------------------------------------------------------------------------------------------
#문제------------------------------------------------------------------------------------------------
반복문을 사용하여 사용자가 입력한 비밀번호가 대소문자+특수문자+숫자를 포함한 6자리 이상 비밀번호인지 판단하는 프로그램을 작성하시오.
만약
문자를 포함하지 않았다면 '대소문자를 포함한 비밀번호를 설정하세요.'
숫자를 입력하지 않았다면 '숫자를 포함한 비밀번호를 설정하세요', 
특수문자를 포함하지 않았다면 '특수문자를 포함한 비밀번호를 설정하세요' 라고 출력.
조건에 맞게 비밀번호를 설정하면 '안전한 비밀번호입니다.' 출력.'''


while True:
    pwd = input("비밀번호를 입력하세요: ")
    int_count = 0
    pwd_count = 0
    upper_count = 0
    lower_count = 0

    for ch in pwd:
        if ch.isdigit():
            int_count += 1
        elif ch in "!@#$%^&&*()":
            pwd_count += 1
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1

    if len(pwd) < 6:
        print("6자리 이상이셔야합니다.")
        continue
    elif upper_count == 0 or lower_count == 0:
        print("대소문자를 포함한 비밀번호를 설정하세요.")
        continue
    elif int_count == 0:
        print("숫자를 포함한 비밀번호를 설정하세요")
        continue
    elif pwd_count == 0:
        print("특수문자를 포함한 비밀번호를 설정하세요")
        continue
    else:
        break

# 모든 조건을 만족했다면 반복 종료
print("안전한 비밀번호입니다.")

