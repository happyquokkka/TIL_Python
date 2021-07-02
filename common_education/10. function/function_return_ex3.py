# function_return_ex3.py

def order() :
    price = int(input('상품가격 입력 : '))
    ea = int(input('주문수량 입력 : '))
    total = ea * price
    print('----------------------')
    print('상품가격 :',price,'원')
    print('주문수량 :', ea,'개')
    print('주문액 :', total,'원')

order()

## 선생님 풀이

def order() :
    pr = int(input('상품가격 입력 :'))
    qt = int(input('주문수량 입력 :'))
    amt = qt * pr
    return pr, qt, amt  # 튜플 형태로 변환

# 함수 호출
price, qty, amount = order()

print('-----------------------')
print('상품가격 : %d원' % price)
print('주문수량 : %d개' % qty)
print('주문액 : %d원' % amount)