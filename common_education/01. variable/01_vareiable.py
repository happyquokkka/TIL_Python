# 변수에 값 저장
# 변수 = 값
result = 10
print(result)
result = 'a'

print(result)

# 여러개의 변수에 여러개의 값을 한 번에 저장 가능
# 변수1, 변수2, 변수3, ... =(assignment) 값1, 값2, 값3, ... 동적 타이핑이 가능하기 때문에.
# 파이썬 코드는 맨 앞부터 시작하는 것이 원칙(띄어쓰기 하면 안 됨)

a, b, c, d = 1, 2, 3, 4
print(a)
print(b)
print(c)
print(d)

#
e, f, g = a, b, c

# 변수이름 = 값이나 혹은 값이 들어있는 식별자
a = b # b변수의 참조값이 a에 저장
# 변수의 값을 교환 (스와핑) -> 파이썬에서만 가능
a, b = 10, 20 # a,b의 값은? a는 10, b는 20
a, b = b,a # a, b의 값은? a는 20, b는 10

print(a,b)





