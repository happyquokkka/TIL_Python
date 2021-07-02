# function_return_ex2.py

def get_area() :
    num1 = int(input('가로길이 입력 : '))
    num2 = int(input('세로길이 입력 : '))
    area = num1 * num2
    print('사각형의 면적 : ', area)

get_area()


## 선생님 풀이

def get_area() :
    width = int(input('가로길이 입력 : '))
    height = int(input('세로길이 입력 : '))
    # 사각형 면적 계산
    area = width * height
    return area # 결과값 반환 : return width * height / 계산이 긴 경우에는 변수 지정해서 변수를 리턴하기

rect_area = get_area()
print('사각형의 면적 : %d' % rect_area)

