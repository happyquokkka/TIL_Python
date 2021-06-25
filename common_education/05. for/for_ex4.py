# for_ex4.py

# 카운트다운 프로그램

start = int(input('시작 숫자를 입력하시오: '))
for n in range(start, 0, -1) :
    print(n, end=" ")
print ("발사", end="")

## 선생님 풀이
count = int(input('시작 숫자를 입력하시오: '))
for x in range(count, 0, -1) :
    print(x, end=" ")
print('발사')
