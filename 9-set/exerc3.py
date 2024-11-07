animais = {"cachorro", "gato", "pássaro", "peixe", "coelho"}
print(f'{animais}\n')

n_animais = len(animais)
print(f'O número de animais é: {n_animais}\n')

animal_presente = 'gato'
animal_nao_presente = 'elefante'

def verificar_animal(nome):
    if nome in animais:
        print(f'O {nome} está presente no conjunto\n')
    else:
        print(f'O {nome} não está presente no conjunto\n')
        
verificar_animal(animal_presente)
verificar_animal(animal_nao_presente)

animais_copy = animais.copy()
print(animais is animais_copy)
animais_copy.add('tartaruga')
print(animais_copy)
print(animais)