# 파일을 여러 개 사용하는 이유: 나중에 복습할 때 찾기가 어려워짐
# 변수는 대입해놓고 사용하지 않으면 메모리 공간을 차지하게 됨 -> 프로그램 성능이 떨어짐
# 변수 삭제 명령어 : del
# del 변수명

# c_var = 100
# print(c_var)
# del c_var
# print(c_var)  # 변수를 삭제했기 때문에 NameError 발생

# 블럭을 잡아서 주석처리 할 때는 ctrl + / 누르면 전체가 다 주석처리가 됨(=실행이 안 됨)

# 문자열 값 저장
# 문자열은 큰따옴표를 사용하는 것을 원칙으로 한다... (작은따옴표도 사용 가능)
# 여러 종류의 따옴표를 사용시에는 짝을 맞춰야 함 (갯수와 종류, 시작과 끝 맞추기)

name = "홍길동"
std_name = '김철수'
pro_name = "이몽룡'교수'"

print(name)
print(std_name)
print(pro_name)

print(name, std_name, pro_name)

address = '서울시 강남구'
# ㅇㅇㅇ 은 xxxx 에 삽니다로 출력하고 싶음
# 문자열을 연결하는 작업을 할 때 : + 연산자를 사용함

print(name, address)
print(name+address)  # 위는 문자열 두 개 출력, 아래는 문자열 하나만 출력

print(name+"은 "+address+'에 삽니다.')

result = name+"은 "+address+'에 삽니다.'  # 변수의 값은 식이 될 수도 있다!
print(result)

## 문자와 숫자의 결합(연결)

age = 23
# print(name + '은 ' + age + '살 입니다') #홍길동은 23살 입니다  -> 결합의 의미로 쓰임
# print(5 + age) -> 정수와 정수끼리는 더하기 연산

# 값은 숫자형이지만 문자열로 처리해야 할 때는 일시적으로 형태(type)를 변경함 = 일시적인 형변환
# 숫자 -> 문자:  str(변수명)

print(name + '은 ' + str(age) + '살 입니다')


## 사각형의 면적을 구해서 출력하는 프로그램
# 넓이 : 100
# 높이 : 200
width = 100
height = 200

area = width * height

print("면적 :"+str(area)) #하나의 문자열만 출력

print("면적 :",area) #두개의 문자열을 출력... 따라서 숫자를 문자로 바꾸지 않아도 됨(결합이 아니니까)










