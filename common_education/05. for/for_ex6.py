# for_ex6. py
# 다중 for문 연습문제2

for y in range(4) :
    for x in range(5) :
        x = "☆"
        print(x, end="")
    print()

print('---------------------------')

sum = 0
for x in range(1,6) :
    sum += 1
    sum1 = str("☆" * sum)
    print(sum1, end="")
    print()

print('---------------------------')

sum = 6
for x in range(5) :
    sum -= 1
    sum1 = str("☆" * sum)
    print(sum1, end="")
    print()

print('---------------------------')

sum = 0
for x in range(1,10) :
    sum += 1
    if sum % 2 != 0 :
        sum1 = str("☆" * sum)
        print(sum1, end="")
        print()

print('---------------------------')

sum = 10
for x in range(9) :
    sum -= 1
    if sum %2 != 0 :
        sum1 = str("☆" * sum)
        print(sum1, end="")
        print()







