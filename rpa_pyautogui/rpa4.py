import pyautogui
import pyautogui as escolherOpcao

# escolherOpcao.sleep(5)
# print (escolherOpcao.position())

opcao = pyautogui.confirm('Escolha uma das opções abaixo', buttons = ['Excel', 'Word', 'Notepad'])

if opcao == 'Excel':
    escolherOpcao.hotkey('win', 'r')
    escolherOpcao.typewrite('Excel')
    escolherOpcao.press('enter')
    escolherOpcao.sleep(2)
    escolherOpcao.moveTo(x=299, y=206)
    escolherOpcao.click(x=299, y=206)
    escolherOpcao.sleep(2)
    escolherOpcao.typewrite('Excel')


elif opcao == 'Word':
    escolherOpcao.hotkey('win', 'r')
    escolherOpcao.typewrite('Winword')
    escolherOpcao.press('enter')
    escolherOpcao.sleep(2)
    escolherOpcao.moveTo(x=299, y=206)
    escolherOpcao.click(x=299, y=206)
    escolherOpcao.sleep(2)
    escolherOpcao.typewrite('Word')

elif opcao == 'Notepad':
    escolherOpcao.hotkey('win', 'r')
    escolherOpcao.typewrite('Notepad')
    escolherOpcao.press('enter')
    escolherOpcao.sleep(2)
    escolherOpcao.typewrite('Notepad')

