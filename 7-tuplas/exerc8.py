t1 = (3, 5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)

if t1 > t2:
    print('O maior é t1')
else:
    print ('O maior é t2')


if t3 > t1:
    print('O maior é t3')
else:
    print ('O maior é t1')


if t1 < t4:
    print('O menor é t4')
else:
    print ('O menor é t1')

if t1 == t5:
    print('Ambos são iguais')
elif t1 > t5:
    print('T1 é maior')
else:
    print ('O menor é t1')