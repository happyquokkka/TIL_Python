# 06_function_dict반환예제

# 함수 정의
# 함수 이름 : get_info()
# 함수 기능 : 사용자로부터 이름과 나이를 입력받아 딕셔너리로 저장하고
# 저장된 딕셔너리 데이터를 반환하는 함수

def get_info() :
    name = input('이름 입력 : ')
    age = input('나이 입력 : ')
    student = {'name':name, 'age':age} # 딕셔너리 만들기
    return student  # 딕셔너리 반환

# 함수 테스트 :
# 함수를 호출하여 반환값을 변수 student_info 에 저장하고
# 저장된 변수값을 출력/ 변수의 형태를 확인

student_info = get_info()
print(student_info)
print(type(student_info))

# 함수 호출 했을 때 결과가 반환되는 함수면 결과값이 호출 함수 이름 위치로 반환되고
# 반환된 값을 변수에 저장해 출력 해 볼 것
total = sum()
print('sum() 함수를 호출해서 반환받은 값은 %d 입니다' % total)

print('sum()함수를 호출해서 반환받은 값을 바로 출력합니다 그 값은 %d 입니다' % sum())

# 반환값이 없는 경우 변수에 저장하면 ????
def show() :
    print('안녕하세요.') # return문이 없는 함수

show()  # 안녕하세요.
result = show() # 안녕하세요.
print(result)   # None
print(show())   # 안녕하세요.

# 반환값이 없는데 변수에 저장하거나 함수 호출 결과를 출력하라고 하면 => None이 저장되거나 출력됨
