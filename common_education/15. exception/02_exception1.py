# 02_exception1.py
# 예외처리 예제

# 에러 종류와 상관 없이 모든 에러 처리
# try ~ except 구문

# try :
#     print(10/0) # 에러가 발생하면 무조건
#     print('나이: ' + 23 + '살')
# except :        # 본 구문으로 포커스가 넘어옴
#     print('오류발생')
#
# print('----- Exception 클래스 사용 -----')
#
# try :
#     print(10/0) # 에러가 발생하면 무조건
#     print('나이: ' + 23 + '살')
# except Exception:        # 본 구문으로 포커스가 넘어옴
#     print('오류발생')

# 에러 종류 명시
# try :
#     print('나이: ' + 23 + '살')   # type 에러 발생 ㅡ 에러 발생 이후 문장을 실행하지 않음
#     print(10/0)   # ZeroDivisionError 발생 ㅡ 바로 except 구문으로 넘어감
#
# except ZeroDivisionError:        # 0으로 나눈 논리 에러만 처리하겠다
#     print('오류발생')

# 숫자를 입력하지 않은 경우
# try :
#     num = int(input('숫자를 입력하세요: '))
# except ValueError :
#     print('숫자가 아닙니다')

# 에러 종류 명시 : as 에러 메시지 변수
# try :
#     num = int(input('숫자를 입력하세요: '))
# except ValueError as e:
#     print('숫자가 아닙니다',e)

## 여러 개의 except 구문 생성 : 첫 번째 에러만 처리됨
a = [1,2,3]

try :
    # print(10/0)
    print(a[4])
    print(10/0)
except ZeroDivisionError as e :
    print('0으로 나눌 수 없습니다')
except indexError as e :
    print(e)

#
a = [1,2,3]

try :
    # print(10/0)
    print(a[4])
    print(10/0)
except (ZeroDivisionError, IndexError) as e :
    print('오류가 발생했습니다')
