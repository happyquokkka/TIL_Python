# 18_global_variable2.py

# 전역변수를 함수 내부에서 변경하려면? global 키워드 사용

a = 1   # 함수 밖에서 정의된 전역변수 a

def add() :
    global a    # a변수는 전역변수고 함수 내에서 수정할 수도 있다는 키워드 / 지역변수와 전역변수의 충돌 막음
    a = a+1     # 전역변수 a의 값이 바뀐다 (global 키워드 때문에)
    c = a+b
    # print(a)
    # print(b)
    # print(c)

b = 3   # 함수 밖에서 정의된 전역변수 b ㅡ 함수 정의 후 생성되어도 함수 내에서 사용 가능

print('add 함수 호출 전 :', a)
add()                               # add() 함수 호출 후 print(a)를 진행
print('add 함수 1번 호출 :', a)
add()                               # add() 함수를 호출할 때마다 전역변수 a의 값이 변경되고 있음
print('add 함수 2번 호출:', a)       # 3