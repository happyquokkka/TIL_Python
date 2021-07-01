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
