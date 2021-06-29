# while_ex3.py

# 사용자에게 숫자(정수)를 입력받아
# 홀수이면 '숫자는 홀 수 입니다.' 출력
# 짝수이면 출력 없이 다음 입력을 받는 프로그램을 작성.
# 종료는 입력에 x 문자가 들어오면 종료하되 break문 활용
# 짝수일 경우 출력 건너뜀은 continue 문 활용

num = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
while int(num) % 2 != 0 :
    print('%d는 홀 수 입니다.' % int(num))
    break
    if int(num) % 2 == 0 :
        continue
    elif num == "x" :
        break
print('종료합니다')























# num = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
# while num % 2 != 0 :
#     print('%d는 홀 수 입니다.' % num)
#     if num % 2 == 0 :
#         continue
#     print(num)
#     elif num == "x" :
#         break
#     print('종료합니다')


# 선생님 풀이
#
# while True :
#     s = input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
#     if s == 'x' :
#         print('종료합니다.')
#         break
#     if int(s) % 2 == 0 :
#         continue
#
#     print(s + '는 홀수입니다.')


