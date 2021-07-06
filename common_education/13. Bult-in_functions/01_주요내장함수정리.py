# 01_주요내장함수정리.py

# 내장함수

# abs(x) : x의 절댓값을 반환
print(abs(-10))


print('==all()==')
# all(iterable) : 모든 요소가 참이면 True, 아니면 False 반환
# False : 0, True : 0 이 아닌 모든 값
# 즉, 0이 하나라도 있으면 False 반환!

# iterable : 각각의 요소를 하나씩 반환할 수 있는 객체 / for문으로 반복해서 출력이 가능한 자료형
# 자료형의 예시 : 리스트, 튜플, 집합, 딕셔너리 (for 문 뒤에 붙여서 슬 수 있는 자료형)

print(all([1,2,3]))      # True
print(all([0,1,2,3,4]))  # False


print('==any()==')
# any(iterable) : 하나라도 참이면 True, 모두 거짓이면 False 반환
# 전부 0이면 False
print(any([0,0,0])) # False
print(any([0,1,0])) # True
print(any([0,"",[]]))   # 0, 빈 문자열, 빈 리스트 ㅡ False
                        # 0도 False지만, 빈 문자열과 빈 리스트 역시 False 이다


print('==chr()==')

# chi(i) : 아스키(ASCII)코드 값에 해당하는 문자 반환
print(chr(65))  # A
print(chr(97))  # a
print(chr(13))  # enter키

for i in range(65,100) :
    print(chr(i))

print('===ord()===')

# ord(c) : chr과 반대로 문자에 해당되는 아스키 코드값을 반환
print(ord('a'))     # 97
print(ord('0'))     # 48
print(ord('\n'))    # 10
print(ord(' '))     # 32 : space
print(ord('\r'))    # 13 : enter

print('===divmod()===')
# divmod(a,b) : a를 b로 나눈 몫과 나머지를 튜플 형태로 반환환print(divmod(7,3))

print('==enumerate()==')
# enumerate(iterable, start=0)
# 시퀀스 형태의 값을 넘겨주면 index 값을 포함하는 enumerate 객체로 반환
# (리스트, 튜플, 문자열, range) -> 인덱스값, 실제값

# ['a', 'b', 'c'] => 0'a' 1'b' 2'c'

# enumerate 객체 반환 <enumerate object at 0x0000029A37A994C0>
print(enumerate(['kim','Lee','Park']))

# 보통 for문을 사용하여 인덱스 값을 확인함
for i, name in enumerate(['kim','Lee','Park']) :
    print(i,name)

# index 와 값을 나타내는 변수명은 임의로 사용 가능
for k, name in enumerate(['kim','Lee','Park']) :
    print(i,name)

# for 문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 사용하는 함수

print('==eval==')
# eval(expression) : 표현식의 연산 결과 반환
print(type(eval('10')))
print(type(eval('10.5')))

print(eval('1+2'))  # 수식을 표현한 문자열을 실제 식으로 변환 후 연산 결과를 반환

print('==filter==')
# filter(function, iterable) : 반복 가능한 자료형 요소들이
# function에 입력되었을 때 반환값이 참인 것만 묶어서(걸러내서) 반환

# 양수만 반환하는 함수
def positive(x) :
    return x > 0   #  함수 반환 결과가 True/False

print(filter(positive, [0,-1,5,-7,10])) #<filter object at 0x0000022B2D56B910> filter 객체 반환
print(list(filter(positive, [0,-1,5,-7,10])))   # 양수만 골라서 리스트로 반환

# 짝수만 반환
def even_number(x) :
    if x%2 == 0 :
        return x

print(list(filter(even_number, [1,2,3,4,5,6,7,8,9])))

print('==help()==')
# 내장 도움말 시스템을 호출
help(print)
help(sum)

print('===hex()===')
# hex() : 정수를 "0x" 접두사가 붙은 소문자 16진수 문자열로 반환
print(hex(7))   # 이 때 반환되는 값은 숫자가 아니라 문자
print(hex(10))
print(hex(1234))

print('==map()==')
# map(function이름, iterable) : iterable 각 요소가 함수 function에 의해 수행된 결과 반환

def increase(x) :
    return x+1
print(map(increase,[1,2,3,4,5]))
print(list(map(increase,[1,2,3,4,5])))

print('===open()===')
# 외부 파일을 사용하기 위해 접근 경로를 생성하는 함수(파일이 없으면 만들고 있으면 해당 파일을 열어줌)
file_write = open('my file.txt','w')

print('==round()==')
# 실수를 반올림하여 반환
# round(number[,ndigits]) : ndigits - 소수 이하 자릿수에 해당
print(round(3.14592,2))     # 3.142

print('==zip()==')
# zip(iterable, iterable1, ...)
# 각 iterable에서 동일한 인덱스의 요소를 추출하여 튜플 형태로 묶어서 반환
print(zip([1,2,3],[4,5,6]))  # <zip object at 0x0000026583F25200>
print(list(zip([1,2,3],[4,5,6])))   # [(1, 4), (2, 5), (3, 6)]
# 짝을 만들 수 있는 요소만 짝은 만들어서 반환
print(list(zip([1,2,3], [4,5])))    # [(1, 4), (2, 5)]
# 문자열도 iterable
print(list(zip('123','abc')))   # [('1', 'a'), ('2', 'b'), ('3', 'c')]

# zip 함수를 사용해서 튜플로부터 딕셔너리 생성하는 예제
keys=('apple','pear','peach')
vals = (300,250,400)

result= dict(zip(keys,vals))
print(result)

print('===sum()===')
# sum(iterable) : iterable의 모든 요소의 합 반환
print(sum([1,2,3,4,5]))
print(sum((1,2,3,4,5)))
