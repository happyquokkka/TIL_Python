# 08_reit_if(me)

num = int(input('번호 입력(1. 현금, 2. 카드): '))

if num == 1 :  # 현금이나 카드 선택
    # 결제수단에 따라 할인율 계산
    pay = int(input('지불액 입력: '))
    print('할인율 : 10%')
    print('할인액 : %d' % (int(pay * 0.1)) + '원')
elif num == 2 :  # 카드면
    pay = int(input('지불액 입력: '))
    print('할인율: 5%')
    print('할인액 : %d' % (int(pay * 0.05)) + '원')
else :
    print('잘못 입력했습니다. 종료 합니다.')