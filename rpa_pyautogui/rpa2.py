import pyautogui as posicaoMouse

posicaoMouse.sleep(2)

# print(posicaoMouse.position())

#menu iniciar
posicaoMouse.moveTo(x=1881, y=53)
posicaoMouse.click(x=1881, y=53)

posicaoMouse.typewrite('Chrome')

posicaoMouse.moveTo(x=1228, y=118)
posicaoMouse.click(x=1228, y=118)

posicaoMouse.sleep(2)
posicaoMouse.typewrite('valor do dolar')
posicaoMouse.press('enter')