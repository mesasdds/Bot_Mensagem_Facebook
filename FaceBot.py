from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

class Facebot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        time.sleep(3)

        # campo de usuario
        usernamecamp = driver.find_element(By.XPATH, "//input[@name = 'email']")
        usernamecamp.click()
        usernamecamp.clear()
        usernamecamp.send_keys(self.username)

        # campo da senha
        passwordcamp = driver.find_element(By.XPATH, "//input[@name = 'pass']")
        passwordcamp.click()
        passwordcamp.clear()
        passwordcamp.send_keys(self.password)

        passwordcamp.send_keys(Keys.RETURN)
        time.sleep(20)

        self.chama_chat()


    #metodo opcional para simular digitação de uma pessoa normal, não está sendo usado 
    #deve ser declarado no mensagem.send_keys
    @staticmethod
    def digite_igual_gente(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def chama_chat(self):
        driver = self.driver
        #A COLETA DOS LINKS QUE ESTÃO NO LIVE SERVER DO HTML NO LOCAL
        driver.get("LINK DO HTML EM LIVE SERVER")

        for i in range (1, 3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)

        hrefs = driver.find_elements(By.TAG_NAME, 'a')
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]


        for pic_href in pic_hrefs:
            #ALTERAR CONFORME GOSTO, TEMPO PARA CARREGAMENTO DE CADA PERFIL.
            time.sleep(40)
            driver.get(pic_href)
            try:
                time.sleep(5)
                #TODAS AS TAGS ABAIXO PODEM SER ALTERADAS PELO FACEBOOK, SEMPRE MANTER ATUALIZADO!
                driver.find_element(By.XPATH, "//span[contains(text(),'Mensagem')]").click()
                time.sleep(2)
                menssagem = driver.find_element(By.XPATH, "//div[@class= 'xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x1iyjqo2 x1gh3ibb xisnujt xeuugli x1odjw0f notranslate']")
                menssagem.click()
                menssagem.send_keys("TEXTO")
                time.sleep(10)
                driver.find_element(By.XPATH, "//div[@aria-label = 'Pressione Enter para enviar']").click()
            except Exception as e:
                #CASO ALGUMA TAG SEJA ALTERADA, VERIFICAR AS LOGS DO PRINT, DEVERA MOSTRAR A EXCEÇÃO DE QUAL TAG NÃO ESTA SENDO ENCONTRADA
                print(e)



Faceboot = Facebot("Email", "Senha")
Faceboot.login()



