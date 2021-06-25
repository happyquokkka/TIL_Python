# 07_reit_if.py

# 사과 상태가 어떤지 확인해서 신선하면 사과를 산다
# 단 사과를 살 경우에 가격이 1000원 미만이면 10개를 사고 아니면 5개를 산다

# 사과 상태 입력 받기
apple_quality = input("사과 상태 입력 : ") # 신선이 들어오면 사과를 산다

# 사과를 살 건지 결정
if apple_quality == "신선" :
    # 사과를 산다
    # 사과 가격 입력 받기
    apple_price = int(input('사과 가격 입력: '))
    if apple_price < 1000 :
        print('10개를 산다')
    else :
        print('5개를 산다')
else :
    # 사과를 사지 않는다
    print("사과를 사지 않는다")


