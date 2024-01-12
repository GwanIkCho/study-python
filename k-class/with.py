class NameCard:
    def print_info(self, name):
        print(name)

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def __del__(self):
        print('del')

# with를 사용하면, 자동으로 file이 close된다.
with NameCard() as name_card:
    name_card.print_info('한동석')