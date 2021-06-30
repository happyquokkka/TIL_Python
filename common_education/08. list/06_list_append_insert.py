# 06_list_append_insert.py

append()
a = [1,2,3,4]
a.append(5) # a 리스트 마지막 요소로 5를 추가하고 a에 저장 (원본을 바꾼다!)
print(a)    # [1,2,3,4,5]

a.append([6,7]) # a 리스트 마지막에 하위 리스트 추가
print(a)    # [1, 2, 3, 4, 5, [6, 7]]

# a.append(8,9) # 원소를 2개 추가하면 에러남 - TypeError: list.append() takes exactly one argument
# append는 무조건 하나의 값만 추가할 수 있음

# 빈 리스트 생성하고 요소를 나중에 추가하고 싶을 때
values = []
values.append(10)
values.append(20)
values.append(30)   # [10,20,30]
print(values)

# 사용자에게 5개의 값을 입력받아서 리스트에 저장하는 코드
scores = []     # 값을 저장할 빈 리스트 생성
for i in range(5) :
    num = int(input('값을 입력하세요: '))
    scores.append(num)
    print(i+1,'번째 입력결과:' ,scores)
print(scores)

# 위 코드에서 입력받은 값을 각 요소로 출력하는 코드를 작성하시오.
# 리스트 요소 출력

for score in scores :
    print(score)

for i in range(len(scores)) :
    print(scores[i])

print('---------------------------')

# insert(위치, 값) : 리스트 특정 위치에 요소 삽입
nums = [1,2,3,4,5]
nums.insert(1,200)  # 두 번째 위치에 삽입(인덱스 값 1번에 삽입 - 기존 인덱스 1번 이상부터는 뒤로 밀림)
print(nums)     # [1, 200, 2, 3, 4, 5]

nums.insert(-1,'홍길동') # 마지막 원소 바로 전에 삽입 [1, 200, 2, 3, 4, '홍길동', 5]
print(nums)

# insert 함수를 이용해서 리스트 맨 뒤에 삽입 - append 를 활용하는 것이 일반적
nums.insert(len(nums),12.3)
print(nums)

nums.insert(len(nums)-1, [10,20]) # 삽입되는 위치는? 마지막 원소 앞에 하위 리스트 삽입
print(nums)     # [1, 200, 2, 3, 4, '홍길동', 5, [10, 20], 12.3]


