# 04_input_ex2.py

kg = float(input("몸무게(킬로그램): "))
m = float(input("키(미터): "))
bmi = kg / (m * m)

print("당신의 BMI : %.2f" % bmi)

# format() 함수 사용
print("당신의 BMI :", format(bmi, '.2f'))

