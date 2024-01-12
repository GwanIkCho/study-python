# fish.txt
# 사용자에게 입력받은 물고기를 fisg.txt에 작성한다
# 사용자가 q를 입력하면 fish.txt의 전체내용을 삭제한다.
# 사용자가 r을 입력하면, fish.tst를 콘솔에 출력한다.


fish = ''

while True:
    choice = input('선택해주세요\n'

                       'a. 내용 입력하기\n'
                       'q. 내용 전체 삭제하기\n'
                       'e. 내용만 확인하기\n'
                       'r. 내용 확인하고 튀기\n'
                       'm. 다바꾸기\n')


    if choice == 'a':
        p = input('추가할 내용을 적어주세요')
        file = open("fish.txt", "a", encoding="utf-8")
        file.write(p+'\n')
        file.close()

    elif choice == 'q':
        file = open("fish.txt", "w", encoding="utf-8")
        file.write('')
        file.close()

    elif choice == 'r':
        file = open("fish.txt", "r", encoding="utf-8")
        print(file.read())
        file.close()
        break
    elif choice == 'e':
        file = open("fish.txt", "r", encoding="utf-8")
        print(file.read())
        file.close()

    elif choice == 'm':
        file = open("fish.txt", "r", encoding="utf-8")
        line = None
        while line != '':
            line = file.readline()
            if line == '고등어\n':
                fish += '참치\n'
                print('바뀌었습니다.')
                continue

            fish += line
        file = open("fish.txt", "r", encoding="utf-8")




    else:
        print('메뉴에서 입력해주세요')


# 고등어를 참치로 수정하기





# with open('./fish.txt', 'w' ,encoding= 'utf-8') as file:
#     pass
#
# with open('./fish.txt', 'a',encoding= 'utf-8') as file:
#     fish = input('물고기 : ') + '\n'
#     file.write(fish)
#
# with open('./fish.txt', 'r', encoding= 'utf-8') as file:
#     print(file.read())