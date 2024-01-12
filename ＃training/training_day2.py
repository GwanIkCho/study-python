user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},
]

number = 5
    # 추가
def insert(name):
    global number
    number += 1
    user_info.append({'number': number, 'name': name})

# 목록
def sellect_all():
    return user_info

# 조회(번호로 조회)
def select(number):
    for user in user_info:
        if user['number'] == number:
            return user
    # 수정(번호로 이름 수정)
def update(**kwargs):
    '''
    :param kwargs: number : 회원번호 : name : 바꿀이름
    '''
    select(kwargs.get('number'))['name'] = kwargs.get('name')

    # 삭제(번호로 삭제)

def delete(number):
    del user_info[user_info.index(select(number))]

insert('cho')
print(select(6))
print(update(number=1, name='pack'))
print(delete(2))
print(sellect_all())






post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

number = 5

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
def insert(**kwargs):
    global number
    number = number + 1
    post =


# 목록(최신순으로 조회)

# 조회(번호로 조회, 조회수 1 증가)




# 수정(번호로 정보 수정)


# 삭제(번호로 삭제)
