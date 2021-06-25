# 09_print_end

# print()함수 : 다음 행에 출력 (커서를 다음으로 내린다)
print("first")
print("second")

# print() 실행 후 커서 마지막 칸에 고정하고자 할 때 end="" 사용
print("first", end="")
print("second")

# 구분자 표시 : 띄어쓰기, 쉼표, / : 등등 전부 사용 가능
print("first", end="-")
print("second")