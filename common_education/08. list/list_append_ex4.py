# list_append_ex4.py

# 현재 5명으로 고정된 학생 수를 입력 받은 수만큼 점수 입력하는 것으로 변경

good = 0
scores = []
student = int(input('학생 수 입력 : '))
for i in range(1,student+1) :
    score = int(input('학생%s 점수 입력 : ' % i))
    scores.append(score)
    if score >= 80:
        good += 1

total = sum(scores)
avg = total/len(scores)

print('총점: %d' % total)
print('평균: %.2f' % avg)
print('80점 이상 학생 : %d명' % good)

# 선생님 풀이

# -------변수생성-----------
# 누적변수 생성
sum_s = 0
count = 0  # 80점 이상인 학생 수를 세기 위한 변수

# --------처리부분-----------
# 학생 수 입력 받는 코드
num = int(input('학생 수 입력 :'))

# 빈 리스트 생성
scores = []
for i in range(num):
    score = int(input('학생' + str(i + 1) + '점수 입력 :'))
    # 리스트에 추가하고
    scores.append(score)

# 리스트의 각 점수 합계
for s in scores:
    sums_s += s  # 총점 계산
    if s >= 80:
        count += 1

# 평균 계산
avg = sums_s / len(scores)
# 총점, 평균 출력
print('총점: %d' % sum_s)
print('평균: %.2f' % avg)
print('80점 이상 학생: %d명' % count)