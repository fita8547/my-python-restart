#함수
#----------------------------------------------------
'''함수 function(== method메ㅅ시드와 같은 말)
>특정한 기능을 수행하는 코드 블록에 이름을 붙인것
> 즉, 어떤 기능을 수행하는 코드를 묶어서 ,
필요할떄 마다 호출에서 사용하는 구조

장점
>한번 만들어 놓으면 언제든지 재사용 사능
>중복된 코드 제거
>프로그램의 구조화
    >작업 단위로 코드를 묶어서 구조화 시킨다.
    
    
    
1.코드 재사용: 같은 코드를 여러번 복사하지 않고 호출만 하면 됨
2.가독성 향상 : 코드의 의미를 이름으로 표현가능
3.유지보수 쉬움 : 변경 시, 함수만 수정하면 됨
4.디버깅관리 : 문제를 함수 단위로 나누어 확인 가능
5.모듈화 기능 : 프로그램을 잘게 나눠서 협업이나 분산 개발 가능.

[함수 정의의 특징]
1. def 키워드로 정의
    def 함수 이흠(매개변수1,매개변수2):
        실행할 코드 
        return 반환값(또는 결과값)

def: define정의 한다 : 함수를 정의 할떄 사용하는 키워드 
함수 이름 : 함수의 이름은 의미있는 이름으로 작성
매개변수 : 힘수입력 받는 값들
콜론 : 함수의 시작을 알리는 문법
실행할 코드 : 함수가 수행할 작업
return : 결과값을 반환하고 함수를 종료

2.매변수의 다양성
    2-1.  매개0변수(peramter)
    -함수에 값을 전달받기 위한 변수
    -함수 밖에서 함수 안으로 정보를 전달하는 통로
    -갯수 제한이 없고, 필요 없으면 생략도 가능
    -함수를 호출할떄 전달하는 값을 인수라고 부른다
    (인수 : ARGUMENT)
def greet(name): #name:parameter
    print('f{name}임, 안녕하세요!')
greet("윤지) #함수 호출 "윤지"는 인수가 된다.
    2-2 매개변수의 다양성
    기본인지 def greet(name="윤지")
    위치인자 def add(x,y):
    키워드인자 def into(age, name):
        info(age=10, name='yunji)
        가변인자 여러개의 값
    3-1 반환 값(RETURN VALUE)
    함수의 실행결과로 밖으로 돌려주는 값
    -함수의 결과로 저장하거나 
    -반환값이 여러개일 수 도 있음
    -튜플 형태로 여러 값도 반환 가능
    -return 을 사용하면 함수의 수행이 끝난다
    def calc(x,y):
    return x+y,x-y

a,b= calc(10,3)
print(a,b)

4.중첩 함수(함수안에 함수)
def outer():
    def inner():
        print("안에서 실행됨)
    
    inner()
>내부에서만 쓰는 로직을 감출 수 있음.

람다 함수 (LAmbda)
>짧은 익명 함수 작성 가눙
>한줄로 작성하는 , 이름 없는 함수 
>LAMBDA키워드를 사용해서 마들고
>주로 간단한 연산이나 함수를 써야할떄 사용한다.
<문법>LAMBDA 매개변수: 표현식
>매개변수: 일반함수 매개변수와 동일학[ 여러개 가능
>표현식 : 계산식이나 처리할 로직, 한줄만 작성가능!
>결과 없이 자동으로 반환됨.


print()
print()
print()
#예제1
square = lambda x: x **2
print(square(5))
#예제2 
add= lambda a,b: a+b
print(add(3,7))

#예제3
data= [(3, 'banana'),(2,'cherry'),(1,'apple')]
sorted_data=sorted(data,key=lambda x:[1])
#sorted()함수 : 리스트를 정렬해서 새 리스트로 반환.
#원본리스트는 변경되지 않음.
#key=매개변수로 함수나 표현식넣음
print(sorted_data)

7.주석으로 설명가능
def greet():
    """이함수는 인사합니다."""
    print("안녕하세요!")
>greet.__doc__로 설명 확인 가능



[함수의 형태 4가지]
1. 매개변수와 반환값이 둘다 있는 함수.
2,매변수도 없고 반환값도 없는 함수
3.매개변수만 있고 반환갑은 없는 함수
4. 반환값만 있고, 매개변수는 없는 함수

'''

print("[함수]")
#함수는 define하기만 하면 프로그래ㅑㅁ 수행에 영향이 없다.
#함수를 정의 한다 = 이후 이함수를 언제든 사용할 수 이도록 준비.
print("[함수의 4가지 형태]")
print("1.매개변수와 반환값이 둘다 있는 함수.")
#외부로 부터 값을 받아서 그 결과를 계산하고 반환
#가장 많이 쓰이는 일반적인 |형태
def add(x,y): #매개변수 x,y
    return x+y#반환값 있음.
result = add(1,2) #함수 호출(1)
print(result)
print("{} + {} = {}".format(1,2,result))
print("{} + {} = {}".format(3,4,add(3,4)))#함수 호출

#반환 값이 있는 함수 를 호출했을 떄는
#함수의 기능 수행이 끝난뒤 반환 값을 들고 온다.
#> 사용목적: 입력값에 따라 결과가 달라지는 계산, 처리, 분석 등에 적합

print("@. 매개변수와 반환값이 둘다 없는 함수.")
#외부로 부터 아무 값도 받지 않고, 결과도 돌려주지 않는다.
# 내부에서 직접 출력하거나 동작만 수행

# def say_hello():
#     print('안녕하세요')
#     #함수를 호출하면, 코드의 흐름이 내가 호출한 함수의 수행문으로 '점프'
#     #함수의 수행문이 끝나면, 함수를 호출했던 원래 위치로 되돌아 온다.
#     #단, 반환 값이 있다면 값을 반환한다.

#     say_hello()
#     #매개변수에 따라 함수를 호출할떄는 규칙을 맞춰야 한다.
#     #반환 갑에 따라서  큐칙을 맞추지 않아도 사용은 가능하다.
#     #반환값이 있다 == 값을 변수에 대입, 그 값을 어딘가에 바로 사용ㄷ
#     print()
# print()
# result = say_hello()
# print("say_hello()함수 호출의 결과 값 1:",result)
# print("say_hello()함수 호출의 결과 값 2:",say_hello())

#사용목적: 단순 출력, 상태표시, 메뉴화면 보여주기 등
#결과 값이 필요없는 동작위 로직에 사용
print("3.매개변수만 이꼬, 반환 값은 없는 함수")
#>외부에서 값을 받지만 , 결과를 돌려주지 않고 그냥 수행만 한다.
#>print()나 저장, 로깅 등으로 결과를 보여줄 수 있다.
#> 사용목적 :
#반은값으로 내부에서 메세지 출력, 파일 쓰기, 화면 표시 등

print("3.매개변수만 없고, 반환값만 있는 함수")
#>아무것도 받지 얺았지만 미리 정해진 결과를 돌려준다.
#> 상태확인, 고정된 설정값 전달 등에 사용된다.

def get_name():
    return "yunji"

name = get_name()
print(name)

#return 뒤에 오는 값의 자료형에 따라서 반환된 결과도 그 자료형이 된다.
#>사용목적:
#고정된 정보 제공 ,내부 계산결과 반환, 무작위 값 생성등
#함수의 기본 개념
#여러값 반환하기
#파이썬 함수는 여러개의 값을 한꺼번에 ㄱㄷ셔구 할 수 있음

#예제1
def get_name_and_age():
    return"yunji",35
name, age=get_name_and_age()
print(name)   
print(age)



#예제2 
def calc(x,y):
    return x+y, x-y,x*y #하나의 튜플로 반환
print(calc(10,2))
print(type(calc(10,2)))
a,b,c=calc(10,2)
print(a,b,c)
#매개변수에 초기값 사용(기본값 인수)
#함수 호출시 인자를 생략하면 기본값이 사용됨
#뒤에 오는 매개변수만 기본값을 가질 수 있음.

#예제1
def greet(name='친구'):
    print(f'{name}님,안녕하세요')
greet()
greet("윤지")


#예제2
def power(base,exponent=2):
    return base ** exponent
print(power(3))
print(power(3,3))

# 에쩨3 
def print_info(name, age,phone='010-xxxx-xxxx'):
    print("이름: ",name)
    print("나이",age)
    print("전화번호",phone)

print_info("홍길동",20,"010-1111-2222")
print_info("임꺽정",30,"010-2222-4444")
print_info("성춘향",17)

#매개변수에 초기 값을 적용하려면,
#초기잢이 들어가는 매케변수는 맨뒤에 위치해야한다!

#키워드 인수 (keyword Arguments):함수의 매개변수명을 키워드로 사용 
# 함수 호출시 인자의 이름을 명시하여 전달
#> 순서를 바꿔도 작동한다.
#예제1
def introduce(name, age):
    print(f'{name}님은 {age}세 입니다.')
introduce(age=37,name="yunji")

#예제2 
def drink_order(menu, size):
    print(f'{size}사이즈 {menu}주문 받았습니다.')
    drink_order(menu="아메리카노",size="Large")

#예제3
def print_info(name,age,phone):
    print('이름 : ', name)
    print('니이 : ',age)
    print('전화번호 : ', phone)
print_info('홍길동',20,"010-1111-2222")#함수호출
print_info(age=19,name="임꺽정",phone="010-4444-3333")#키워드 인수 사용
print(1,2,3,sep='ㅋ')
#print함수 사용시 sep 갓을 넣어주는 행위(키워드 인수)
#가변 인수 : 전달하려는 값의 갯수가 변할 수 있더.
#>인자를 여러개 받을 수 있는 함수
#*args:여러개의 위치인자를 튜플로 받음
#**kwargs :여러개의 키워드 인자를 딕너리로 받음
#args 예제1
def add(*args): #argments :인수들
    print(args)
    add_result=0
    for i in args:
        add_result+=1
    return add_result
print(add(1,2,3,4,5))
print(add(1,2,3))

#일반 매개변수, 가변매개변수, 가변 인수를 *args는 마지막위치에 작성
#초기값이 지정된 매개변수나 가변인수 *args는 뒤;에 작성

#args 예제2
def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4,5))
print(total(1,2,3))

#args 예제3
def show_item(*items):
    for item in items:
        print(f'-{item}')
show_item('사과','바나나','딸기')



#**kwards 예제1
def print_info(**info):
    return info
profile= print_info(name='yunji',city='대구')
print(profile)

#여러개의 키워드 인자 받아서 딕셔너리로 변환

def func3():
    print("fun3() 시작")
    print("fun3() 끝")
    
def func2():
    print("fun2() 시작")
    print("fun2() 끝")
    
def func1():
    print("fun1() 시작")
    print("fun1() 끝")
print("func1() 호출 전")
func1()
print("func1()호출 후 ")
#---------------------------------------------------------------
#재귀함수
#---------------------------------------------------------------


'''
-함수의 수행문 안에서나 자기자신 함수를 다시 호출하는 함수
-수행문이 반복되기 떄무에 반복문과 유사한 성격
-너무 많아 반복 수행하다보면 프로그램 오류 발생
-함수 호출 시 stack이라는 구조의 메모리를 사용
-stack : First in,Last Out
    -Stack용량이 초과될 정도로 많이 호출하면 오류
    StackOvercomeflow 오류 발생
    -함수 호출시  Stack을 사용하는 이유는 함수 수행이 끝난 후
    돌아갈 위치를 저장하기위해서'''

def fuc(num):
    print('func() start,num = ',num)
    if num == 1:
        return 1
    else:
        return num * fuc(num-1)
print(fuc(3))




#-----------------------------------------------------------------------------------------------
#지역변수와 전역변수
#-----------------------------------------------------------------------------------------------

'''
1. 전역변수 (Grobal Variable)
정의:함수 바깥에서 선언된 변수
어떤 함수 안에서도 접근 할 수 있음.

특징 코드 전체에서 사용가능
프로그램 전체에 영향을 줄 수 있음
실수로 값을 바꾸면 버그 위험 있음 
'''
#예제1
count =10 
def show_count():
    print('count = ',count)
show_count()


#예제2
meseage='안녕하세요'
def greet():
    print(meseage)
greet()

'''
지역변수(local Variable)
정의 : 함수 안에서 선언된 변수
그 함수 안에서만 사용가능

특징: 함수 안에서만 사용가능한 변수
같은 이름의 변수를 다른 함수에서 독립적으로 사용할 수 있음'''

#예제1
def say_hi():
    name_1="윤지" #전역변수
    print(f'{name_1}님, 반가워요!')
say_hi()
#say_hi(name_1)

#예제2
def sqare():
    number=5 #지역변수
    print(number * number)
sqare()
#print(number) #오류발생! number 정의 되지 않음

#---------------------------------------------------------
#예제1 : 전역변수 읽기
total = 100
def show_total():
    print("총합은",total)
show_total()
#>이경우는 읽기만 하므로 문제가 없음.
#예제2: 전역변수 수정하기 (Global 키워드 필요!)
score =0
def add_score():
    global score
    score+=10
add_score()
print('점수 : ',score)

'''
global 키워드
> 함수 안에서 전역변수를 참조하고, 수정하기 위해 사용
>함수 안에서 이미 존재하는 전역변수를 사용하겠다고 명시
>함수 빡에서 곧바로 사용가능한 전역변수
>이변수는 지역이 아니라 전역공간에 있어. 내가 수정하려해 ! 라고 선언
>전역변수를 지역변수로 변환 하겠다는 것이 아니라
>전역변수를 사용하겠다는 '표시'하는것
'''
#예제1: 전역 변수 수정하기
count=5
def increase():
    global count #전역변수임을 명시!
    count+=1

increase()
print(count)


#예제2
value='전역변수'
def func1():
    print("func1() 호출")
    print(value)
    func1_value = 'func의 지역변수'
    print(func1_value)
func1()
#print(func1_value)
print(value)

print()

def func2():
    print('func2() 호출')
    value = '지역변수 변경!'
    print(value)
func2()
print(value)
#전역변수 value가 있는데 
#지역에서 같은 이름으로 변수에 값을 대입하면 
#value 라는 지역변수 생성

def func3():
    print('func3()호출')
    global func3_value
    func3_value = '함수 3의 지역변수'
    print(func3_value)
    
def func4():
    print('func4()호출')
    global value
    func4_value = '전역변수 변경'
func3()
print(func3_value)
func4()
print(value)

#> 되도록 지역변수만 사용하면 안전하다.
#>적역변수는 공통설정값, 전체 상태 저장할떄만 사용
#변수명이 겹치지 않도록 주의

#------------------------------------------------------------------

'''
코드가 너무 길면 쪼개서 관리하기가 힘들기 떄문에 
모듈과 패키지를 사용한다. 모듈과 패키지를 활용하면 꺠끗하고 
체계적인 코드 작성이 가능하다.
팀 작업 시, 나눠서 개발하고 협업에 유리하다.

모듈(module)
-파이썬 파일 (.py)을 그대로 하나의 도구로 쓰는 것
-함수, 변수,클래스등을 담고 있는 .py파일 하나가 모듈이다.
-간단한 기능을 담을떄 사용한다.
-다른 파이썬 파일 에서 가져다 쓸 수 있다.
-ex) math.py, my_utils.py 같은 파일
#예제1:mymath.py파일 라는 모듈 생성
# mymath.py
# def add(a,b):
    return a+b
def sub(a,b):
    return a-b
#main.py
import mymath

print(mymath.add(3,4))
print(mymath.sub(10,2))'''

#예제2: 내장 모듈사용하기
# import math
# print(math.sqrt(16))
# print(math.pl)


'''
패키지(package)
-여러모듈을 폴더로 묶어 놓은 것 
-코드가 많고 복잡할떄 사용(모듈에 비해서)
-관련 모듈들끼리 한 폴더에 넣어 놓은 형태
-반드시 그 폴더안에 _init_.py파일이 있어야 패키지로 인식됨
    >파이썬3.13버전 이후는 생략가능하지만
    >하위버전 호환을 위해 가급적만들어 두는 것이 좋음
-폴더 안에서 또 다른 폴더가 있는 하위 구성일떄도 동일함

[패키지 설치]
pip install 패키지명

[패키지 삭제]
pip uninstall 패키지 명

[_init_.py 역활]
'이 폴더는 패키지다'라고 파이썬에게 알려주는 표시이다.
관습적으로  많이 쓰이기 떄문에 되도록 생성하는 것이 좋다
공통설정, 초기화 코드,패키지 불러 올떄 실행될 코드를 넣을 수 있다.

#패키지의 _init_.py 파일이 가장 먼저 수행된다.
'''

#예시1: _init_.py
#mypackage/_init_.py
print('my_package 불러왔어요!')

#>import mypackage 했을떄 저 문장이 콘솔에 출력됨.

#예시 2: 모듈을 감춰주는 역활
#mypackage import *
#이렇게 사용했을 시, mod1,mod2만 불러오고, 나머지는 무시함
#보안이나 인터페이스 정리용으로 많이 사용함.

#[_all_의 의미]
#from mypackage import *
#이렇게 사용했을 시, mod1, mod2만 불러오고, 나머지는 무시함
#보안이나 인터페이스 정리용으로 많이 사용함.
#[_all_의 의미]
#from 패키지 import * 했을떄 불러올 수 있는
#모듈 또는 변수/함수 리스트
#상대경로 임포트 
#같은 패키지 내에서 모듈을 불러올떄 현재위치 기준으로 임포트 하는 방식
##FROM , IMPORT MOD1
##from ,



from my_package import module_a, module_b
from my_package.sub_package import module_c
module_a.func_a()
module_b.func_b()
module_c.func_c()
#수치해석과 통계에서 많이 사용하는 
#명령 프롬프트에서
#pip list:설치된 패키지 목록 보기
#pip instal numpy:numpy패키지 설치
# import numpy as np
# print(np.sum([1,2,3,4,5]))
#설치된 패키지 삭제하기







