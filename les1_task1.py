'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

#from sys import getsizeof as memor

a = int(input('Введите трехзначное число: '))
a1 = a//100
a2 = a%100//10
a3 = a%10
summ = a1+a2+a3
proizv = a1*a2*a3
print('Сумма:       ', summ)
print('Произведение:', proizv)

#print(memor(a), memor(a1), memor(a2), memor(a3), memor(summ), memor(proizv))
#print(memor(a) + memor(a1) + memor(a2) + memor(a3) + memor(summ) + memor(proizv))

# При вводе значения "100" сумма используемой памяти всеми переменными (a,a1,a2,a3,summ,proizv) = 156 байт
# При вводе значения "999" сумма используемой памяти всеми переменными (a,a1,a2,a3,summ,proizv) = 168 байт
# (разница связана с тем, что с количеством нолей в числе растет и количество переменных, имеющих значение 0)
