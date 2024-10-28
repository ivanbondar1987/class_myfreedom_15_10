# Разделить строку "Apples, Oranges, Pears, Bananas, Berries" по запятым и вывести на экран. Затем обьединить элементы с использованием пробела, чтобы прога вывела "Apples Oranges Pears Bananas Berries"
str = 'Apples, Oranges, Pears, Bananas, Berries'
str_split = str.split(',')
print(str_split)
str_join = ' '.join(str_split)
print(str_join)