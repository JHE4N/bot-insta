from selenium import webdriver
import time

user = 'jhe4nbryan'
senha = 'eumeamo123'
seguir_este_user = 'hashtagprogramacao'

#criar navegador
navegador = webdriver.Chrome('chromedriver.exe')

#entrar no site do instagram
navegador.get('https://www.instagram.com/')
time.sleep(5)

#preencher usuário
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)

#preencher senha
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
time.sleep(1)

#clicar no botão entrar
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(5)

#salvar suas informações de login? Agora não
#navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
#time.sleep(3)

# ativar notificações? Agora não
navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(3)

#clicar na barra de pesquisa
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()

#digitar perfil a ser seguido
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(seguir_este_user)
time.sleep(2)

#clicar no nome do perfil a seguido (entrar nele)
navegador.find_element_by_class_name('-qQT3').click()
time.sleep(30)

#clicar no botão de seguir
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()