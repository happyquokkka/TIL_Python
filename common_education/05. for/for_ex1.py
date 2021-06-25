# for_ex1.py

# 정수 2개를 입력 받아서 두 수 사이의 합을 구하는 프로그램 작성 (for문 사용)

num1 = int(input('숫자 1 입력: '))
num2 = int(input('숫자 2 입력: '))
sumn = 0
for x in range(num1, num2+1) :
    sumn += x
print('%d부터 %d까지 누적 합:' % (num1, num2), sumn)

## 선생님 풀이
# 정수 2개 입력 받기
num1 = int(input('숫자 1 입력: '))
num2 = int(input('숫자 2 입력: '))

sumx = 0  # 누적변수 초기화 하기

for x in range(num1, num2+1) :
    sumx += x
print("%d 부터 %d 까지의 합 : %d" % (num1, num2, sumx))
