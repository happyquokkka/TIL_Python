# 15_function_keyward_args

# 키워드 인수 예제

# 학생 정보를 입력받아 학생 dict를 구성하여 반환하는 함수
def student_info(name, age, gender) :
    student = {
        'name' : name,  # "name"이라는 key에 대응하는 변수는 name
        'age' : age,    # 'age'라는 key에 대응하는 변수는 age
        'gender' : gender  # 'gender'라는 key에 대응하는 변수는 gender
    }
    return student

# 함수 테스트
# 함수 호출 시 인수를 넘겨 dict가 제대로 구성되어 반환되는지 출력
print(student_info(name="kim",gender="여",age=23))   # 키워드 인수
print(student_info('lee',20,'남'))   # 위치 인수
print(student_info('park',gender='여',age=25)) # 위치 인수와 키워드 인수 동시 사용

### 주의 !
# print(student_info(gender='남', age=22, 'lee')) / 위치인수는 키워드 인수 앞에 위치해야 함!!!
# SyntaxError: positional argument follows keyword argument

