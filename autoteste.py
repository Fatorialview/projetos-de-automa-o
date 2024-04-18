import pyautogui
import time

#abrir o chrome no windows
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')


#procurar pelo site no chrome
time.sleep(2)
pyautogui.click(x=944, y=607)
time.sleep(2)
pyautogui.click(x=646, y=86)
time.sleep(2)
pyautogui.write('Jornada do dev')
pyautogui.press('enter')
time.sleep(5)
           

#entrar no site e fazer o login e senha
pyautogui.click(x=385, y=500)       
time.sleep(3)
pyautogui.click(x=995, y=187)
time.sleep(3)   
pyautogui.click(x=1016, y=349)
pyautogui.write('flaviosgp26@yahoo.com.br')
time.sleep(3)
pyautogui.press('tab')
time.sleep(3)
pyautogui.write('Streetfiter1')
pyautogui.click(x=1106, y=531)
time.sleep(1)

   


#screenshot functions
