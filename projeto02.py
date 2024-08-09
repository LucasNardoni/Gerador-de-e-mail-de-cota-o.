import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close
fechamento

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "@gmail.com"
assunto = "Análise do Projeto 2020"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Atte.
"""

webbrowser.open("www.gmail.com")
time.sleep(5)

pyautogui.PAUSE = 3

pyautogui.click(x=97, y=275)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1190, y=1039)

print("E-mail enviado com sucesso!")