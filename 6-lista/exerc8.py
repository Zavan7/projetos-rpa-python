notas = [89, 92, 56, 78, 45, 34, 90, 99, 65, 76, 80, 82]

notas_altas = [notas for notas in notas if notas >= 75]

notas_altas.sort()

print(notas_altas)
