# function_ret_param_ex2.py

def get_interest() :
    deposit = int(input('예금액 입력 : '))
    int_rate = float(input('이자율 입력(%) : '))
    interest = deposit * int_rate * 0.01
    print('이자액 :', format(int(interest),','),'원')

get_interest()