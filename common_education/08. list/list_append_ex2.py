# list_append_ex2

scores = []
for i in range(1,6) :
    score = int(input('학생%d 점수 입력 : ' % i))
    scores.append(score)
total = scores[0]+scores[1]+scores[2]+scores[3]+scores[4]
avg = total/5
print('총점: %d' % total)
print('평균: %.2f' % avg)
