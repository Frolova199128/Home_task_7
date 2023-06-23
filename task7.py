# Задача 34
#def Viny(str):
#    str = str.split()
#    list = []
#    for word in str:
#        result = 0
#        for i in word:
#            if i in 'аоуыэяёюие':
#                result +=1
#        list.append(result)
#    return len(list) == list.count(list[0])
#print('пара-ра-рам рам-пам-папам па-ра-па-да')
#str = input()
#if Viny(str):
#    print('Парам пам-пам')
#else:
#    print('Пам парам')

#Задача 36
def print_operation_table(operation, num_rows = 6, num_columns = 6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows +1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])
print_operation_table(lambda x, y: x * y)
