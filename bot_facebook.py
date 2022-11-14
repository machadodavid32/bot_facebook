from fileinput import close
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # Serve para trabalhar com dropdown
import os, random



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


# Passos para automação Facebook


# Digitar algo
# Clicar em publicar

driver = iniciar_driver()
# Abrir página facebook.com
driver.get('https://facebook.com')
sleep(2)

# Digitar email
email = driver.find_element(By.ID, 'email')
sleep(3)
email.send_keys('**********')

# Digitar senha
senha = driver.find_element(By.ID, 'pass')
sleep(2)
senha.send_keys('**********')

# Clicar em login
entrar = driver.find_element(By.XPATH, "//button[@name='login']")
entrar.click()

# Encontrar e clicar no campo de postagem
publicacao = driver.find_element(By.XPATH, "//div[@class='xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe']")
publicacao.click()
sleep(1)

# Clicar dentro do campo de "somente eu"
somente_eu = driver.find_element(By.XPATH, "//*[text()='Somente eu']")
somente_eu.click()
sleep(2)

# Clicar confirmar a escolha
concluir = driver.find_element(By.XPATH, '//*[text()="Concluir"]')
sleep(1)
concluir.click()

def digitacao_humana(texto, variavel):
    for letra in texto:
        variavel.send_keys(letra)
        sleep(random.randint(1,5)/30)

# Acima fiz um função para escrever de forma humana.
escrever = driver.find_element(By.XPATH, '//p[@class="x16tdsg8 x1mh8g0r xat24cr x11i5rnm xdj266r"]')
sleep(3)
digitacao_humana('oi, é somente um teste', escrever)
sleep(2)

# Clicar em publicar
publicar = driver.find_element(By.XPATH, "//*[text()='Publicar']")
sleep(2)
publicar.click()


input('')
driver.close()
