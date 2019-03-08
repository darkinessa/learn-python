# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв а в слове
word = 'Архангельск'
print(len((word)))

# Вывести количество гласных букв в слове
word = 'Архангельск'
i = 0

for volwels in list(word.lower()):
    if volwels in 'аеёиоуыэюя':
        i += 1
print(i)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

for word in sentence.split(' '):
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
word_sum = 0

for word in sentence.split(' '):
    word_sum = word_sum + len(word)

print(int(word_sum / len(sentence.split(' '))))
