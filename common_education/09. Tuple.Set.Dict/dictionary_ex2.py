# dictionary_ex2.py

# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력받아 사전을 구성
# 사용자가 입력한 단어를 검색하여 뜻을 출력하는 프로그램

eng_dict = {'word':''}

# 사전 구성
while True :
    word = input('영어 단어 등록 (종료는 quit) : ')
    meaning = input('%s의 뜻입력 (종료는 quit) : ' % word)
    eng_dict[word]=str(meaning)
    if word == "quit" :
        break
        print()

# 검색할 단어 입력
while True :
    search = input('검색할 단어 입력 (종료는 quit) : ')
    print('%s의 뜻은 %s입니다' % (search,eng_dict['%s'] % search))
    break


