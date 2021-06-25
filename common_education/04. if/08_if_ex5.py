# 08_if_ex5

a = int(input("도형 입력(1: 사각형, 2: 삼각형, 3: 원) : "))

if a == 1 :
    b = float(input("가로 입력: "))
    c = float(input("세로 입력: "))
    area1 = b*c
    print("사각형의 면적 = %.2f" % area1)

elif a == 2 :
    d = float(input("밑변 입력: "))
    e = float(input("높이 입력: "))
    area2 = d*e/2
    print("삼각형의 면적 = %.2f" % area2)

else :
    f = float(input("반지름 입력: "))
    area3 = f*f*3.141592
    print("원의 면적 = %.2f" % area3)
