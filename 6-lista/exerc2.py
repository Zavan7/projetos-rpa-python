animais = []
animais.append ('gato')
animais.append ('cachorro')
animais.append ('pássaro')
print (animais)

animais.insert (1, 'peixe')
print (animais)

animais.remove ('gato')
print (animais)

amimal_removido = animais.pop()

print (animais)
print (amimal_removido)

animais_2 = ['tartaruga', 'hamister']

zoo = animais + animais_2 
zoo *= 2
print (zoo) 

print ('cachorro' in zoo)