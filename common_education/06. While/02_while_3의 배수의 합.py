# 02_While_3의 배수의 합.py

# 1부터 100 사이의 모든 3의 배수의 합을 while 문을 이용해서 코드 작성
# 누적변수 필요
sum = 0
# 초기값
num = 1

while num <= 100 : # 조건
    # num 이 3의 배수인지 확인
    if num % 3 == 0 :
        sum += num
    num = num+1  # num은 1부터 100까지 1씩 증가하는 수

print('1부터 100까지의 모든 3의 배수의 합은 %d 입니다.' % sum)
# 최종 num의 값은 얼마인가?
print('반복 후 num의 값은', num, '입니다')
