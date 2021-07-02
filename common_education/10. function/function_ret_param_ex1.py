# function_ret_param_ex1.py

# 사칙연산 함수 작성
def add(num1, num2) :
    total = num1+num2
    print('%d + %d = %d' % (num1, num2, total))

add(9,3)

def sub(num1, num2) :
    total = num1-num2
    print('%d - %d = %d' % (num1, num2, total))

sub(9,3)

def mul(num1, num2) :
    total = num1*num2
    print('%d * %d = %d' % (num1, num2, total))

mul(9,3)

def div(num1, num2) :
    total = num1/num2
    print('%d / %d = %d' % (num1, num2, total))

div(9,3)


## 선생님 풀이

def add(a,b) :
    return a+b

def sub(a,b) :
    return a-b

def mul(a,b) :
    return a*b

def div(a,b) :
    return a/b

# 함수 호출 테스트

x=9
y=3

print('%d + %d = %d' % (x,y, add(x,y)))
print('%d - %d = %d' % (x,y, sub(x,y)))
print('%d * %d = %d' % (x,y, mul(x,y)))
print('%d / %d = %d' % (x,y, div(x,y)))


