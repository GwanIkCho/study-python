user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},
]


# 추가
# 회원 번호는 자동 증가한다.
number = 5

def set_user():

    def insert(name):
        global number
        number += 1
        user_info.append({'number': number, 'name': name})

    # 목록
    def select_all():
        return user_info

    # 조회(번호로 조회)
    def select(number):
        for user in user_info:
            if user['number'] == number:
                return user
        return {}

    # 수정(번호로 이름 수정)
    def update(**kwargs):
        '''
        :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
        '''
        select(kwargs.get('number'))['name'] = kwargs.get('name')

    # 삭제(번호로 삭제)
    def delete(number):
        del user_info[user_info.index(select(number))]

    return {'insert': insert, 'select': select, 'update': update, 'delete': delete}


user_service = set_user()
user_service.get('insert')('han')
user_service.get('insert')('cho')
print(user_service.get('select')(6))
user_service.get('update')(number=7, name='kim')
user_service.get('update')(number=6, name='pack')
print(user_service.get('select')(6))
print(user_service.get('select')(7))


post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]


number = 5

def set_user():

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
    def insert(**kwargs):
        '''

        :param kwargs: {'title': '게시글 제목', 'content': '게시글 내용', 'file': '파일의 경로'},
        :return:
        '''
        global number
        number += 1
        post = {
            'number': number,
            'title': kwargs.get('title'),
            'content': kwargs.get('content'),
            'file': kwargs.get('file'),
            'read_count': 0
        }
        post_info.append(post)

    # 목록(최신순으로 조회)
    def select_all():
        return post_info[::-1]

    # 조회(번호로 조회, 조회수 1 증가)
    def read(number):
        post = select(number)
        post['read_count'] += 1
        return post


    def select(number):
        for post in post_info:
            if post['number'] == number:
                return post
        return {}


    # 수정(번호로 정보 수정)
    def update(**kwargs):
        post = select(kwargs.get('number'))
        post['title'] = kwargs.get('title')
        post['content'] = kwargs['content']
        post['file'] = kwargs.get('file')


    # 삭제(번호로 삭제)
    def delete(number):
        del post_info[post_info.index(select(number))]

    return {'insert': insert,
            'select_all': select_all,
            'read': read,
            'update': update,
            'delete':delete}


user_service = set_user()

user_service.get('insert')(title = '타이틀',content = '내용없음',file = '주소없음')
user_service.get('insert')(title = '7번',content = '7번',file = '7777777')
user_service.get('read')(number = 6)
user_service.get('read')(number = 6)
user_service.get('read')(number = 6)
user_service.get('read')(number = 6)
user_service.get('read')(number = 6)
user_service.get('update')(number = 5,title = '5번',content = '5번',file = '55555')
user_service.get('delete')(number = 3)
print(user_service.get('select_all')())




# insert(title='테스트 제목6', content='테스트 내용6', file='')
# print(select_all())
# print(read(5))
# print(read(5))
# print(read(5))
# post = read(5)
# post['title'] = '수정된 제목'
# update(**post)
# print(read(5))
# delete(5)
# print(select_all())