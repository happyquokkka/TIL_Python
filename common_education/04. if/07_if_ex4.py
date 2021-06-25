# 07_if_ex4

a = int(input("정수 1 입력 : "))
b = int(input("정수 2 입력 : "))
c = int(input("정수 3 입력 : "))

if (a > b) and (a > c) :
    print("제일 큰 수: ", a)
elif b > c :
    print("제일 큰 수: ", b)
else :
    print("제일 큰 수: ", c)
