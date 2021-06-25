# 05_input_ex3

dep = int(input("예금액 입력 : ")) #예금액
int_rate = float(input("이자율 입력(%) : ")) #이자율
int_ = int(dep * (int_rate/100))   #예금이자
balance = int(dep + int_)   #잔액
print("-------------------------------")
print("예금액 : %d 원" % dep)
print("이자율 : %.1f %%" % int_rate)
print("예금이자 : %d 원" % int_)
print("잔액 : %d 원" % balance)
print("-------------------------------")
print("예금액 : %d 원" % dep)
print("이자율 : %.1f " % int_rate, "%")
print("예금이자 : " + format(int_, ',') + "원")
print("잔액 : " + format(balance, ',') + "원")

# 쉼표를 붙이면 숫자가 아닌 문자열이 되므로 %s
"""
print("예금액 : %s 원" % format(dep, ','))
print("이자율 : %.1f %%" % int_rate)
print("예금이자 : %s 원" % format(int(int_), ','))
print("잔액 : %s 원" % format(int(balance), ','))
"""
