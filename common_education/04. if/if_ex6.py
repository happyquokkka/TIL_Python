# if_ex6.py

# 상품번호 입력 시 1,2 이외의 숫자 입력하면 프로그램 종료
# 할인액
 # 주문액이 100만원 이상 - 10%
 # 주문액이 50만원 이상 100만원 미만 - 5%
 # 주문액 50만원 미만 - 할인 없음

pc_price = 1200000
dc_price = 400000


print('*******상품 정보*******')
print('1 노트북: 1,200,000 원')
print('2 디지털카메라 : 400,000 원')
print("*************************")
choice = int(input('상품번호 입력 : '))
ea = int(input('주문 수량 입력: '))
print("")
if choice == 1 :
    print('*******주문 내용*******')
    print('상품명:    노트북')
    print('가격 :     1,200,000 원')
    print('주문 수량 : %d' % ea)
    print('주문액 : %s 원' % format(int((ea*pc_price)), ','))
    if (ea*pc_price) >= 1000000 :
        a = ea * pc_price * 0.1
        print('할인액 : %s 원' % format(int(a), ','))
        print('총지불액: %s 원' % format(int((ea * pc_price)-a),','))

    elif (ea*pc_price) >= 500000 :
        b = ea * pc_price * 0.05
        print('할인액 : %s 원' % format(int(b)), ',')
        print('총지불액: %s 원' % format(int((ea * pc_price)-b),','))

    else :
        print('할인액 : 0 원')
        print('총지불액: %s 원' % format(int((ea * pc_price)-0),','))

elif choice == 2 :
    print('*******주문 내용*******')
    print('상품명:    디지털카메라')
    print('가격 :     400,000 원')
    print('주문 수량 : %d' % ea)
    print('주문액 : %s 원' % format(int((ea*dc_price)), ','))
    if (ea*dc_price) >= 1000000 :
        a = ea * dc_price * 0.1
        print('할인액 : %s 원' % format(int(a),','))
        print('총지불액: %s 원' % format(int((ea * dc_price)-a),','))
    elif (ea*dc_price) >= 500000 :
        b = ea * pc_price * 0.05
        print('할인액 : %d 원' % format(int(b)),',')
        print('총지불액: %s 원' % format(int((ea * dc_price)-b),','))
    else :
        print('할인액 : 0 원')
        print('총지불액: %s 원' % format(int((ea * dc_price)-0),','))
else :
    print('잘못 입력하였습니다. 종료합니다.')
