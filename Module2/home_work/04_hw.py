# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

square_sides = 6

i = 0
j = 0
line = ''

while j < square_sides:
    while i < square_sides:
        if i == 0 or j == 0 or j == square_sides - 1 or i == square_sides - 1:
            line = line +'#'
        else:
            line = line + ' '
        i += 1
    print(line)
    i = 0
    line = ''
    j += 1
