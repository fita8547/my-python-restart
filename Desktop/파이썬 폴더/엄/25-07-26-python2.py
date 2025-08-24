#--------------
#입력
#사용자로부터 문자열 형태의 입력을 받는 함수
#콘솔키반의 프로그램을 만들떄,
#사용자와 상호작용할 수 있게 해주는 대표적인 함수
#input() 안의 문자열은 프롬프트(prompt)
#-> 사용자에게 보여주는 질문이나 지시문
#사용자가 키보드로 입력한 값은 무조건 문자열 (string)으로 반환됨
#아무것도 입력하지 않고 엔터를 치면 빈 문자열 반활("")
#정수나 실수로 사용하려면 형변환이 필요하다.


#그냥쓰기
# input("숫자를 입력하세요 :")#문자열
#변수에 대입가능
# str1=input()
# #입력된 값을 출력
# print(f'입력된 값: {str1}')
#바로 사용가능 
# print("입력한 내용 : "+ input())

#출력 문구 지정가능
# print("문자열을 입력하세요 : ",end="")
# str1=input()
# print("입력된 문자열 :",str1)
# str1 = input("이름을 입력하세요 : ")
# print(" 작성한 이름 : ",str1)

# #입력된 문자열을 숫자로 다루겠다.
# s=input("입력")
# print("변수s의자료 :",s)
# print("변수s의자료형 :",type(s))
# print("변수s의자료(int함수 이용) :",int(s))
# print("변수s의자료 (int함수이용):",type(int(s)))

# num = input("숫자 입력하세요 :")#입력된 숫자는 문자열 형태
# num = int(num) #자료형을 정수형으로 변환
# # print(num+10)

# num = int(input("숫자를 입력해주세요 : "))
# print(f'입력한 숫자는 {num}입니다')

#여러개의 값을 한번에 입력받고 숫자로 다루기
# num1 = int(input("첫번쨰 숫자: "))
# num2 = int(input("두번쨰 숫자: "))
# print(F'두수의 합계: {num1+num2}')

#여러개의 수 입력받기
# split():문자열을 나누어서 리스트로 반환(공백,개행)

#변수1,변수2 = input().split()

#예제
# a,b=input("문자열 두개 입력하세요 : ").split()#공백을 기준으로 분리
# print(a)
# print(b)


# a,b=input("문자열 두개 입력하세요 : ").split(".")#콤마를 기준으로 분리
# print(a)
# print(b)




#map 함수이용해서 한번에[ 값을 여러개 입력받기
#map(함수,반복가는항 객체)
# <작성형식>
# 변수1,변수2=map(int,input().split())



# a,b=map(int,input("숫자 두개를 입력하세요").split())
# print(f"두 수를 더한 값은 : {a+b}")


#실수 하나 입력받기
# num =float(input("실수 하나 입력하세요 : "))
# print(f"입력한 실수는 : ",num)

# #실수 여러개 입력받기
# a,b=map(float,input().split())
# print(f'두수를 더한 값 ', a+b)
#정리
#1)문자열만 입력 받을떄
str1=input("문자열입력 : ")

#2) 정수하나만 입력 받을때
num1=int(input("숫자 입력: "))

#3 실수하나만 입력받았을떄
num2=float(input("숫자 입력 : "))

#4여러개의 숫자 입력받을 때
num1,num2.num3,num4 =map(int,input("4개의 정수 입력").split())
#입력한 4개의 숫자가 split()함수에 의해서 공백으로 구분됨.
#map()함수에 의 해서 int(정수)형태로 변환됨
#각각의 4개의 수자는 num1~num4까지 정수 입력