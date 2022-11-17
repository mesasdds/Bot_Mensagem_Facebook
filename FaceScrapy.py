from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


#classe construtoraprincipal
class FaceBoot:
    #funcao de inicio com os parametros de usuario e senha
    def __init__(self, username, password):
        self.usermame = username
        self.password = password
        #self do driver
        self.driver = webdriver.Chrome()


    #funcao login com o site que vamos logar
    def login(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        time.sleep(3)


        #campo de usuario
        usernamecamp = driver.find_element(By.XPATH, "//input[@name = 'email']")
        usernamecamp.click()
        usernamecamp.clear()
        usernamecamp.send_keys(self.usermame)

        #campo da senha
        passwordcamp = driver.find_element(By.XPATH, "//input[@name = 'pass']")
        passwordcamp.click()
        passwordcamp.clear()
        passwordcamp.send_keys(self.password)

        passwordcamp.send_keys(Keys.RETURN)
        time.sleep(3)

        self.procura("GruposFace")

    def procura(self, grupo):
        driver = self.driver
        
        #IMPORTE: O LINK AQUI DEVE SER COPIADO DA AREA DE SEGUIDORES DE UM GRUPO DO FACEBOOK!
        #1_ENTRAR NO GRUPO DESEJADO, 2_CLICAR NA ABA DE PESSOAS 
        #EXEMPLO DO LINK: https://www.facebook.com/groups/XXXXXXXXXXXX/members
        driver.get("LINK DO GRUPO")
        
        for i in range (1, 10):#SUBSTITUA O 10 PARA O NUMERO DE VEZES QUE FOR NECESSÁRIO O SCROLL NA PAGINA!
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)

        #COLETA TODAS TAG A
        hrefs = driver.find_elements(By.TAG_NAME, 'a')
        
        #SERA SALVO EM UM ARQUIVO TXT
        arquivo = open("grupos perfils.txt", "a")
        linhas = list()

        #COLETA DO LINK DOS PERFIS
        perfils = [elem.get_attribute('href') for elem in hrefs]
        for perfil in perfils:
                linhas.append("\n<a href=" + str(perfil) + ">" + "\nLINK PERFIL AQUI</a>\n")

        linhas = set(linhas)
        #Finaliza aqui!
        arquivo.writelines(linhas)


Testefunc = FaceBoot("Email", "Senha")
Testefunc.login()

