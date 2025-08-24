def check_even_odd():
    a=int(input("정수를 입력하세요"))
    if a%2==0:
        print("짝수")
    else:
        print("홀수")
check_even_odd()

def  calculate_bmi():
    kg,m=map(float,input("사용자의 체중(kg) 키(m)를 입력 (예시 68 1.79)").split())
    print(f'bmi수치는 {kg/m**2}')

calculate_bmi()

def find_max():
    c=-99999999999999999999999999999999999999999999999999
    a=list(map(int,input("숫자로 이루어진 리스트를 입력").split()))
    for i in a:
        if i>c:
            c=i
    print(f'최대값:{c}')

find_max()

def calculate_parking_feea(a):

    if a<=30:
        return "1000원"
    else:
        return (a-10)//10*1000+1000


a=int(input("주차 시간을 분 단위로 입력"))
print(f"총요금{calculate_parking_feea(a)}")