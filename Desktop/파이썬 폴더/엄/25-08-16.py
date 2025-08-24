#예외처리(Exeption Handling)
'''프로그램 실행도중에 발생할 수 있는 에러(예외)를 미리 감지하고ㅡ
프로그램이 강제 종료되지 않도록 안전하게 처리하는 방법

예외란?
코드를 실행하다가 문법은 맞지만 실행 중 문제가 생기는 경우.
예) 0으로 나누기, 없는 파일 열기, 리스트 범위 벗어나기 등

예외처리가 필요한 이유
에러 발생 시 프로그램이 종료되지 않게 하고,
사용자에게 친절한 메세지를 주거나,
복구 가능하면 복구할 기회를 주기 위해 사용한다.

[기본구조]
try - except - finally

try :
    예외가 발생할 수 있는 코드 (무조건 진입해서 수행)
exept 예외 종류:
    예외가 발생했을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 무조건 실행되는 코드
    >정상/오류 없이 마무리이나 코드가 있을 떄 사용
    finally는 반드시  try except와함꼐 사용, 단독으로 사용하면 문법오류'''

# #예제
# try:
#     input_num=int(input("숫자를 입력하세요 : "))
#     print("결과 : ",input_num)
# except:
#     print("숫자를 입력하세요")
# finally:print("예외 처리 끝")

# #예제2 : 0으로 나누기
# try:
#     a=10/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 있습니다.")
# finally:
#     print("무조건 실행됩니다.")

#예제3 : 여러가지 예외 처리하기]
# try:
#     num=int(input("숫자 입력 : "))
#     result = 10/ num
# except ZeroDivisionError:
#     print("0으로 나눌 수 있습니다.")
# except ValueError:
#     print("숫자가 아닙니다.")

#예제 4 : 예외 객체 사용하기
# try:
#     a = 1/0
# except ZeroDivisionError as e:
#     print("에러 메세지 : ",e)
#     print("에러 타입 : ",type(e))
'''
>as 변수명 작성
>exept 블럭에서 예외객체를 담는 변수
>여기서는  e는 예외객체
>오류의 정보(종류, 메세지 등)을 담은 객체


예외 객체란? 
오류 상황을 표현하는 객체

1.예외 객체로 할 수 있는 것들 ? 메세지 출력
print(e)
2.예외 타입 확인 
print(type(e)) ZeroDivisionError
3.예외 객체를 직접 raise로 다시 결정시키기
4. 속성 접근 (고급 예외 객체는 다양한 속성을 가짐)
'''
# #예쩨 5
# try:
#     num1,num2 = map(int,input("두 수 입력 : ".split()))
#     print("나눈 결과 : ",(num1/num2))
#     my_list = [1,2,3]
#     index = int(input("인덱스 입력(0~2) : "))
#     try:
#         print("값 : ",my_list[index])
#     except:
#         print("try안의 또다른 try except문")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱스가 잘못되었습니다.")
# except :
#     print("뭔지 몰라도 오류가 났다.")



#예제 6
#else : 예외가 발생하지 않았을떄 실행괸다.
#필요하면 else도 사용가능하다.
# try :
#     print("정상 실행")
# except:
#     print("예외 발생")
# else:
#     print("예외없이 성공적으로 실행됨")




#------------------------------------------------------
#객체 지향 프로그래밍
#-------------------------------------------------------

'''
[object orient Programing]
-객체 지향 이론
실제 세계는 사물로 이루어져 있으면,
발생하는 모든 사건들은 사물간의 상호 작용이다.
이 개념을 토대로 프로그래밍 언어 접목 -> 객체 지향 프로그래밍

1. 객체 지향 프로그래밍(oop)개념
= '객체'를 중심으로 프로그램을 구성하는 방식
데이터를  속성(변수)와 기능 (메서드)로 묶어서 하나의 단위로 만들고,
이 단위를 재사용/ 확장하며 프로그램을 설계
절차 중심의 프로그래밍과 달리, 객체들이 서로 메세지를 주고 받으며
동작한다."데이터와 동작을 하나로 묶어서, 부품처럼 재활용 가능한 프로그램을 만드는 방법

2. OOP의 주요 특징
1) 캡슐화(Encapsulation)
데이터(속성)과 메서드(동작)을 하나의 객체 안에 감싸서 숨김
외부에서는 객체가 제공하는 메서드를 통해서만 데이터에 접근
코드의 재사용성이 높다
코드를 관리하기 좋다.
프로그램의 신뢰성이 높아진다.

2)상속(Inheritance) - 
기존 클래스의 기능을 물려받아 확장하거나 수정 가능

3)다형성(Polymorphism) - 
같은 이름의 메서드라도 객체 종류에 따라 다르게 동작 가능

4)추상화 (Abstaction) - 
불필요한 내부구현은 감추고, 필요한 기능만 노출

3. 클래스와 객체의 설명괴 차이 
클래스는 일종의 설계도이며
객체는 그 설계도를 통해 만들어진 실제 사물이다.
갤럭시 노트 9의 설계도 : 클래스
갤럭시 노트 9 : 객체


-클래스 class
객체를 만들기 위한 설계도
속성과 메서드가 어떻게 구성될지 정의

-객체 Object
클래스로부터 만들어진 실제 물건
메모리에 생성되어 독립적으로 동적

4. 인스턴스 (INSTANCE)
기본적으로는 객체와 같은 의미이다.
문장에서 쓰임에 따라 구분한다.
*클래스를 통해 실제 만들어진 객체를 '인스턴스'라고 한다.
클래스라는 설계도로부터 생성된 구체적인 객체
'객체'라는 말은 넓은 의미에서 만들어진 객체를 지칭
ex)
갤럭시 노트 9은  객체이다.
갤럭시 노트 9 설계도(클래스)로 객체를 만들 수 있다.
내가 가지고 있는 갤럭시 노트 9는 인스턴스이다.


'''
# class Dog:
#     pass
# mt_dog = Dog()
#my_dog는 Dog클래스의 인스턴스

'''
5. 객체의 구성요소 : 속성, 기능
(속성 : 갤럭시 노트9의 색상
기능 : 갤럭시 노트9의 카메라 기능)

# 1)객체는 클래스에서 정의하ㅣㄴ 다수의 속성과 기능을 가질 수 있다.
# 2)속성(Attribute)
#     객체가 가진 데이터(변수)
#         예) 이름,나이,색깔'
# 3) 기능 - 메서드(Mothod)
#     객체가 할 수 있는 동작
# -클래스룸 비유할 떄 
# 붕어빵틀(클래스)/ 만들어진 붕어빵 (객체)
# 자동차 공장(클래스) / 출고된 자동차 (객체)
# '''
# #예제)
# # class Dog:#Dog이름으로 생성된 클래스
# #     #생성자 : 객체[가 만들어 질떄 호출됨
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age=age

# #         #메서드 
# #         def bark(self):
# #             print(f'{self.name}이(가) 멍멍 짓습니다.')
# # #객체(인스턴스)생성
# # dog1 = Dog("초코",3)
# # dog2 = Dog("만두",5)
# # #속성에 접근 
# # print(dig.name, dog1.age)
# # print(dog2.name, dog2.age)

# # #메서드 호출 
# # dog1.bark()
# # dog2.bark()
        


# '''
# 1.클래스는 속성(변수)를 지칭하거나, 기능(함수)를 정의 할 수 있다.
# >함수나 마찬가지로 클래스로 작성해놓기만 하면 프로그램 수행에 영향이 없다.
# >객체를 생성한 뒤부터 클래스에 작성된 코드가 효력이 발생할 수 있다.
# 2.클래스 안에 정의 된 함수는 '메서드'라고 부른다.
# >(파이썬 언어 규칙) 메서드를 만들 떄는 반드시 최소 하나의 매개변수가 필요하다.
# >나 자신을 의미하는 self 라는 이름으로 한다.
# (꼭 self아니어도 되지만 관례적)
# '''
# #클래스 만들기
# class Car:
#     def power_on(self):
#         print("부릉부릉")
#         self.power = True #self에는 BMW가 대입 (이 메서드를 호출한 인스턴스)
#         #BMW인스턴스에 power라는 변수가 추가 되었다(변수 생성코드)
#         self.drive()#self=BMW이기 떄문에 BMW.drive()와 같다.
#     def drive(self):
#         print("주행시작")
# BMW=Car()#변수명 = 클래스명()
#         #Car클래스의 객체 (인스턴스 )생성
# BMW.power_on()#클래스에 정의된 함수 호출
#         #내부적으로 Car.power_on(BMW)호출과 동일하다
# print("BMW의 시동여부 : ",BMW.power)

# tico = Car()
# tico.drive()
# tico.power="시동 켜짐"
# print(tico.power)
# tico.model = "TICO 최신 모델" #tico에 model변수를 추가헤버림
# print(tico.model)
# #Car 클래스에  model이라는 속성이 원래 정의 되지 않아도.
# #인스턴스에 새속성을 동적으로 추가 할 수 있음
# # 이순간 , tico라는 객체의 _dict_안에 {"model":"TICO 최신 모델"}가 생김
# #tico만 이 속성을 가지게 됨.
# #다른 인스턴스에는 영향 없음.
# # print(BMW.model)에러발생하는 거 확인

# #클래스 Car()에도 model 정의 되지 않음.
# #따라서 AttributeError 예외 발생

# # 정리)


# #------------------------------------------------------------------------
# '''
# self는 파이썬 클래스/ 메서드에서 가장 중요한 개념이다.
# self는 그 메서드를 호출한 그 객체 자신을 가리키는 참조(=나 자신) 이다
# 1)self의 역할(요점)
# 인스턴스 자신을 가리킨다(this와 비슷한 개념)
# 인스턴스의 속성(Attribute)에 접근/ 수정 할떄 SELF.X로 사용.
# 다른 안스턴스 메서드를 호출할 떄 self.other_method()처럼 사용한다.

# 2)왜 필요한가?
# 파이썬의 클래스 내부에 정의된 함수는 보통 함수이다.
# 인스턴스에서 obj.method()로 호출하면 파이썬이 명목적으로 그 인스턴스(obj)를 첫번쨰
# 인자로 전달해준다. 그 인자를 받아 주는 인수(관례,self)




# a=A()
# a.foo() #typeError발생
# #self는 예약이 아님(이름 바꿀 수 있지만 self가 관례)
# 4) 값 전달 방식 -self는 참조이다.
# self는 객체에 대한 참조 (reference)를 받음 . 복사가 아님
# 예를 들어서 리스트 등을 self를 통해 수정하면 인스턴스 내부 상태가 바뀜.
# '''
# class Bag:
#     def _init_(self):
#         self.items=[]
#     def add(self,x):
#         self.items.append(x)
    
# b=Bag()
# b.add('apple')
# print(b.items)

# #파이썬 객체의 특징: 만들어 지는 인스턴트 별로 속성(변수)가 다를 수 있다.
# # #파이썬 객체는 필요할 떄 속성을 자유롭게 추가 가능.
# # 하지만 그 속성은 해당 인스턴트에만 적용되고, 다른 인스턴스에는 자동으로 생기지 않음.
# # 속성을 모든 인스턴스에서 공유하라면 클래스 변술로 정의 해야함




# #예제)
# class Car:
#     wheels =4
#     def __init__(self,color):
#         self.color= calor# 인스턴스 변수

# car1=Car("red")
# car2=Car("yellow")

# print(car1.color) # car1만의 색상

# print(car2.color) # car2만의 색상


# print(car1.wheel) # 공유
# print(car2.wheel) # 공유
# car.wheels =6 #클래스 변수 변경
# print(car1.wheels) # 모든 인스턴스에 반영된 것 확인 가능
# print(car1.wheels) # 모든 인스턴스에 반영된 것 확인 가능

# #인스턴스 변수는 각자 가짐 클래스변수는 다같이 가짐의 의미

# 클래스를 왜 사용할까?
#클래스 없이 자동차 2개 다뤄보기

# car1_model = "bmw"
# car1_power=False
# car1_max_speed =200

# car2_model = "sonata"
# car2_power = True
# car2_max_speed =280

# #자동차 주행하는 함수 
# def drive_car(model,power,max_speed,speed):
#     print("{}주행준비....".format(model))
#     if power == False:
#         print("주행불가 : 시동을 켜주세요.")
#         return
#     if speed > max_speed:
#         print("{}의 최고속도는 {}km입니다. 속도를 줄이세요".formt(model, max_speed))    
#     print("{}km로 주행합니다. 출발-").format(speed)

# drive_car(car1_model,car1_power,car1_max_speed,150)
# drive_car(car2_model,car2_power,car2_max_speed,200)

# #클래스의 사용
# #하나의 틀을 만들고 , 그 틀로 자동차를 생성한다.
# class Car:
#     def drive_car(self,speed,power,max_speed):
#         print("{} 주행준비...".format(self.model))
#     if self.power == False:
#         print("주행불가 : 시동 키세요")
#     if speed > self.max_speed:
#         print("{}의 최고 속도는 {}km입니다. 속도 줄이세요".format(self.model,self.max_speed))
#         speed = self.max_speed
#     print("{}km로 주행합니다.".format(speed))

# car1=Car()
# car2=Car()

# car1.model="bmw"
# car1.power="False"
# car1.max_speed =200
# car.model ="sonata"




#------------------------------------------------------------------------
#클래스의 사용 생성자
#---------------------------------------------
'''
인스턴스 생성 시 자동으로 호풀되는 특별한 메서드(함수) 무조건 호출
파이썬에서는 _init_()메서드가 생성자 역활을 한다.
목적 : 인스 턴스가 생성될떄 초기화 작업을 수행(속성 추가/초기값 지정 등)
자동 호출 : 객체이름 = 클래스 이름()을 하면 , _init_()이 자동 실행된다.
반환 값: None이어야 한다.(다른 값을 return 하면 안됨)
self: 새로 만들어진 그 객체 자신을 가리킨다.
생성자 함수 이름 규칙 : __init__(언더바 2개씩)'''
#기본문법
# class클래스명
#     def __init__(self,매개변수들):
#     # 초기화 코드
#     self.속성 = 값


#예제 1 -단순 초기화
# class Car:
#     def __init__(self,model,color):
#         self.model = model #인스턴변수 초기화
#         self.color = color
#         print(f'{model}생성됨!')
# bmw=Car("BMW520d")

#예제2 - 초기값 지정
# class Account:
#     def __init__(self,owner,blance=0):
#         self.owner = owner
#         self.balnce = blance

# acc1=Account("무현")
# print(acc1.owner,acc1.balnce)

# #생성자 특징
# '''
# 메서드명 고정 : 반드시 _init_사용
# 자동호출 : 객체 생성시 자동 호출
# 반환값 없음 : return으로 값 변환하지 않음
# 초기화 전용 : 주로 속성(변수) 초기화, 준비 작업에 사용
# 매개 변수 가ㅓ능 생성시 필요한 값을 인자로 받을 수 있음



# 생성자가 없는 경우
# __init__()를 정의 하지 않으면 , 파이썬이 빈 생성자를 제공.'''

# t=Test()
#생성지 없는 클래스를 통해서 인스턴스 생성시 오류 발생하지 않음.
#빈 객체 생성됨

#생성자 오버로딩 (파이썬 방식)
#파이썬은  c++/Java 처럼 여러 생성자를 만들 수 없음
#대신 기본 값 매개변수나  *args, kwargs 로 유연하게 처리 가능하다.

# class User:
#     def __init__(self, name=None,age=None):
#         self.name = name or "이름 없음"
#         self.age = age or 0
# u1 = User()
# print(u1.name, u1.age)

# u2 = User("윤지",33)
# print(u2.name, u2.age)

# #생성자는 객체 탄생 시 자동 실행되는 초기화 담당 메서드
# #주로 하는 일: 인스턴스 변수 초기화 , 필수 데이터 세팅, 준비작업
# #팁: 가능한 모든 속성을 생성자에서 미리 정의하면 코드 안정성이 높아진다.


# #---------------------------------------------------------------------------------
# #클래스 사용 --생성자를 활용
# #-------------------------------------------------------------------------------
# class Car : 
#     def __init__(self,model,power,max_s):
#         print("{} 인스턴스가 생성됩니다.".format(model))
#         self.model = model
#         self.power = power
#         self.max_speed = max_s
#     def drive_car(self, speed):
#         if self.power ==False:
#             print("주행불가 : 시동키세요")
#             return
#         if speed > self.max_speed:
#             print("{}의 최고속도는 {}km입니다. 속도 줄이세요".format(self.model,self.max_speed))

#             speed = self.max_speed
#         print("{}km로 주행합니다. 출발~".format(speed))


# car1=Car("BMW",False,200)
# car2 =Car("SONATA",True,180)
# car1.drive_car(180)



#----------------------------------------------------------------------
#변수와 메서드 종류
#--------------------------------------------------------------
'''
1. 클래스 변수
정의 : 클래스 전체에서 공유하는 변수
선안 위치 : 클래스 내부(메서드 밖)
접근 방법 : 클래스명.변수명 or 객체명.변수명
특징 : 모든 인스턴스가 같은 값을 공유

2. 인스턴트 변수
정의 : 인스턴스마다 개별적으로 유지되는 변수
선언위치:__init__안에서 self.변수명
접근방법: 객체명, 변수명
특징 : 객체마다 값이 다를 수 있음


    1.생성자에게 생성
        속성은 각 인스턴트가 태어날떄마다 각자 생성하는 인스턴스 변수
        즉, 생성자에서 만든 변수는 모든 인스턴스가 각자 자신만의 곡립된 변수를 가진다는 뜻
        같은 이름의 변수가 각각 인스턴스마다 만들어진다는 의미
    2.인스턴스 메서드에서 생성
        인스턴스 메서드 안에서 self.속성을 만들면, 그 메서드를 
        
        클래그 정의 밖, 인스턴스가 만들어진 뒤에
        작업 인스턴스 명 , 속성=값 형태로 속성을 추가하면 
        그 속성은 오직 그 인스턴스에만 추가됨
        
        
        
#         [메서드 종류]
#         . 인스턴스 메서드

# 정의: 객체가 호출하는 메서드

# 선언 방법: def 메서드명(self, ...)

# 첫 번째 매개변수: self

# 호출 방법: 객체명.메서드()

# 특징: 인스턴스 변수/메서드 접근 가능

# 2. 클래스 메서드

# 정의: 클래스 자체에서 호출 가능한 메서드

# 선언 방법: @classmethod 데코레이터 사용, def 메서드명(cls, ...)

# 첫 번째 매개변수: cls (클래스 자신을 의미)

# 호출 방법: 클래스명.메서드() 또는 객체명.메서드()

# 특징: 클래스 변수/클래스 메서드 접근 가능, 인스턴스 변수는 접근 불가

# 3. 정적 메서드

# 정의: 클래스와 인스턴스 모두에서 호출 가능하지만, 인스턴스/클래스 정보를 사용하지 않는 메서드

# 선언 방법: @staticmethod 데코레이터 사용, def 메서드명(...)

# 첫 번째 매개변수: 없음

# 호출 방법: 클래스명.메서드() 또는 객체명.메서드()

# 특징: 인스턴스 변수나 클래스 변수에 접근할 수 없음, 독립적인 기능 수행
        
        
        
        
# '''

# # #예제
# class Car:
#     wheels =4  #클래스 변수
#     def __init__(self,model):
#         self.model = model#인스턴스 변수
#         #인스턴스 메서드
#     def drive(self):
#         print(f'{self.model}주행시작!')
#     #클래스 메서드
#     @classmethod
#     def change_wheels(cls,count):
#         cls.wheels= count
#         print(f'바퀴 수를 {count}로 변경')
#     #정적 메서그 
#     @staticmethod
#     def car_info():
#         print("자동차는 이동 수단입니다.")


# #인스턴스 메서드
# car1 = Car("BMW")
# car1.drive()

# #클래스메서드 호출
# Car.change_wheels(6)
# print(Car.wheels)

# #정적 메서드 호출
# Car.car_info()

# #예제2
# class Car:
#     engine = '1000cc' #클래스 변수
#     @ classmethod#장식자(데코레이터): 이것을 작성행 클래스 메서드
#     def clsMethod(cls):
#         print("클래스 메서드")
#         cls.clsValue="클래스 변수"
#     def isertMathod(self):
#         print("인스턴스 메서드")

# #클래스 메서드 호출
# Car.clsMethod()# 인스턴스 생성 없이 생성 가능하다.
# print(Car.engine)#클래스명. 클래스 변수

# car1 =Car() #인스턴스 변수 생성
# car1.clsMethod()
# print(car1.engine)
# print("clsValue = ",Car.clsValue)
# #cls변수는 clsMethod()안에서 생성된다.
# car1.instMethod()#인스턴스 매서드 호출
# # Car.instanMethod()#오류! 인스턴스 매서드는 반드시 인스턴스 통해서 호출!
# car1.sunRoof = "썬 루프 옵션 추가"
# # print(Car.sunRoof)#오류!!
# #클래스명으로는 인스턴스메서드, 인스턴스 변수에 사용 불가능
# #----------------------------------------------
# #외부 접근 제어
# #------------------------------------------------------
'''
클래스 내부의 변수나 메서드에 외부에서 접근할 수 있는지 , 접근 못하게 한느지
>다른 언어 (C++,JAVA 등)처럼 public,private,producted 키워드가 있는것은 아니고,
네이밍 컨벤션 (이름 규칙) 과 언어 기능으로 접근 제어 흉내를 낸다.

외부 = 클래스가 정의된 코드 바깥

접근 수준 : 공개(public)
표기법:변수명
외부접근 가능 여부 : 가능
특징:기본 상태. 외부에서 자유롭게 접근 가능

접근 수준 : 보호(protected)
표기법:_변수명
외부접근 가능 여부 : 가능(권장 X)
특징:외부접근은 가능 하지만 , 내부에서만 사용하는 관례

접근 수준 : 비공개(private)
표기법:__변수명
외부접근 가능 여부:직접 접근 불가
특징:이름이 변경(mangling)되어 외부 접근 차단

'''

#예제)
class Myclass:
    def __init__(self):
        self.public_var ="공개 변수"
        self._protected_var = "보호 변수"
        self.__private_var = "비공개 변수"

    def get_private_var(self):
        return self.__private_var
obj = Myclass()#인스턴스 생성
print(obj.public_var)#접근 가능
print(obj._protected_var)#접근 가능. 관례상 내부에서만 사용
# print(obj.__private_var)#에러발생
print(obj.get_private_var())#이 처럼 볼 수 있다
'''
[특징]
파이썬은 완전한 접근 차단이 없기 떄문에 
__(더블 언더 스코어)로 시각하면 네임 맹글링이 적용되어
_클래스명__변수명으로 내부이름이 바뀜
@property와 같은 메서드를 써서 Getter/Setter를 구현하면 더 안전하게 관리 가능하다.

실무에서는  
public -> 기본상태, 자유접근 
_protected -> 내부전용(외부 접근이 가능하지만 하면 안됨)
__private-> 이름 충돌방지 외부 접근 차단 의도
진찌 중요한 값은 내부 메서드를 통해서만 노출 하는 것이 일반 적이다.
'''
#예제)
class Person:
    name="이몽룡"
    __addr="대구시 중구"
    def print_info(self):
        print("{}님은 {}에 거주중입니다.".format(self.name,self.__addr))
    def __print_info(self):
        print("{}님은 {}에 거주 합니다.".format(self.name,self.__addr))
    # #메서를 private로 해놓으면 외부에서 접근이 차단된다.
    # 다른 pubvlic메서드를 통한 private메서드우회 접속 가능.

    def print_info2(self):
        self.print_info()
        self.__print_info()

lee = Person
print(lee.name)
#print(lee.__addr) #private 변수로서 클래스 바깥코드에서 접근 불가!
# lee.print_info()
#lee.__print_info() #AttributeError 에러 발생 ! 메서드  마찬가지 private
                                    #외부접근 불가
# lee.print_info2()


#------------------------------------------
#상속
#----------------------------------------------------
'''
1.상속이란 
무언가를 물려 받는다.
기존에 있던 클래스(부모/슈퍼 클래스)의 속성과 메서드를 그대로 물려받아
코드 재사용과 확장이 가능 
-기반 클래스 : 부모 클래스, 슈퍼 클래스 
-파생클래스 : 지식 클래스, 서브 클래스

2. 특징
코드 재사용 > 부모의 기능을 그대로 사용
기능확장 > 부모 기능에 새로운 기능 추가 가능
기능변경(오버라이딩) > 부모 메서드를 재정의 가능
    >부모 클래스에 정의 된 메서드를 무시하고 자식 클래스에서 같은 이름으로 다시 정의 
is-a관계>'학생은 사람이다','고양이는 동물이다' 같은 관계일떄 적합


3. 클래스와 상속 문법'''
# class Parents:
#     def greet(self):
#         print("안녕하세요. 부모클래스입니다.")
# class Child(Parents): #부모 클래스(Parent)상속
#     pass

# c=Child() #객체 생성
# c.greet()

# # 4.오버라이딩(Overrriding)
# # 부모의 메서드를 자식이 같은 이름으로 다시 정의해서 덮어쓰기

# class Child(Paret): #부모 클래스 (Parent) 상속
#     def greet(self): #부모 greet() 재정의
#         print("안녕하세요. 자식 입니다.")

# c = Child() #객체 생성
# c.greet()


#5.super() 부모 메서드 호출
#부모의 원래 기능을 유지하면서 추가 기능을 넣을떄



class Parents:
    def greet(self):
        print("안녕하세요. 부모클래스입니다.")
class Child(Parents): #부모 클래스(Parent)상속
    def greet(self) :#부모 greet() 재정의
        super().greet() #부모 메서드 호출
        print("안녕하세요. 자식입니다.")

c=Child() #객체 생성
c.greet()

#6.상속의 종류
'''
단일 상속: 부모 1명만 상속 class A(B):
다중 상속 : 부모 여러명 상속 class A(B,C):
다단계 상속 : 부모 > 가직> 손자 형태
계층 상속 : 여러 자식이 하나의 부모를 상속'''

#예제 
#동물>개
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):#부모의 기본 메서드
        print(f'{self.name}가 소리를 냅니다.')
class Dog(Animal):
    def speak(self): # 오버라이팅
        print(f'{self.name}가 멍멍 짖습니다.')
#부모 클래스 인스턴스 생성
animal = Animal("동물")
animal.speak()

#자식 클래스 인스턴스 생성
dog = Dog("바둑이")
dog.speak()


#예제 ) super() 사용
#부모 클래스 
class Character:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp 
    def attack(self):
        print(f"{self.name}이 기본 공격을 합니다.!")
#자식 클래스
class Wizard(Character):
    def attack(self):
        super().attack()
        print(f'{self.name}가 화염구를 발사합니다.')
warrior = Character("전사",100)
warrior.attack()
mage = Wizard("마법사",80)
mage. attack()

#예제)
class Person:
    def __init__(self,name,age):
        print(Person,'생성자')
        self.name=name
        self.age=age

    def print_info(self):
        print("Person.printt_info")
        print("이름 : ",self.name)
        print("나이 : ",self.age)
    def sleep(self):
        print("Person, sleep")
        print(self.name + "남은 8시간 입니다.")
class Student(Person): #상속받을 클래스를  ()괄호안에 적는다.
    def study(self):
        print("Student, study")
        print(self.name + "학생은 6시간 잡니다.")
class Teacher(Person):
    def __init__(self,name,age):
        print("Teachar, 생성자")
        super()._init__(name,age) #부모클래스 생성지 호출
    def sleep(self):
        print("Teacher, sleep")
        super().sleep()#부모 클래스 메서드 호출
        print("선생님은 그렇게 많이 자지 않습니다.")
    def work(self):
        print("Teacher, work")
        print("Teacher, 선생님은 8시간 근무입니다.")
#부모 클래스 인스턴스 생성
print()
print()
print()
person = Person("홍길동",20)
person.print_info()
person.sleep()
print()
print()
print()
#자식 클래스 인스턴스 생성
student = Student("성춘향",18)
#Student Class에는 생성자를 만들지 않았지만,
#Person에서 상속 받아았기 떄문에
#Person에서 상속받았기 떄문에
#Person의 생성자가 호출 되었음.
# student.study()

# teacher = Teacher()

# print()
# print()
# print()
# teacher = Teacher("이몽룡",27)
# teacher.sleep()
# teacher.work()
# teacher.print_info()
#--------------------------------------------------
#추상클래스
#-----------------------------------------------------
'''
정의:
추상클래스(Abstrack Class)는 객체를 직접 만들 수 없는 
클래스로, 자식 클래스에서 반드시 구현해야하는 추상메서드를 
포함하고 있는 메서드이다.

동물이라는 클래스를 정의하며, 동물은 '운다'라는 추상적인 개념만
정의해놓고 각 동물들이 실제로 어떻게 우는지는 각자 정의하도록 (자식클래스)하는 것




이따 운다 라는 메서드를 추상메서드라고 한다.
추상메서드는 자식 클래스가 '반드시'정의 해야 한다.
추상메서드가 있는 클래스다 추상 클래스


목적:
이클래스의 시작들은 반드시 이런 메서드를 구현해야한다한다라는 규칙
(인터페이스)를 강제하기위해 사용한다. 즉, 부모가 설계도 역활을 하고,
자식이 그 설계도대로 내용으ㅏㄹ 채우는 것.

특징:
1.인스턴스 생성 불가
추상클래스는 직접 객체를 만들 수 없음
상속받은 자식 클래스에서 모든 추상메서드를 구현해야 객체 생성 가능
2. 추상 메서드 포함
메서드 선언만 있고,구현(내용)이 없는 메서드
3.abc모듈 사용
파이썬에서 추상 클래스는  abc(Abstrack Base Class)모듈로 만든다.
4.규칙정제
게발자들이 공통적인 메서드 이름과 매게변수를 지키도록 강제함
[사용방법]
from abc import ABC,abstractmethod
class 추상클래스 명(ABC):#ABC를 상속
    @abstractmethod
    def 추상메서드 명(self):
        pass
'''

from abc import ABC, abstractmethod

# 추상 클래스
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 자식 클래스
class Dog(Animal):
    def speak(self):  # @abstractmethod 제거
        print("멍멍")

# 자식 클래스2
class Cat(Animal):
    def speak(self):
        print("야옹")

dog = Dog()
cat = Cat()
dog.speak()  # 멍멍
cat.speak()  # 야옹