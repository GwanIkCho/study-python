# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    choice = int(input(title+'\n'+menu))
    # 추가
    if choice == 1:
        new_name, new_price = input(append_message).split()
        if new_name not in name_list:
            name_list.append(new_name)
            price_list.append(int(new_price))
        else:
            result_message = append_error_message
    # 수정
    elif choice == 2:
        name = input(search_name_message_for_update)
        if name in name_list:
            new_name, new_price = input(append_message).split()
            if new_name not in name_list:
                index = name_list.index(name)
                name_list[index],price_list[index] = new_name, new_price
            else:
                result_message = update_error_message2
        else:
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        de = input(delete_message)
        if de in name_list:
            index = name_list.index(de)
            del name_list[index]
            del price_list[index]
        else:
            result_message = delete_error_message
    # 검색
    elif choice == 4:
        choice = int(input(search_menu))
        # 상품명검색
        if choice == 1:
            name = input(search_name_message)
            if name in name_list:
                index = name_list.index(name)
                print(f'{name_list[index]},{price_list[index]}')
                continue
            else:
                result_message = search_error_message
        # 가격검색
        elif choice == 2:
            price = int(input(search_price_message))
            if price in price_list:
                # min = price * 0.5
                # max = price * 1.5
                index = price_list.index(price)
                print(name_list[index],price_list[index])
                continue
            else:
                result_message = search_error_message
#     목록
    elif choice == 5:
        if len(name_list) == 0:
            result_message = no_item_message
        else:
            for i in range(len(name_list)):
                print(f'{name_list[i]},{price_list[i]}')
    elif choice == 6:
        break

    else:
        result_message = error_message

    print(result_message)
