# 캐릭터 닉네임을 정할 때, 비속어를 사용하지 못하게 막아주기
# 바보 멍게 해삼 운영자
# 직접 Error를 제작하여 발생 시 안내 메세지까지 출려갛기


class NickNameError(Exception):
    def __str__(self):
        return "사용할수 없는 닉네임입니다."

def check_nickname(nickname):
    ben = ['바보', '멍게', '해삼', '운영자']
    for i in range(len(ben)):
        if ben[i] in nickname:
            raise NickNameError


nickname = input('닉네임 : ')

try:
    check_nickname(nickname)
    print(f'{nickname}으로 생성되었습니다')

except NickNameError as e:
    print(e)




