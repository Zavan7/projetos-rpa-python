conjunto_a = {1, "Python", (10, 20)}
print(conjunto_a)

# conjunto_a.add([3, 4, 5])
#erro

conjunto_a.add(5)
conjunto_a.remove(1)
print(conjunto_a)

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])

conjunto_b = (fs1, fs2)
print(conjunto_b)

# fs1.add(4)
# print(fs1)