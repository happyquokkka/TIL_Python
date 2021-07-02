# function_ret_param_ex2.py

def get_interest() :
    deposit = int(input('예금액 입력 : '))
    int_rate = float(input('이자율 입력(%) : '))
    interest = deposit * int_rate * 0.01
    print('이자액 :', format(int(interest),','),'원')

get_interest()


## 선생님 풀이

# 함수 정의

def get_interest(deposit, int_rate) :   # 매개변수
    interest = deposit * int_rate / 100
    return int(interest)    # 정수형으로 반환

# 함수 호출 테스트
dps = int(input('예금액 입력 : '))
rate = float(input('이자율 입력(%) : '))

inter = format(get_interest(dps, rate),',')     # 이자액 계산 / inter 변수는 문자열

print('이자액 : %s원' % inter)


