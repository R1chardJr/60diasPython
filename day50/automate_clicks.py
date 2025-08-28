import pyautogui
import time

print("Posicione o mouse na primeira posicao e espere 3 segundos. Apos isso, deixe o mouse na segunda posicao e espere mais 3 segundos.")
time.sleep(3)
x,y = pyautogui.position()
print(f"Posicao 1 capturada: {x}, {y}")
time.sleep(3)
x2,y2 = pyautogui.position()
print(f"Posicao 2 capturada: {x2}, {y2}")

qtde_cliques = int(input("Quantas vezes deseja fazer o loop? "))

for i in range(qtde_cliques):
    pyautogui.click(x, y)
    time.sleep(2)
    pyautogui.click(x2, y2)
    time.sleep(2)
else:
    print("Processo finalizado.")