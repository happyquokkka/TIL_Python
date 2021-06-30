# 05_list_함수 정리

a = [1,2,3,3,4]

# len()
# 내장함수
# 리스트의 길이 반환
print('전체 원소의 개수: ', len(a)) # 5 = 리스트 a의 원소의 개수

# count() = 리스트 객체의 메소드
# 메소드
# 리스트 내의 특정 요소의 개수 셈
# 리스트.count(요소)
print('원소 3의 개수: ', a.count(3)) # 2

print('--------------------------')

# append() : 리스트의 끝에 새로운 요소 추가
# 리스트.append(새로추가할요소)

# insert() : 리스트의 특정 위치에 요소 삽입
# 리스트.insert(삽입위치, 새로추가할요소)
# 06_list_append_insert.py 에 정리

# remove() : 리스트에서 값에 해당되는 요소를 제거
# 리스트.remove(값)
# 동일한 값이 여러 개 있는 경우 첫 번째 값만 제거

# pop() : 값을 반환하고 삭제
# 리스트.pop()
# 리스트의 마지막 요소를 반환하고 삭제
# 리스트.pop(인덱스값)
# 인덱스 위치에 있는 요소를 반환하고 삭제
# 07_list_remove_pop에 정리

# extend()
# 리스트의 확장
# 리스트.extend()
# 이전 리스트에 원소 추가하여 확장된 리스트로 변화함
# 원본 리스트 변경됨
a = [1,2,3]
a.extend([4,5])
print('a리스트:', a)

b = [1,2,3]
b.append([4,5])
print('b리스트', b)
# extend는 원소가 추가되면서 리스트가 확장됨 - 하나의 리스트
# append 와 insert 는 추가된 원소가 리스트면 하위 리스트로 추가됨 - 리스트 안의 리스트

c = [1,2,3]
c.insert(len(c),[4,5])
print('c리스트:',c)

print('---------------------------') ; print()

# sort() / reverse() / sorted() : 원소의 정렬과 관계되는 함수
# 08_list_sort.py에 정리

# index()
# 리스트 안에서 원소의 위치 값을 반환
# 리스트.index(값)
a = [1,2,3,4,5,5]
print(a.index(3))  # 값 3은 2번 인덱스에 있삼
print(a.index(5))  # 값 5는 4번 인덱스에 있삼/ 첫 번째 만나는 원소의 위치값을 반환
# print(a.index(10)) # ValueError: 10 is not in list  리스트 안에서 못 찾았삼


print('---------------------------') ; print()

# min() : 리스트 내 최소값을 가지는 원소 반환
# max() : 리스트 내 최댓값을 가지는 원소 반환

n = [100,7,-2,99,30]
char = ['c','a','D','A','b']
n_char = [1,300,'a','D',-2]

print(min(n))
print(max(n))

print(min(char))     # A (대문자 에이)
print(max(char))     # c (소문자 씨)


# 복합 자료형인 경우 max 함수나 min 함수는 사용할 수 없음

# print(min(n_char))  # TypeError: '<' not supported between instances of 'str' and 'int'
# print(max(n_char))  # TypeError: '<' not supported between instances of 'str' and 'int'

print('---------------------------')

# in/not in (포함여부 판단 후 True/False로 반환)
num = [1,2,3,4,5]
result = 2 in num   # 2가 있삼?
print(result)   # True

result = 2 not in num   # 2가 없삼?
print(result)   # False

# 리스트 일치 검사
# 비교 연산자를 사용해서 2개의 리스트 비교
# 첫 번째 요소부터 비교 시작
# 첫 번재 요소의 비교에서 결과가 False 면 더 이상 비교하지 않고 첫 번째 요소가 동일하면 두 번째 요소를 비교하는 방식
# 리스트 안에 모든 요소 비교 결과가 True 면 전체 결과 : True

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 == list2)

list1 = [5,2,3]
list2 = [1,2,3]
print(list1 >= list2)


