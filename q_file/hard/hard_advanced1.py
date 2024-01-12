from q_file.hard.hard_calc1 import Calculator

menu = "1. 계산하기\n2. 로그보기\n3. 종료하기\n"
number_message = "두 정수를 입력하세요.\n예)3 4\n"
oper_message = "연산자를 입력하세요.(+, -, *, / 중 1 택)\n"
error_message = "다시 시도하세요."
error_code = None

while True:
    choice = int(input(menu+'\n'))
    if choice == 1:
        number1,number2 = map(int, input(number_message).split())
        oper =  input(oper_message)
        result = Calculator(number1).calc(number2,oper)
        print(result)

    elif choice == 2:
        pass
    elif choice == 3:
        break