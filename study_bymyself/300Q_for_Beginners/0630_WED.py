# 0630_WED.py

# 071. my_variable 이름의 비어있는 튜플을 만들어라.

my_variable=tuple()
print(type(my_variable))

print('--------------------------------')

# 072. 영화 제목을 movie_rank 이름의 튜플에 저장하라.

movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

print('--------------------------------')

# ★ 073. 숫자 1이 저장된 튜플을 생성하라.

random = (1,)
print(random)

print('--------------------------------')

# 074. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.

t = (1,2,3)
# t[0] = 'a'    TypeError: 'tuple' object does not support item assignment
# 오류 발생 원인: 튜플 내 값은 변경 불가능함.

print('--------------------------------')

# 075. 아래와 같이 t 에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?

t = 1,2,3,4
# t는 튜플
print(type(t))

print('--------------------------------')

# 076. 변수t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정하라.

t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
# 튜플 내 원소값은 수정이 불가해서 다시 정의함.

print('--------------------------------')

# ★ 077. 다음 튜플을 리스트로 변환하라.

interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)

print('--------------------------------')

# 078. 다음 리스트를 튜플로 변경하라.

interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data)

print('--------------------------------')

# ★ 079. 튜플 언팩킹 ㅡ 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'bannana', 'cake')
a, b, c = temp
print(a, b, c)
# ('apple', 'bannana', 'cake') 로 출력될 것임
# 아니다!!!!!! apple bannana cake 으로 출력됨. 튜플 내 각각의 원소가 튜플 밖으로 빠져나옴

print('--------------------------------')

# ★ 080. range 함수 ㅡ 1부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.

data = tuple(range(2, 100, 2))
print(data)

# 내가 풀려고 했던 방식
tuple = tuple()
for i in range(1,100) :
    if i % 2 == 0 :
        tuple.add(i)    # AttributeError: 'tuple' object has no attribute 'add'
print(tuple)

# S1 = {}   / 빈 딕셔너리
# s2 = set()    / 빈 집합
# 빈 튜플은 어차피 튜플이 수정이 불가하니 쓸모 없음!