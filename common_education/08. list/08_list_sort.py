# 08_list_sort.py

# sort() : 리스트 정렬, 원본 리스트 변경
scores = [90,78,81,64,89] ; print()
scores.sort()   # 기본 : 오름차순 정렬
print(scores)   # [64, 78, 81, 89, 90]

scores = [90,78,81,64,89] ; print()
scores.sort(reverse=True)   # 내림차순 정렬
print(scores)

scores = [90,78,81,64,89] ; print()
scores.reverse() # 원소의 위치를 역순으로 변경(정렬이 아니라 위치값만 변경하는 것임)
print(scores)   # [89, 64, 81, 78, 90]

print('---------------------------') ; print()

## 문자의 정렬 - 대문자 < 소문자, A~Z, a~z
char = ['b','A','d','C']
char.sort()   # 오름차순 정렬
print(char)

char = ['b','A','d','C']
char.sort(reverse=True)   # 내림차순 정렬 - ['d', 'b', 'C', 'A']
print(char)

print('---------------------------') ; print()

# 대소문자 구별 없이 알파벳 순으로 정렬하고 싶을 때
# key = str.lower
char = ['b','A','d','C']
char.sort(key=str.lower)  # sort의 옵션으로 key=str.lower 부여
print(char)

# 대소문자 구별없이 내림차순 정렬 하고 싶을 때
char = ['b','A','d','C']
char.sort(key=str.lower,reverse=True)
print(char)

print('---------------------------') ; print()

# 문자열은 어떻게 정렬?
ids = ['SKY','Blue','red','eBook','GREEN']
ids.sort()  # 오름차순 정렬 ㅡ 첫 문자 기준으로 정렬함
print(ids)  # ['Blue', 'GREEN', 'SKY', 'eBook', 'red']

# 대소문자 구별 없이 정렬
ids = ['SKY','Blue','red','eBook','GREEN']
ids.sort(key=str.lower)  # 대소문자 구별 없이 알파벳 순 정렬
print(ids)

print('---------------------------') ; print()

# sorted() : 원본을 유지하면서 정렬된 새로운 리스트를 반환함
a = [3,5,2,1,4]
b = sorted(a)
print('a:',a)
print('b:',b)
