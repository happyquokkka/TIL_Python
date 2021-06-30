# list_append_ex5.py

# 상품을 리스트에 추가
# 엔터키 누르면 입력이 종료되고, 등록된 상품 리스트 출력
# 입력값을 ""와 비교해서 같으면 종료되게 구성

product = []
while True :
    customer = input('상품 등록 (엔터키 누르면 종료) : ')
    product.append(customer)
    if customer == "" :
        break
print('등록된 상품 : ', product)
