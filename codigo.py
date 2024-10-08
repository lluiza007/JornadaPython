# Passo 1: Entrar no sistema
import pyautogui
import time
import pandas as pd

#abir o navegador
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2: Fazer login
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=893, y=535)
pyautogui.write("oyaraluiza@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=944, y=727)

time.sleep(2)

# Passo 3: Importar base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto


for linha in tabela.index:
    pyautogui.click(x=750, y=384)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(1000)

# Passo 5: repetir o processo de cadastro até acabar os produtos