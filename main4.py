print('Данная программа является счетчиком слов, пробелов, знаков препинания, символов')
print('-------------------------------------------------------------------------------')
text = input('Введите текст: ')
count_probel = 0
for i in text:
    if i == " ":
        count_probel += 1
print('Количество пробелов:', count_probel)
print('Количество символов:', len(text))
print('Количество знаков препинания:', text.count('!') + text.count(',') + text.count('.') + text.count('?'))
print('Количество слов:', text.count(' ') + 1)
print('-------------------------------------------------------------------------------')

