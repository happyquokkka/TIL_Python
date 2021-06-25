# 04_variable3
# 화씨 온도를 섭씨 온도로 변환
fTemp = 90  # 정수변수
cTemp = (fTemp -32) * 5 /9  #정수연산
# cTemp 변수의 type은?

print(cTemp)
print("%f" % cTemp)
print("%.3f" % cTemp)
print("%10.3f" % cTemp) #실수 %f 사용시 전체자리수.소수이하자리수f 사용 가능

print("화씨온도 %d 를 섭씨온도로 변환하면 %.3f 입니다 " % (fTemp, cTemp))


