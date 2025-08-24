'''
문제 1] 사용자에게 쉼표로 구분된 단어들을 입력받아, 마지막 요소만 출력하시오.
입력 예시: apple,banana,grape
출력 예시: grape
'''
a=list(input("과일을 입력해라").split(","))
print(a[-1])
'''
문제 2] 아래 딕셔너리에서 "banana" 키가 있는지 확인하고 결과를 출력하시오.
fruits = {"apple": 1, "grape": 3}
출력 예시: False
'''
fruits = {"apple": 1, "grape": 3}
print("banana" in fruits)
'''
문제 3] 기존 리스트에 사용자가 입력한 숫자를 추가하고 출력하시오.
lst = [1, 2, 3]

입력 예시: 5
출력 예시: [1, 2, 3, 5]
'''
lst = [1, 2, 3]
num=int(input("숫자를 입력하세요."))
lst.append(num)
print(lst)
'''
문제 4] 튜플로 요일 출력하기(튜플에 인덱스로 접근)

입력 : 요일 번호(0~6)를 입력하세요 :
출력결과 : 오늘은 월요일입니다.
'''
days=int(input("요일 번호(0~6)를 입력하세요 :"))
arr = ("월요일","화요일","수요일","목요일","금요일","토요일","일요일")
print(arr[days])

'''
문제 5] 아래 딕셔너리에서 "math" 점수를 사용자 입력으로 변경하고 출력하시오.
score = {"math": 80, "english": 90}

입력 예시: 95
출력 예시: {'math': 95, 'english': 90}
'''
score = {"math": 80, "english": 90}
num=int(input(" 'math' 점수를 사용자 입력으로 변경하고 출력하시오."))
score["math"] = num
print(score)
'''
문제 6] 아래 딕셔너리 정보를 이용해 "이름은 Yoonji이고, 나이는 36살입니다."를 출력하시오.
(문자열 포멧 이용)

info = {"name": "Yoonji", "age": 36}
'''
info = {"name": "Yoonji", "age": 36}
print(f'이름은 {info["name"]}이고, 나이는 {info["age"]}살입니다')

