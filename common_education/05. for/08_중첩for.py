# 08_중첩for.py
# 다중 for문 : for문 안에 for문을 포함하고 있는 문장
# for y in range(3) : # y는 0-2까지 변한다
#     for x in range(5) : # x는 0에서 4까지 변한다
#         print(x, end=" ")
#     print("")

# print(x, end=" ") 문장의 수행 횟수는? 15번
# print() 문장의 수행 횟수는? 3번  y for문에 걸려있기 때문에!!!

# 다중 for문 연습문제1


# for i in range(1,5) :
#     sum += 1
#     print(i, end=" ")
#     for i in range(5,9) :
#         for i in range(9, 13) :
#             print(i, end=" ")
#     print("")

sum = 0

for y in range(3) :
    for x in range(4) :
        sum += 1
        print(sum, end=" ")
    print("")

# FT님의 가르침 -> y = 행, x = 열로 생각!! 따라서 3개의 행(y), 4개의 열(x)
# 모르겠을 때는 그리면서 생각해보기

