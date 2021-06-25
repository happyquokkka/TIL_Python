# 03_for_누적합.py
sumx = 0  # 누적변수는 사용하기 전에 반드시 선언(=초기화, 준비)
# 1부터 10까지 출력하고 1-10까지 더한 결과도 출력하는 프로그램을 작성하시오
for x in range(1,11) :
    print(x)
    # sumx = sumx + x
    sumx += x   # 누적합 연산으로 표현하는 게 연산 수가 줄어서 효율적이기는 함
print('1부터 10까지 누적 합:', sumx)


# 1+2=3
# 3+3=6
# 6+4=10

# x 가 1일 때 sumx는 0인 상태에서 sumx = sumx + x
# x 가 2일때 sumx는 1인 상태에서 sumx = sumx + x
# ...

sumx = 0 # (아까 설정한 55가 들어가므로 다시 sumx 초기화)
## 1부터 100까지 더하는 프로그램을 작성하세요
for x in range(1,101) :
    print(x)
    # sumx = sumx + x
    sumx += x  # 누적합 연산으로 표현하는 게 연산 수가 줄어서 효율적이기는 함
print('1부터 100까지 누적 합:', sumx)
