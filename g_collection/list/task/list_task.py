



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
    # 사용자에게 메뉴를 보여주고 번호를 선택하게한다.
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자).
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지 없다면,
        if new_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품명이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 수정할 이름을 입력하게한다.
        name = input(search_name_message_for_update)
        #  이름 목록에 같은 이름이 있는지 확인한다.
        if name in name_list:
            # 새로운 입력할 이름, 가격을 입력받는다.
            new_name, new_price = input(update_message).split()
            # 같은 이름이 없다는 가정하에
            if new_name not in name_list:
                # 인덱스 값을 찾아내고
                index = name_list.index(name)
                # 이름, 가격은 같은 자리에 인덱스 값을 가지고있어 같이 계산
                name_list[index], price_list[index] = new_name, new_price
                continue
            else:
                # 이미 등록된 이름이여서 취소
                result_message = update_error_message2
        # 찾는이름이 여기에 없음
        else:
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        #  삭제할 이름을 찾는다
        name = input(delete_message)
        #  그 이름이 이름 목록에 있는지 확인
        if name in name_list:
            # 그 이름의 인덱스 번호를 찾고
            index = name_list.index(name)
            #  이름, 가격은 같은 인덱스 번호를 가지고있어서 같이 제거
            del name_list[index]
            del price_list[index]
            continue

        else:
            #  같은 이름을 찾지못하면 출력
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        #  상품명으로찾을지 가격으로 찾을지 보여주고 선택지 줌
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 찾는 상품을 입력하게 함
            name = input(search_name_message)
            #  검색한 이름이 이름목록에 있는지 확인
            if name in name_list:
                #  있으면 인덱스 번호 확인
                index = name_list.index(name)
                #  그 인덱스 번호에 해당하는 이름. 가격 보여줌
                print(f'{name_list[index]}, {price_list[index]}')
                continue
            # 검색한 이름이 이름목록에 없음
            else:
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            #  가격을 검색함
            price = int(input(search_price_message))
            # 최대값, 최소값 설정을함
            min = price * 0.5
            max = price * 1.5
            # 가격리스트안에서 가격 조건설정 - 그 값이 다시 가격조건이되고 i에 담김 그러고 가격리스트에 조건 맞는애들담기
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]

            # 설정값이 하나라도 있다면
            if len(result_index) != 0:
                #  설정한 값을 보여주고
                for i in result_index:
                    print(f'{name_list[i]}, {price_list[i]}')
                    continue

            else:
                #  하나도 없으면 이거 보여줌
                result_message = search_error_message
    # 목록
    elif choice == 5:
        # 목록에 아무것도 없다면 메시지 보내줌
        if len(name_list) == 0:
            result_message = no_item_message
        else:
            # 하나라도 있다면 어떤것이 있는지 표시
            for i in range(len(name_list)):
                print(f'{name_list[i]}, {price_list[i]}')
                continue

    # 나가기
    elif choice == 6:
        # 탈-출
        break

    # 그 외
    # 모든 에러메시지를 한곳에 담아서 보내준다.
    else:
        result_message = error_message

    print(result_message)
    result_message = ""
