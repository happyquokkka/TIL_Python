# 05_if_ex4.py

## 선생님 풀이 [연습문제]
# 정수 3개를 입력 받아서 제일 큰 수 출력
# 1. 정수 3개 입력받아 변수에 저장
num1 = int(input("정수 1 입력: "))
num2 = int(input('정수 2 입력: '))
num3 = int(input('정수 3 입력: '))




# 2. 저장된 3개의 변수 중 제일 큰 수를 판별
# num1 이 가장 큰 경우 : num1 > num2 and num1 > num3
if (num1 > num2) and (num1 > num3) :
    print('제일 큰 수: ', num1) # 3. 판별된 제일 큰 수 출력

# num1 이 제일 큰 수가 아니면 : num2 > num3 => num2가 가장 큰 수
elif num2 > num3 :  # 첫 번째 if가 참이 아닌 경우 elif 조건문으로 내려옴
    print('제일 큰 수: ', num2) # 3. 판별된 제일 큰 수 출력

# num2가 제일 큰 수가 아니면 : num3이 가장 큰 수
else :
    print('제일 큰 수: ', num3) # 3. 판별된 제일 큰 수 출력


