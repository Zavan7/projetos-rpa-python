s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8} 

union = s1 | s2
print(union)

union_m = s1.union(s2)
print(union_m)
print()

intersseccao = s1&s2
print(intersseccao)

inter_m = s1.intersection(s2)
print(inter_m)
print()

diferenca = s1-s2
print(diferenca)

dif_m = s1.difference(s2)
print(dif_m)
print()

dif_simetrica = s1 ^ s2
print(dif_simetrica)

dif_simetrica_m = s1.symmetric_difference(s2)
print(dif_simetrica_m)
print()


sub_conjunto = s1.issubset(s2)
print(sub_conjunto)

sup_conjunto = s2.issuperset(s1)
print (sup_conjunto)