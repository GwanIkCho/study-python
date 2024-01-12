with open('alice.txt','r',encoding='utf-8') as file:
    content = file.read().lower()

temp = ''
for i in content:
    if 'a' <= i <= 'z':
        temp += i

    else:
        temp += ' '

words = [word for word in temp.split() if len(word) >1]

result = {}
for word in words:
    if result.get(word) is not None:
        result[word] += 1

    else:
        result[word] = 1


result = {word:result[word] for word in words if result[word]>100}

sorted_list = sorted(result, key=result.get, reverse=True )
for key in sorted_list:
    print(key, result[key])