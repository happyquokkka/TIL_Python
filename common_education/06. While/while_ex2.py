# while_ex2.py

num = int(input('마지막 숫자를 입력하세요: '))
sum = 0
i = 0
while i <= num : # 1부터 마지막 수까지 해당할 때
    if i % 2 == 1 : # 홀수라면
        sum += i  # 초기변수를 1부터 누적합
    i += 1
print('1부터 %d까지 홀수의 합은 %d입니다' % (num, sum))


# 선생님 풀이

# su = int(input('마지막 숫자를 입력하세요 : '))
#
# i = 0  # 초기변수
# sum = 0  # 누적변수
#
# while i <= su:
#     i += 1
#     if i % 2 == 1 : # 홀수인지 확인
#         sum += i
#
# print('1부터', su, '까지 홀수의 합은', sum, '입니다')
