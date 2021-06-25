#03_input_ex1.py

a = int(input("국어 점수 입력 : "))
b = int(input("영어 점수 입력 : "))
c = int(input("수학 점수 입력 : "))
total = a+b+c
average = total/3

print("총점 :", total)
print("평균 : %.2f" % average)
