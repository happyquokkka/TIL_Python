# function_dic.py

# 다음과 같은 함수를 포함하는 프로그램 작성
# 함수명 : show_info()
# 이름, 학년, 나이, 연락처를 전달 받아서
# 딕셔너리로 만들어 출력

# 빈 딕셔너리 만들기
info = {}

# 함수 정의
def show_info() :
    name = input('이름: ')
    year = input('학년: ')
    age = input('나이: ')
    phone = input('연락처: ')
    info['name'] = name
    info['year'] = year
    info['age'] = age
    info['phone'] = phone
    print(info)

show_info()
