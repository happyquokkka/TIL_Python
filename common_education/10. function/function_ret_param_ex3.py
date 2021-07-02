# function_ret_param_ex3.py

def order() :
    price = int(input('상품 가격 입력 : '))
    qty = int(input('주문 수량 입력 : '))
    print('--------------------------------')
    amount = price * qty
    print('주문액 : %d원' % amount)
    if amount >= 100000 :
        discount = amount * 0.1
    elif amount >= 50000 :
        discount = amount * 0.05
    else :
        discount = 0
    print('할인액 : %d원' % discount)
    total = amount - discount
    print('지불액 : %d원' % total)

order()
