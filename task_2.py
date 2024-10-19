# TODO Найдите количество книг, которое можно разместить на дискете
size = 1.44
pages = 100
lines = 50
symbols = 25
one_symbol = 4

size_new = size * 1024 * 1024
book = symbols * lines * pages * one_symbol
number = size_new // book

print("Количество книг, помещающихся на дискету:", int(number))
