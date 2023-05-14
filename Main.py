from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from tqdm import tqdm

import requests

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

INITIAL_POINTS = None

service = Service(ChromeDriverManager().install())

done = 0

def Opcoes(mobile = False):
    edge_options = webdriver.ChromeOptions()
    if mobile:
        edge_options.add_argument(
            "user-agent=Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0. 3945.79 Mobile Safari/537.36")

    edge_options.add_argument("--user-data-dir=C:\\Users\\Pichau\\AppData\\Local\\Google\\Chrome\\User Data\\")
    edge_options.add_argument("profile-directory=Default")

    driver = webdriver.Chrome(options=edge_options, service=service)

    driver.get("http://www.bing.com")

    return driver


def Searchs(mobile=False):
    global INITIAL_POINTS

    driver = Opcoes(mobile)

    palavras = requests.get("https://random-word-api.herokuapp.com/word?number=25")

    if not mobile:
        INITIAL_POINTS = driver.find_element(By.XPATH,'//*[@id="id_rc"]').text
        INITIAL_POINTS = int(INITIAL_POINTS)
        print(f"SEUS PONTOS INICIAIS SÃO : {INITIAL_POINTS}")

    pbar = tqdm(palavras.json(), desc='PROGRESSO')

    for palavra in pbar:

        search = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
        search.clear()
        search.send_keys(palavra)
        search.submit()
        pbar.update()
        sleep(2.5)
    pbar.close()
    if mobile:
        try:
            botao = driver.find_element(By.ID, 'mHamburger')
            botao.click()
            sleep(2)
            PONTOS_FINAIS = driver.find_element(By.ID, 'fly_id_rc')
            print(f"Pontos ganhos com Pesquisa : {int(PONTOS_FINAIS.text)-INITIAL_POINTS}\nSeus pontos agora : {PONTOS_FINAIS.text}")
        except:
            PONTOS_FINAIS = driver.find_element(By.ID, 'fly_id_rc')
            print(PONTOS_FINAIS.text)
            print(INITIAL_POINTS)

    driver.quit()

def Fortnite():
    driver = Opcoes()
    driver.get("https://www.xbox.com/pt-PT/play/games/fortnite/BT5P2X999VH2")
    sleep(10)

    botao = driver.find_element(By.XPATH, '//*[@id="gamepass-root"]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div')
    botao.click()
    sleep(100)
    print('FORTNITE ENCERRADO, REINVINDIQUE SEUS PONTOS NO APP')

print("""                                                         ▄▄              ▄▄                       
                                                       ▀███             ▄██                  ██   
                                                         ██              ██                  ██   
▀███▄███  ▄▄█▀██▀██▀    ▄█    ▀██▀▄█▀██▄ ▀███▄███   ▄█▀▀███  ▄██▀███     ██▄████▄   ▄██▀██▄██████ 
  ██▀ ▀▀ ▄█▀   ██ ██   ▄███   ▄█ ██   ██   ██▀ ▀▀ ▄██    ██  ██   ▀▀     ██    ▀██ ██▀   ▀██ ██   
  █▓     ▓█▀▀▀▀▀▀  ██ ▄█  ██ ▄█   ▄███▓█   █▓     █▓█    █▓  ▀█████▄     ▓█     ██ ██     ██ ██   
  █▓     ▓█▄    ▄   ███    █▓▓   █▓   ▓█   █▓     ▀▓█    █▓       ██     ▓▓▓   ▄█▓ ██     ▓█ █▓   
  ▓▓     ▓▓▀▀▀▀▀▀   ▓█▓▓   ▓▒▓    ▓▓▓▓▒▓   ▓▓     ▓▓▓    ▓▓  ▀▓   █▓     ▓▓     ▓▓ ▓█     ▓▓ ▓▓   
  ▓▒     ▒▓▓        ▓▓▓    ▓▒▓   ▓▓   ▒▓   ▓▒     ▀▒▓    ▓▒  ▓▓   ▓▓     ▒▓▓   ▓▓▓ ▓▓▓   ▓▓▓ ▓▓   
▒ ▒▒▒     ▒ ▒ ▒▒     ▒      ▒    ▒▓▒ ▒ ▓▒▒ ▒▒▒     ▒ ▒ ▒ ▓ ▒ ▒ ▒▓▒       ▒ ▒ ▒ ▒▒   ▒ ▒ ▒ ▒  ▒▒▒ ▒
                                                                                                  
                                                                                                  
""")

print("INICIANDO PESQUISAS PC...")
Searchs()
print("INICIANDO PESQUISAS MOBILE...")
Searchs(True)
print("INICIANDO FORTNITE...")
Fortnite()