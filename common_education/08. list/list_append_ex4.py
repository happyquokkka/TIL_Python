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