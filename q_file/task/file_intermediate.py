# def keep_only_alphabets(input_string):
#     clean_string = ''.join(char if char.isalpha() else '' for char in input_string)
#     return clean_string
# text_list = []
#
# with open('alice.txt', 'r', encoding='utf-8') as file:
#     text_file = file.read()
#
# words = text_file.split()
#
# text_list = [{}]
# count = 0
# for word in words:
#     word_lower = word.lower()
#     data = keep_only_alphabets(word_lower)
#     if len(data) > 1:
#         text_list.append({'word': word_lower, 'count': count})
#
#
#
#
#
#
# print(text_list)
#
#
#
#
with open('../ailce/alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()
    temp = []
    for character in content:
        if 'a'<character<'z':
            temp.append(character)
        else:
            temp.append(" ")

    content = ''.join(temp)

    words = [word for word in content.split() if len(word) > 1]



result = {}
for word in words:
    if result.get(word) is not None:
        result[word] += 1
    else:
        result[word] = 1

result = {
    word : result[word]
    for word in result
    if result[word] >= 100
}

sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
    print(key, result[key])














