# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).


class User:
    # private: 자신의 클래스에서만 접근 가능
    # 1. 외부에서 접근하지 못하게 만듬
    # 2. 외부에서 접근할때 꼭 메소드로 접근해야한다.
    # __user_number = 0


    number = 0


    def __init__(self ,id ,pw, name):
        self.id = id
        self.pw = pw
        self.name = name
        User.number += 1
        self.number = User.number

    @classmethod
    def master(cls,id ,pw, name):

        id = 'admin_' + id

        return cls(id ,pw, name)

# user = User('iki','pw/kik','cho')

user1 = User('a123', 'a321', 'cho')
user2 = User('b123', 'b321', 'cho')
user3 = User('c123', 'c321', 'cho')
master1 = User.master('iki', 'pw/kik', 'cho')

print(user1.id, user1.pw, user1.name, user1.number)
print(master1.id, master1.pw, master1.name, master1.number)

# users = [User.master('iki', 'pw','cho'),
# User('c123', 'c321', 'cho')]
#
# print(users)