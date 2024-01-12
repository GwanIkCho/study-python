# # 절대 경로: 대한민국 서울시 강남구 역삼동 123-123 103동 203호
# # 어떤 위치에 있든 상관없이 찾아갈 수 있는 경로
# # C:/a/b, D:/User/ted, ..
#
# # 상대 경로: 직진해서 좌회전 후 오른쪽 건물
# # 현재 위치에 따라 변경되는 경로
# # ./: 현재 경로, ../: 이전 경로, ./src/images, ../../a/b, src/images
#
# # 파일 생성하기
# file = open('food.txt', 'w', encoding='UTF-8')
# file.write('부대찌개\n')
# file.write('햄버거\n')
# file.close()
#
# # 파일 추가하기
# file = open('food.txt', 'a', encoding='UTF-8')
# file.write("피자\n")
# file.close()
#
# try:
#     file = open('food.txt','r',encoding='utf-8')
#     # print(file.read())
#     # for i in range(10):
#     #     print(file.readline(i),end='')
#     line = None
#     while line != '':
#         line = file.readline()
#         print(line, end='')
#
#
#     file.close()
# except FileNotFoundError:
#     print('경로를 확인해주세요')


# 외부파일에 있는 내용을 담아줄 변수
content = ''
with open('food.txt', 'r',encoding='utf-8') as file:
    line = None
    # 내용이 없는곳까지 달려갑니다
    while line != '':
        # line에 한줄씩 담아주고
        line = file.readline()
        # 햄버거가 있는지 확인하고
        if line == '햄버거\n':
            content += '치킨\n'

            continue
        content += line
        a = len(line)
        print(a)
# 수정 완료된 문자열 값 확인
print(content)
#  기존 내용을 수정 완료된 문자열로 덮어쓰기
with open('food.txt', 'w',encoding='utf-8') as file:
    file.write(content)
# 원본 파일의 내용 확인
with open('food.txt', 'r',encoding='utf-8') as file:
    print(file.read())

