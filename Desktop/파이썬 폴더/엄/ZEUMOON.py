#제어문(조건문,반복문)
#>코드를 상황에 따라 제어한다.(프로그램 흐름 제어)

'''
1.조건문(if문)
어떤 조건이 참(True)일떄만 특정 코드를 실행
아니면 다른 코드를 실행
<형식>
if 조건문 :
    실행할 코드

    if문 : 만약에
        만약 조건이 만족 하면 수행해라
        조건 만족 =True
        조건에 만족하지 않는다 =Fause

    1.조건문
        참이나 거짓이 있어야 한다. 결과가  T/F
        조건문 씉에는 콜론(:)을 붙인다.
        콜론이 있으면 조건문이 끝
        콜론 뒤부터는 수행문 (실행항 문장)으로 간주한다.
    2.실행할 코드
        조건식이 만족할떄 수행하는 코드들
        반드시 '들여쓰기'를 해야한다
        ->공백3개, 공백 4대 Tab으로 들여쓰기
        수행문으로 코드간의 들여쓰기가 맞지 않으면 오류 발생,
        들여쓰기가 맞으면 수행물을 여러줄 작성할 수 있고,
        들여쓰기가 끝나면 if문의 수행문이 끝난것
        '''
'''
a=99
if a< 100:
    print('100보다 작준요~')
if 3>0:
    print(3>0)
print()
'''
'''
num= int(input("정수를 입력하세요: "))
if num>0:
    print("양수 입니다.")
if num<0:
    print("음수입니다.")
if num==0:
    print("0입니다.")
'''
#if ~ else문
'''
else구문 : if 조건문 뒤에 사용하며, if조건문의 조건이 거짓일떄
        실행되는 부분
<형식>
if <조건문>:
    실행할 코드
else:
    실행할 코드
'''
'''
a=200
if a<100:
    print("100보다 작군요!")#실행할 문장
else:
    print("100보다 크거나 같군요!")#실행할 문장
    '''
'''
num = int(input('정수를 입력하세요 : '))
if num%2 == 0:#조건이 참일떄
    print('짝수 입니다.')
else: #조건이 거짓일떄
    print("홀수 입니다.")
    '''
#예제
#값을 사용자에게 입력받아 in연산자를 활용해서
#짝수 , 홀수 판별하기
'''
num = input("정수를 입력하세요")
a=num[-1]#맨 끝 문자(숫자)를 변수 a에 담는다.

if a in '02468':#a만약에 맨끝 문자가 02468안에 있는 문자라면
    print("짝수입니다.")
else:
    print('홀수입니다.')
    '''
#if-elif-else
'''
<형식>
if 조건문:
    실행할 코드1
elif  조건문2:
    실행할 코드2
else:
    실행할 코드3



    3.elif 조건식 (else if)그게 아니라 만약에 ~ 조건이라면
    이전 조건이 거짓이고, 이 조건이 참이면 실행
    if 문에 종속됨
    if문 없이 단독사용 불가능
    >조건문의 시작은 반드시 if문으로 시작
    if 조건문의 시작은 반드시 if문으로 시작
    if 조건문과 else 구문 사이에 입력 ,개수 제한 없음.
    여러개 사용 가능.
4.else:
    위 조건이 모두 만족하지 않을떄 무조건 실행됨.
    위 모든 조건이 거짓일떄 실행(조건없음)
    if문에 종속됨
    한가지만 사용할 수 있다.
    '''
'''
score = int(input("정수를 입력하세요 : "))
if score >=90:
    print("A학점입니다.")
elif score>=80:
    print("B학점입니다.")
elif score > 70:
    print("D학점입니다.")
else:
    print("F학점입니다.")
'''

#pass
'''
나중에 구현하고자 할떄 아무것도 작성하지 않고 비워둘 경우 쓴다.
'''
#아무일도 일어나지 않음
'''

score = 59
if score >= 60:
    print("합격")
else:
    pass
'''
#if문 중펍 (다중 if문)
#>if문으ㅏ 수행문 안에 또 다른  if문 (조건)을 작성하는것
'''
score = int(input("정수 입력: "))
if score >= 60 : #60보다 크거나 같으면
    print("합격입니다.")
    if score ==100:
        print("만점입니다.")
    print("축하합니다.")
else:
    print("불합격입니다.")
    '''

#----------------------------
#반복문
#----------------------------
'''
    >같은 코드를 여러번 실행하고 싶을떄 사용
    >특정횟수만큼 반복하거나, 어떤 조건이 참인 동안 계속 반복
    >단, 조건에 만족하지 않을때까지

    1.while문
        >조건식이 참이면 수행문 수행
        <if문과 기본 구조가 동일
        >if문 :조건이 참이면 수행하고 끝
        >while문 : 조건이 참이면 구행하고 다시 조건식을 비교


        [특징]
        반복횟수가 정해지지 않았을떄 유용하다.
        무한루프 주의 필요!!!!


        [기본구조]
        while 조건식:
            수행할 문장1
            수행할문장2

        [while문 수행 순서]
        1. 조건식 판별
        2. 수행문 수행
        3.조건식 판별부터 반복'''
#while문사용
count=0
while count<3:
    print("hello")
    count+=1
print('while문 끝!')


'''
1. 무한반복
    count 값을 수행문에서 증가 시키지 않으면  조건문에서
    비교대상인 count의 값이 계속 동일하기 떄문에
    항상 조건이 만족하여 반복문이 끝나지 않는다.->무한반복
    Ctrl+c강제종료
2.조건 변수
    count와 같이 조건식의 비교에 사용되는 변수를 '조건변수'라고 한다
    조건 변수를 어떻게 다루었는지에 따라 반복횟수다 정해진다.
초기값 (조건변수 생성)
while조건식: #조건 변수 사용
    수행문 (반복해서 수행하고 싶은 코드 +조건 변수의 변화식)
'''
#반복 횟수 지정
'''
count = int(input("반복 횟수 입력 :"))
while count >0:
    print(f'count = {count}')
    count-=1
    '''
#특정 조건 만족
#x를 입력하면 종료
# input_str = 0
# while input_str != "x":
#     input_str=input("x를 입력하면 종료")

#소문자 x와 대문자 x 둘다 종료되게
'''
input_str = ""
while input_str.lower() != "x":
    input_str=input("x를 입력하면 종료")
'''
#1. break문 : 반복문 즉시 종료
#2.continue문 : 이런 반복만 건너 뛰고 다음 반복으로 넘어감
# #break문
# #조건을 내부에서 처리한다면 변수 초기값 없어도 안전하게 실행됨
'''
while True:
    input_str = input('x를 입력하면 종료')
    if input_str == "x":
        break
        '''
#변수 i가 100이 되면 반복문 종료 (0에서 99까지 출력)
'''
i=0
while True:
    print(i,end=' ')
    i+=1
    if i==100:#만약에 i가 100과 같다면
        break#반복문을 빠져나가라
'''
#-----------------
#continue

num = 0
while num <10:#num아 10보단 작을 동안 반복
    num+=1# num1씩증가
    if num%2==0:#num이 짝수 일떄
        continue#반복을 중단하고 조건문으로 넘어감
    print(num)
#break, continue 문은 반복문 안에서만 쓰이며,
#if문이 필요하다
#if문 없는 break= 무조건 반복 종료
#if문 없는 continue =무조건 조건식으로 이동


# while True:
#     str1=input('소문자를 입력하세요 (Q:종료) : ')
#     if str1=='Q':
#         break
#     if str1<'a' or str1 >'z':
#         continue
#     print(str1.upper())

#while문 이용해서 1- 10 까지의 합계 구하기

# while문이용해서 1-10까지의 합계구하기
#1.합계를 누적할 변수
#2.1-10 숫자 증가 시킬 변수 필요
#3.while문에서 10회 반복
#4.1-10까지 숫자들의 합계 필요
#5. 누적된 숫자 출력

# my_sum = 0
# num=1

# while num<11: #num <= 10
#     my_sum=my_sum+num #my_sum+=num
#     num+=1
#     print("1-10까지의 합 : ",my_sum)
# print("1-10까지의 합2: ",my_sum)


#--------------------------------------------------
#for문
'''
시퀀스(리스트, 튜플, 문자열 등)의 요소를 하나씩 꺼내서 사용할떄 사용
요소가 니열된 형태의 값을 첫 요소부터 마지막 요소 까지 변숭테 대입하며
반복한다. 정해진 횟수만큼 반복할떄 주로 사용한다.
range()함수와 자주 함께 사용됨.
[for문 기본구조]
for 변수 in 시퀀스:
    수행할 문장
    수행할 문장
in의 사용:
    if문: 포함되어 있는지 확인하여  True/False
    for 문: 한씩 대입
    '''
#for문 사용 - 범위 지정 반복문
#요소의 갯수다 반복횟수를 나타낸다.

# for  i in [3,2,1]:
#     print("i=",i)


# for i in "대한민국":
#     print("str1")

# print()
# print()
# #리스트나 튜플등 반복 가능한 모든 것에 사용가능
# for ch in ["사과","배","포도"]:
#     print(ch)
# print()
# print()
# print()

# print()
'''
    for문을 사용할떄 일반적인 사용법
    range()함수 사용 : 지정한 범위 만큼의 숫자들을 반환
    range(10): 0~9 (마지막 번호는 생략)
    range(101): 0~100
    range(5,11): 5에서 부터 ~ 10까지 반복
    range(1,101):1~100
    rnage(100,0,-1) 100 ~1, -1씩 감소
    range(1,10,2) 1~9,2씩 증가
                    ->1,3,5,7,9


<형식>
#변수: 간순히 몇번 반복할지 정하는 역할

for i in range(횟수):
    실행할 문장
for 변수 in range(시작값,끝값+1):
    실행할 문장
for 변수 in range(시작값,끝값+1,증가 또는 감소 폭):
    실행할 문장
for _ in range(횟수):
    실행할 문장
#관습적으로 반복할 변수 생략하고 언더비 사용
for i in range(10):
#     print(f"{i}번쨰 문장입니다.)'''
# for i in range(10):# 초기 변수 i의 값은 0
#     print(f"{i}번쨰 문장입니다")
# print()
# print()
# for i in range(10,0,-1):
#     print(f'{i}반쨰 문장입니다.')
# print()
# print()
# for i in reversed(range(10)):
#     print(f"{i}번째 문장을 출력합니다.")
#for문으로 1-10까지의 합 구하기
my_sum = 0
for i in range(1,11):
    my_sum+=i
print("1-10까지의 누적된 합 : ",my_sum)


#예제 1부터 100까지의 수 중에 3과 5의 공배수와 3의 배수 5의 배수 출력하기
# for i in range(1,101):
#     if i %3==0 and i %5 ==0:
#         print(f"{i} : 3과 5의 공배수")
#     elif i%3 ==0:
#         print(f'{i} : 3의 배수')
#     elif i%5 ==0:
#         print(f'{i} : 5의 배수')
#     else:
#         print(f'{i}')
# count = int(input("반복할 횟수를 입력하세요 : "))
# for  i in range(count):
#     print(f'{i}번쨰 문장입니다/')

#구구단 만들기
# for i in range(1,10,1):
#     print(f'2 x {i} = {2*i}')

# num = int(input("원하는 단을 입력하세요 : "))
# for i in range(1,10,1):
#     print(f'{num} x {i} = {num*i}')
list1=[["피카츄","라이츄"],["파이리","리자몽"],["꼬북이","거북왕"]]
for str1 in list1:
    print("진화전 : " , str1[0])
    print("진화전 : " , str1[1])
    print()
#집합자료와 딕셔너리 사용가능
#순서가 없기 때문에 대입되는 값이 바뀔 수 가 있어요.

# a= {2,1,1,2,"A","A","B","B"}
# for i in a:
#     print(i)
#중복되지 않는 값들만 출력(순서 보장되지 않음)
# b= {"A":1,"B":2,"C":3}
# for i in b:
#     print(i)
#     print(b[i])

# eng_dict = {
#     "sun" : "태양",
#     "moon" :"달",
#     "star" : "별",
#     "space" : "우주"
# }

# for word in eng_dict:
#     print(f'{word}의 뜻은 {eng_dict[word]}')
#for문의 중첩: 2중 for문,3중 for문
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} X {j} = {i*j}')
#     print()
# for i in range(1,4):#1~3
#     for j in range(1,4):#1~3
#         for k in range(1,4):#1~3
#             print(i,j,k)
#-------------------------------------------------------------
#함수 - 내장 함수
'''
파이썬 언어에서 기본으로 제공하는 함수
>print(),input()와 같이 그냥 사용할 수 있는 함수
>종류가 엄청나게 많지만 자주 사용되는 함수들을 익힌다

함수명(인자값1,인자값2...)
'''
print('hello')#출력
len('abc')#길이반환
int("123")#문자열 정수로 변환
str(456)#숫자를 문자열로 변환
type(3.14)#자료형확인
input("이름 :" ) #사용자 입력
range(5)
sum([1,2,3])# 합계계산

chr()#특정 문자의 유니 코드 값을 전달하려면 
#해당 유니코드 값을 가진 문자를 반환

'''
아스키코드(ASCll: American Standard Code for information
                intrtchange)
            미국 표준 코드 , 영문자, 숫자, 특수문자등을 컴퓨터가 처리할 수 있도록 변환한 표준체계이다
            즉 문자마다 고유한 숫자가 배정되어 있음
    특징 : 문자 수 7비트로 표현(128개의 문자)
    범위 : 영어,숫자 ,특수기호
    호환성: 좁음
    사용용도 : 고전 시스템, 단순한 영문처리
유니코드 : 전세계의 모든 문자(글자,숫자,기호 등)을 하나의 통일된
    방식으로 표현하기 위한 국제 문자 인코딩 표준
    배경: 문자만 표현할 수 있음. 비 영어권 (한글,한자,일본어,아랍어,
    언어를 표현하지 못하는 문제가 생겨서 유니코드가 등장.
    특징 : 문자 수 : 143000개 이상
        범위 : 전세계 언어, 이모지, 특수 문자 
        사용범위: 현대웹, 앱,다국어 문서등)
        다양한 인코딩 방식 (UTF-8,UTF-16,UTF-32 등)'''

print(chr(43032))
print(chr(65))#A
print(chr(97))#B
a= "A"

#ord(문자) #뮨저를 유니코드롷 입력

print(ord('A')) #65
print(ord('가'))
#evaluate
#eval() : 특정식을 문자열로 전달하면 결과값을 제한
print(eval("100+200"))
a=10
print(eval("a*5"))


print()

expr = input('계산식을 입력 : ')
result = eval(expr)
print(expr + "=" +str(result))

#eval(input())처럼 외부입력을 그대로 사용하면 악성코드를 실행
#실무에서는 보안상 위험으로 잘안씀
#AST.LIFERAL_EVAL()과 같은 안전한 대안을 사용하는 것이 일반적이다.

print()
print()
#format():형식을 갖춘 문자열 반환
print(format(10000))
print(format(10000,'.'))

print()
print()
#abs() : 절대값을 반환
print(abs(10))
print(abs(-10))
print(abs(-10.1))
print()
print()

#divmod(value1, value2): 두 인수를 나누어 몫과 나머지를 튜플로 반환한다.

print(divmod(10,3))

#거스름돈 계산기
money = 10000
price=3000
bread, change=divmod(money, price)
print(F'빵을 {bread} 개 사고 {change}원이 남았습니다.')

#max() :인수 중에 가장 큰 값을 반환
print(max(1,2,3,4))
list1 = [10,4,3,2,9,11]
print(max(list1))

#min() :인수 중에 가장 작은 값을 반환
print(min(1,2,3,4))
list1 = [10,4,3,2,9,11]
print(min(list1))

#pow(제곱할 인수, 제곱근) : 거듭제곱 반환
print(pow(10.3))


#round() :소수점 반올림
print(round(1.5))
print(round(1.555,1))#자리수 지정

#sum() : 합계 반환
list3 = [1,2,3,4,5]
print(sum(list3))

#enumerate() : 리스트에 저장된 요소와 해당 요소의 인덱스가 튜플로 반환

for item in enumerate(["가위","바위","보"]):
    print(item)

for idx, item in enumerate(["가위","바위","보"]):
    print(idx, item)
print()
print()
print()

#zip() : 잔딜된 여러개의 객체의 각요소를 튜플로 묶어서 반환
names = ["유재석","김종국","송지효"]
scores=[60,77,88]
for  student in zip(names,scores):
    print("{}의 정수는 {}점입니다".format(names, scores))

#-------------------------------------------------
