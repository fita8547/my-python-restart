'''
문자열 인덱싱
>indexing: index 색만. 무언가를 가리킨다
>문자열에서 특정글자를
뽑아내며 사용하는 것.
>특정글자를 찾을때 순서를 사용 -> 인덱스
>순서는 항상 0부터
>음수는 뒤에서 부터 순서를 센다-1부터
'''
my_str="동해물과 백두산이 마르고 닮도록"
print(my_str)
print(my_str[0])
print(my_str[1])
print(my_str[2])
print(my_str[-1])
print(my_str[-2])



'''
문자열 슬라이싱
> slicing:조각내다.
>인덱스를 이용해서 특정범위의 문자를 조각내서 사용한다
>콜론으로  범위지정 
my_str[시작인덱스: 끝인덱스]
my_str[시작인덱스:]:시작부터 끝까지
my_str[:끈 인덱스]:처음부터 인덱스 끝까지
my_str[:]: 시작부터 끝==my_str'''
print(my_str[0:4])#처음과 끝 인덱스 범위를 지정해서 출력
print(my_str[5:])
print(my_str[:20])#슬라이싱은 인덱스 범위를 초과해도 오류발생하지 않는다.
# print(my_str[20])#인덱스는 범위안에 없는 인덱스 번호를 초과해도 오류발생하지 않는다
#my_str 문자중에 첫글자를 다른 문자로 바꾸고 싶다면 오류 발생
#이미 만들어진 문자열은 수정할 수 없다.
new_my_str="하"
new_my_str="하"+my_str[1:]
print(new_my_str)


#[문제1]
print(1,2,3,4,5,sep=">")#한줄로 수정함

#[문제2]
A=10 ;B="5"
print(A+int(B))

#[문제3]
text="I love Python";print(text[2:6])

#[문제4]
text="DataScience20251"
arr1=text[0]+text[4]
print(arr1)