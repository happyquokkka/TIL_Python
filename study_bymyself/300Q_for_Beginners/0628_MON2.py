# 0628_MON2.py
# 1주차 누적복습: 반복문(for문)
# Q.141-170

# 141. 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라.
# 단, 부가세는 10원으로 가정한다.

list = [100, 200, 300]
for num in list :
    print(num + 10)

# 142. for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
list = ['김밥', '라면', '튀김']
for menu in list :
    print('오늘의 메뉴:', menu)

# ★ 143. 리스트에 주식 종목이름이 저장돼 있다.
list = ['SK하이닉스', '삼성전자', 'LG전자']
for name in list :
    length = len(name)   # len() 함수는 매개변수로 들어온 문자열의 길이를 반환함
    print(length)

# 144. 리스트에 동물이름이 문자열로 저장돼 있다.
list = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력
for animal in list :
    length = len(animal)
    print(animal, length)

# 145. 리스트에 동물 이름이 문자열로 저장돼 있다.
list = ['dog', 'cat', 'parrot']
# for 문을 사용하여 동물 이름의 첫 글자만 출력
for animal in list :
    first = animal[0]
    print(first)

# 146. 리스트에는 세 개의 숫자가 바인딩 돼 있다.
list = [1, 2, 3]
for cal in list :
    print('3 x', cal)

# 147. 리스트에는 세 개의 숫자가 바인딩 돼 있다.
list = [1, 2, 3]
# for 문을 사용하여 다음과 같이 출력하라.
for cal in list :
    num = cal * 3
    print('3 x', cal, '=', num)

# ★ 148. 리스트에는 네 개의 문자열이 바인딩 돼 있다.
list = ['가', '나', '다', '라']
list1 = list[1:]
for character in list1 :
    print(character)

# 149. 리스트에는 네 개의 문자열이 바인딩 돼 있다.
list = ['가', '나', '다', '라']
list1 = list[0::2]
for character in list1 :
    print(character)

# 150. 리스트에는 네 개의 문자열이 바인딩 돼 있다.
list = ['가', '나', '다', '라']
list1 = list[::-1]
for character in list1 :
    print(character)


print ('-----------------------------------------')


# ★ 151. 리스트에는 네 개의 정수가 저장돼 있다.
list = [3, -20, -3, 44]
for num in list :
    if num < 0 :
        print(num)

print ('-----------------------------------------')

# 152. for 문을 사용하여 3의 배수만을 출력하라.
list = [3, 100, 23, 44]
for num in list :
    if num % 3 == 0 :
        print(num)

print ('-----------------------------------------')

# 153. 리스트에서 20보다 작은 3의 배수를 출력하라.
list = [13, 21, 12, 14, 30, 18]
for num in list :
    if (num % 3 == 0) and (num < 20) :
        print(num)

print ('-----------------------------------------')

# 154. 리스트에서 세 글자 이상의 문자를 화면에 출력하라.
list = ['I', 'study', 'python', 'language', '!']
for words in list :
    if len(words) >= 3 :
        print(words)

print ('-----------------------------------------')

# 155. 리스트에서 대문자만 화면에 출력하라.
list = ['A', 'b', 'c', 'D']
for word in list :
    if word.isupper() :
        print(word)

print ('-----------------------------------------')

# 156. 리스트에서 소문자만 화면에 출력하라.
list = ['A', 'b', 'c', 'D']
for word in list :
    if word.islower() :
        print(word)

print ('-----------------------------------------')

# ★ 157. 이름의 첫 글자를 대문자로 변경해서 출력하라.
list = ['dog', 'cat', 'parrot']
for name in list :
    print(name[0].upper() + name[1:])

print ('-----------------------------------------')

# 158. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
list = ['hellp.py', 'ex01.py', 'intro.hwp']
for file in list :
    file1 = file.split('.')[0]
    print(file1)

print ('-----------------------------------------')

# 159. 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in list :
    file1 = file.split('.')[1]
    if file1 == "h" :
        print(file)

print ('-----------------------------------------')

# 160. 파일 이름이 저장된 리스트에서 확장자가 .h 나 .c인 파일을 화면에 출력하라.
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in list :
    file1 = file.split('.')[1]
    if (file1 == "h") or (file1 == 'c') :
        print(file)

print ('-----------------------------------------')

# 161. for문과 range 구문을 사용해서 0~99까지 한 라인에 순차적으로 출력하는 프로그램을 작성하라.
for num in range(0,100) :
    print(num, end=" ")

print ('-----------------------------------------')

# ★ 162. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
for num in range(2002,2051, 4) :
    print(num)
# range() 함수: range(start, stop, step)로 세 번째 파라미터는 증감폭을 나타낼 수 있음
# 출처: https://withcoding.com/79

print ('-----------------------------------------')

# 163. 1부터 30까지의 숫자 중 3의 배수를 출력하라.
for num in range(1,31) :
    if num % 3 == 0 :
        print(num)

print ('-----------------------------------------')

# 164. 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for num in range(99,0,-1) :
    print(num)

print ('-----------------------------------------')

# ★ 165. for문을 사용해서 아래와 같이 출력하라.
for num in range(10) :
    print(num / 10)
# 동영상 풀이
# for i in range(0, 10) :
#   print("0.", i, sep="")   # sep-"" 하는 이유는 공백을 없애기 위함임

print ('-----------------------------------------')

# ★ 166. 구구단 3단을 출력하라.
for num in range(1, 10) :
    print (3, "x", num, " = ", 3 * num)

print ('-----------------------------------------')

# ★ 167. 구구단 3단을 출력하라. 단, 홀수 번째만 출력한다.
num = 3
for i in range(1, 10, 2) :
    print(num, "x", i, " = ", num * i)

print ('-----------------------------------------')

# ★ 누적합 ★: 168. 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for문을 사용하여 작성하라.
nsum = 0
for i in range(1,11) :
    nsum += i
print("합:", nsum)

print ('-----------------------------------------')

# 169. 1~10까지의 모든 홀수의 합을 출력하는 프로그램을 for문을 사용하여 작성하라.
nsum = 0
for i in range(1,11) :
    if i % 2 == 1 :
        nsum += i
print("합:", nsum)

print ('-----------------------------------------')

# 170. 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for문을 사용하여 작성하라.
nmul = 1
for i in range(1,11) :
    nmul *= i
print(nmul)




