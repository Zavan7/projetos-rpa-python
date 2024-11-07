import pyautogui as posicaoArquivos

posicaoArquivos.hotkey('win', 'r')
posicaoArquivos.sleep(1)

posicaoArquivos.typewrite('notepad')
posicaoArquivos.press('enter')

posicaoArquivos.sleep(1)
posicaoArquivos.typewrite('ola mundo')

posicaoArquivos.sleep(1)
fecharJanela = posicaoArquivos.getActiveWindow()

fecharJanela.close()

posicaoArquivos.sleep(1)

posicaoArquivos.press('tab')
posicaoArquivos.press('enter')
