# split.ex.py

# 그림과 같이 입력 받고 split()을 사용하여 분리

birthday = input('생일 입력 (연/월/일) :')
year = birthday.split('/')[0]
month = birthday.split('/')[1]
day = birthday.split('/')[2]
print('당신은 %s년에 태어났고' % year)
print('생일은 %s월 %s일 이군요' % (month, day))
