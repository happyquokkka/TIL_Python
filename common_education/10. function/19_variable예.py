# 19_variable예제.py

def sub(x,y) : # 매개변수 x,y -> 지역변수 x -> 3, y -> 4
    global a

    a=7 # 전역변수 a가 7로 수정
    x,y = y,x   # x와 y는 지역변수를 사용 : x-> 4, y -> 3
    b=3         # 지역변수 정의
    print(a,b,x,y)  # 출력되는 값 예측 : 7, 3, 4, 3

a,b,x,y=1,2,3,4     # a, b, x, y -> 전역변수
sub(x,y)
print(a,b,x,y)      # 출력되는 값 예측 : a -> 7, b -> 2, x -> 3, y - > 4
                    # 7, 2, 3, 4

# 전역변수 a가 생성되어 있어도 지역변수 a를 생성해서 함수 내부에서만 사용할 수 있다



#####

def test(a,b) : # 매개변수 a->5, b-> 6
    x = 10  # 지역변수
    a = 3   # 지역변수 수정
    b = 5   # 지역변수 수정
    print(x,y,a,b)  # y는 전역 변수를 사용/ 출력값: 10, 10, 3, 5

a = 5
b = 6
x = 9
y = 10
test(a,b)
a = x*y
print(x,y,a,b)  # 출력값: 9, 10, 90, 6
