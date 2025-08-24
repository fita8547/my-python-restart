#=--------------------
#문자열관련 함수

#문자열은 텍스트처럼 띠옴표로 묶어서 표현
#문지열에는 자주 사용하는 함수와 메서들이 있음
#문자열에는 함수()형태로 사용


'''
메서드   설명
len()  문자열 길이구하기
max() 큰 숫자 알파벳 순서상 가장 뒤에 나오는 문자
min() 가장작은 숫자나 알파벳 순서상 가장 앞에 나오는 문자
lower() 모든글자를 소문자로 변경
upper( 모든글자를 소문자로 변경)
title()문자열에 존재하는 영단어의 첫글자를 대문자로 변환
strip() 앞뒤 공백 채우기
lstrip() 왼쪽공백지우기
rstrip()오른쪽공백지우기
replace(ord,new) 특정글자를 다른 글자로 대체
join() 특정문자열을 대상으로 문자열 사이사이에 삽입
sprit()특정기준으로 문자열을 잘라서 리스트로 변환
index("A") 문자열에서 A를 찾고 그위치를 변환
find("A) 문자열에서 A를 찾고 그 위치를 변환
in 연산자 문자열 내부에 어떤 문자가 있는지 확인할떄 사용
'''
print('안녕' in "안녕하세요")

print('안녕' in "안녕하세요")


#문자열 길이 구하기
a= "life is too short"

print(len(a))#17자, 빈칸 포함한다.
print(max(a))
print(min(a))

b="victory"
print(max(b))
print(min(b))

#대소문자로 변환
print(a.upper())#출력할떄만 모두 대문자로 변경
print(a.lower())#출력할떄만 모두 소무자로 변경
print(a.title())#단어의 첫번쨰만 대문자로 변경
print(a)

#strip  앞뒤 공백 지우기
#replaced(ord,new) 특정글자를 다른글자로 대체
str1=" hello, world!  "
print(str1.strip())#앞뒤 공백제거
print(str1.replace(" ",""))#치환 함수를 이용해서 공백 제거하겠다
print(str1.replace("hello","hi"))

#split()
# #join
str2="서로에게 모든 것을 줄 떄 평등한 거래가 된다. "
print(str2.split())#기준되는 문자를 적지 않으면 
                    #기본 개행으로 공백으로 나눠진다.

print(str2.split("평등한")) #기준되는 문자는 없어짐
                            #결과는 리스트(자료혈)로 저장되어 나왔다.

#join
str3="ABC"
print("-".join(str3))
print(".".join("hello"))

str4 = "apple, banna, grape"
print(str4.split("."))
#print(str4)
str5 = str4.split(",")
print("-".join(str5))



# count("A") : 문자열에서  A 갯수 반환
str6="안녕하세요 저는 장준수 입니다. 파이썬 수업 입니다. "
print("str6레서 입니다의 갯수 :",str6.count("입니다"))


#index()
#find()
print(str6.index("저"))#위치를 찾는 함수, 위치를 반환
print(str6.find("저"))

print(str6.find("가"))
print()
print()
print()
print()
print()


print(str6.find("입"))
print(str6.rfind("입"))#뒤에서 붙터 처음 찾은 위치
print(str6.find("입",20))#인덱스 20번쨰부터 찾은 위치


#------------------------------
#연산자
#산술 연산자 : 수치 값을 계산할떄 사용하는 연산자
'''
더하기+
빼기-
나누기 / ->결과가 실수형
몫 //
나머지 % 
제곱 **
'''

a=1
b=2
print("a+b=", a+b)
print("a*b=", a*b)

#비교연산자 : 두 값을 비교햐서  T, F변한
'''
크다 a>b
작다 <
이상 크거나 같다 >=
이하 작거나 같나 <=
같다            ==
같지않다         !=
'''
print("a !=b",a != b)
print("a == b", a==b)
print("a > b",a>b)

#논리 연산자
'''
참 True
거짓 False
논리부정 not (모두참이면 참 True)
논리곱 and (모두 참이면 참 True)
논리합 or (하나라도 참이면 참 True)
'''

c=10
print("c는 20보다 작나요?", c<20)
print("c는 20보다 크거나 같나요?",not(c < 20))


num1=10
num2=2
print((num1>5) and (num2<5))
print((num1<5) or (num2<5))
#복합대입연산자 :대입과 산술을 한번에 처리하는 연산자
#코드를 더 간단하고 읽기 쉽게 만들기 위해서 사용한다
#내부적으로 조금 더 최적화된 연산이 가능

a = 10
a +=5 #a = a + b
print(a)
a *= 5 # a= a * 5



#문자열로 복합대입연산자 사용해보기
s = "안녕하세요"
print('원본:',s)

s+='!'
print('!하나 추가 후:',s)

s+='!'
print('!하나 더 추가 후 :',s)


#------------------------------------
#문자열 포멧팅
'''
문자열 안에 변수나 값을 넣어서 원하는 모양의 문자열을 만드는 방법
>사용지에게 정보를 보여줄떄
>로그를 출력할떄
>파일이름 자동생성
>수치나 날짜 형식 조정할떄'''
#1.퍼센트 %방식(구식)
#2.format() 함수 사용 방식
'''
>파이썬 2.7부터 도입
>중괄호 안에 순서나 이름을 지정
s-string 방식 (파이썬 3.6이상)
>가장 현대적으로 많이 사용하는 방식
>문자열앞에 f또F를 붙이고 , 중괄호 안에 변수나 수식을 삽입
>가독성이 좋고 간단하다
>숫자 포맷팅도 지원(예,소수점 자리수 지정)
'''
'''
퍼센트 %방식
<문법>
*문자열 %타입기호 "%값
%s:문자열
%c:문자
%d:정수
%f:실수
%o:8진수
%x:16진수
%%문자: '%'
'''
name="준수" #문자열 #s
age=30
height =167.423132
print("이름은 %s입니다"%name)# 문자열 출력
print("나이은 %d입니다"%age) #정수 출력
print("키는 %fcm입니다"%height) #실수 출력
print("이름은 %.1fcm입니다"%height)#실수 소수점지정

print('i eat %d apples,'%3)
#print('i eat %d apples,'%'five')
#print('i eat %d apples,'%'f')

#----------
#2. format()힘수 방식
#<문법>
#"문자열{}.format(변수 또는 상수)"
"""
중괄호를 포함한 문자열 뒤에 마침표를 찍고 format()함수를 사용하되,
중괄호 갯수와 format 함수안 매개변수의 갯수는 반드시 같아야 한다.
문자열의 중괄호 기호가 format함수 괄호 안에 매개변수로 차례대로
대치되면서 숫자가 문자열이 된다."""
print()
print()
print()
#순서대로 삽입
#print('이름:{}, 나이 : {}'.format("차수",20))

#인덱스 지정
#print('이름:{}, 나이 : {1}'.format("차수",20))

#키워드 인자 지정
#print('이름:{name}, 나이 : age}'.format(name="차수",age=20))


name="유재석"
age= 45
print("1.제이름은 {}이고 {}살 입니다.".format(name,age))
print("1.제이름은 {1}이고 {0}살입니다.".format(name,age))
print("1.제이름은 {name1}이고 {}살입니다.".format("이름",age,name1=name))
'''
참고 규칙!
위치 인자{} 는 앞에서부터 순서대로 채워짐
키워드 인자{name}등은 변수이름을 지정해서 삽입
주의할점!
위치인자가 먼저 모두 처리 된 후에 키워드 인자가 들어와야야함.
위치인자를 {}보다 많이 넣건,{}보다 적게 넣으면 오류 발생
'''
#오류
#"{} {}".format("hello",name="유재석")
# {0} {1}.format("hello",name="우재석")
# 
# 
#올바른 표현
# 모두 위치인자
#"{A} {B}".format(A="hello",B="유재석")
#섞어 사용할때는 위치 이자 먼저. 그다음 키워드 인자
#"{} {B}".format(A="hello",B="유재석")

#키워드 인자 작성후 위치 인자 들어 갔을때 에러 발생
#'{A}{}'.format(A="hello","유재석")
#"{A} {}".format("유재석",A="hello")
#정렬
#0는 format 함수 안에 넘갸즌 첫번쨰 인자값 의미
#: 뒤부터는 어떻게 출력할지 설정하는 영역
#<왼쪽 정렬
#>오른쪽 정렬
#^가운데 정렬

print('{0:>10}'.format('hi'))
print('0:<10'.format('hi'))
print('{0:^10}'.format('hi'))

pi=3.141592
print('{0:2f}'.format(pi))
a=30.0
print('{:g}'.format(a))#의미없는 소수점제거
#g는 파이썬 문자열 포멧팅에서 사용하는 형식 지정자 중에 하나
#g는 살수를 출력할떄 자동으로 소수점 표기법 또는 지수 표기법중 적절한 것을 
#선택하여 출력한다.
#a가 실수일 경우
#그렇지 않으면 : 일반 소수 표기법(f)
#불필요한 소수점 이하 0은 제거 시키는 것

b=0.00000123 #크기 너무 작을 경우
print('{:g}.format(c)')#지수 표기법으로 표기됨

#출력을 세밀하게 조절할떄 자주쓰는 형식
#천단위 쉼표  '{:,}'.format(100000)
#%백분율 표기 '{:.1%}.format(0,1234)
#'{:.2f}'.format(10000000,123)# 천단위 구분기호 + 소수점 2자리
#{:1%}:백분열로 표현

#예시: 천단위 쉼표+소수점
price=1234567.89
print("총가격은 {:..1f}원 입니다.")
rate=price%100
print("이자율:{:.1%}".format(rate))

#==========================
#3.f-string방식
#가장 읽기 쉬움
#현대적
#문자열앞에 f
#<문법>
name="준수"
print(f"안녕하세요 {name}님!")

#계산식 넣기
a=5
b=4














#문제 1
v="hello"
print(v.count("e"))

#문제2 
text="Hello world"
print(text.upper)
print("hello" in "hello world")

#문제3
a=10
b=3
print(a%b)

x=5
x+=3
print(x)
a=7
b=10
print((a<b)and(a>5))

x=10

print((x//2)>4)





name="Alice"
print(f'Hello, {name}!')
pi=3.141592
print(f'{pi:.2f}')


print('{0:^4}'.format(5))


#문자열_연산자_문자열포멧팅_문제
'''
[문자열 관련 함수 및 메서드 문제]
1. 문자열 'hello'에 포함된 'e'의 개수 count 를 출력 print 하는 코드를 작성하세요.
>>	print('hello'.count('e'))
2. 문자열 'Hello World'를 모두 소문자 lower() 로 바꾸고, 
'world'라는 단어가 포함되어 있는지 확인하는 코드를 작성하세요. in
text = 'Hello World'
text = text.lower()
print('world' in text)

[연산자 관련 문제]
1. 변수 a=10, b=3일 때 a를 b로 나눈 나머지(/, %, //)를 출력하는 코드를 작성하세요.
a=10
b=3
print(a % b)

2. 변수 x=5일 때 복합대입연산자를 사용하여 x에 3을 더한 후 출력하세요.
x=5
x += 3 #x = x + 3
print(x)


3. 변수 a=7, b=10일 때 a보다 b가 크고 a는 5보다 크다는 논리식을 출력하세요.
a=7
b=10
print((a < b) and (a > 5))

4. 변수 x=10일 때, x를 2로 나눈 몫을 구한 뒤 그 값이 4보다 크면 True, 아니면 False를 출력하세요.
x=10
result = x // 2 > 4
print(result)



[문자열 포맷팅 관련 문제]
1. 변수 name에 'Alice'를 저장하고 'Hello, Alice!'라는 문장을 출력하세요. (f-string 사용)
name = 'Alice'
print(f"Hello, {name}")

2. 소수점 이하 두 자리까지 출력되도록 3.141592를 포맷팅하여 출력하는 코드를 작성하세요.
pi = 3.141592
print('{:.2f}'.format(pi))

3. 정수 5를 폭 4칸에 오른쪽 정렬하여 출력하는 코드를 작성하세요.
print('{:>4}'.format(5))
'''