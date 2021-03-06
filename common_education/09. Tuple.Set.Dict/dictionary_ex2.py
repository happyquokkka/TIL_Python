# dictionary_ex2.py

# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력받아 사전을 구성
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램

eng_dict = {}

# 사전 구성
while True :
    word = input('영어 단어 등록 (종료는 quit) : ')
    if word == "quit" :
        print()
        break
    if word not in eng_dict.keys() :    # 사전 안에 그 단어가 없다면
        meaning = input('%s의 뜻입력 (종료는 quit) : ' % word)
        eng_dict[word] = meaning    # eng_dict 이라는 빈 딕셔너리에 키값이 'word', 벨류값이 'meaning'인 아이템 추가
        print()
    elif word in eng_dict.keys() :
        print('%s는 이미 등록된 단어 입니다.' % word)
        print()

# 검색할 단어 입력
while True :
    search = input('검색할 단어 입력 (종료는 quit) : ')
    if search == 'quit' :
        print('종료합니다.')
        break
    elif search in eng_dict.keys() :
        print('%s의 뜻은 %s 입니다.' % (search, eng_dict[search]))
        print()
    elif search not in eng_dict.keys() :
        print('%s는 사전에 없는 단어입니다.' % search)
        print()


# 선생님 풀이

# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력받아 사전을 구성
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램

# 입력의 종료/ 단어 검색의 종료 모두 quit 단어를 이용한다
# 사전 구성이 끝나면 바로 단어 검색을 진행한다.

# 빈 딕셔너리 생성
# ek_dic = {}       # 라고 하거나
ek_dic = dict()     # dict 함수 호출

# 사전 구성
# 종료조건은 사용자가 quit 단어를 입력했을 때

while True :
    # 단어 등록
    eng = input('\n영어 단어 등록(종료는 quit) : ')

    # 단어를 등록시켜달라는 입력
    # 사전에 단어가 있는 경우 (등록하면 안 됨: 이미 등록된 단어입니다.)
    # 사전에 단어가 없는 경우 (뜻을 입력받아서 등록)
    if eng == 'quit' :
        break   # 단어등록 종료하겠삼
    elif eng not in ek_dic :
        kor = input('%s의 뜻 입력 :' % eng)
        ek_dic[eng] = kor
    else :
        print('%s는 이미 등록된 단어 입니다.' % eng)

print()

print('사전에서 단어를 검색하세요.')    # 사전에서 영단어 검색
while True :
    eng = input('검색할 단어 입력 (종료는 quit) : ')
    if eng == 'quit' :
        break
    elif eng in ek_dic :    # 입력된 단어가 사전에 있는 경우
        print('%s의 뜻은 %s 입니다.' % (eng, ek_dic[eng]))
    else :
        print('%s는 사전에 없는 단어입니다.' % eng)

print('\n종료합니다.')




