n = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]

n.sort()
print (n)

n.reverse()
print (n)

nx = n.count(11)
print (nx)

on = n.index (78)
print (on)

try:
    index = n.index(100)
    print(f"O número 100 está no índice {index}.")
except ValueError:
    print("O número 100 não está na lista.")
