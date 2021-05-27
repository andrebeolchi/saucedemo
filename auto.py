from logging import exception
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

option = Options()
option.headless = False
driver = webdriver.Chrome(executable_path=('chromedriver.exe'),options=option)

driver.get("https://www.saucedemo.com/")

html = driver.page_source

username = ["standard_user", "locked_out_user", "problem_user"]#, "performance_glitch_user"]
password = "secret_sauce"

def login(username, password): # Realiza o login no site
    try:
        driver.find_element_by_xpath("//*[@id=\"user-name\"]").send_keys(username) # Digita username
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(password) # Digita senha
        driver.find_element_by_xpath("//*[@id=\"login-button\"]").click() # Clica pra login
    except Exception:
        print("\033[1;31;48m Tentativa falha de preencher campos de login")

def validate_login(): # Valida o login no site
    try:
        error = driver.find_element_by_xpath("//*[@id=\"login_button_container\"]/div/form/div[3]/h3") # Salva o campo de erro da página
        if "locked out" in error.text: # Se encontrar 'locked out' no campo de erro, reconhece usuário bloqueado
            print("\033[1;31;48m Usuário bloqueado")
            user_logged = False
        elif "not match any user" in error.text: # Se encontrar 'not match...', reconhece que o username/senha está errado
            print("\033[1;31;48m Usuário/Senha errado")
            user_logged = False
    except Exception:
        print("\033[1;32;48m Nenhum erro durante o login encontrado") # Se não encontrar o campo de erro da página, reconhece que foi realizado com sucesso o login no site
        user_logged = True
    return user_logged

def check_images(): # Checa imagem do produto
    html = driver.page_source # Salva o html novamente
    if "sl-404.168b1cce.jpg" in html: # Procura se a imagem do cachorro está na página
        print("\033[1;31;48m Imagem errada encontrada")
    else:
        print("\033[1;32;48m Todas as imagens estão certas")

def list_products(): # Realiza a listagem dos produtos
    html = driver.page_source
    options = ["za", "lohi", "hilo", "az"] # Define as opções do DropDown
    for option in options:
        select = Select(driver.find_element_by_class_name('product_sort_container')) # Define qual é o DropDown
        select.select_by_value(option) # Seleciona uma opção
        newHtml = driver.page_source

        if option == "az" and newHtml == html: # A página padrão é listada em 'az'
            print("\033[1;32;48m Listagem ", option ," realizada")
        elif option != "az" and newHtml == html:
            print("\033[1;31;48m Listagem ", option ," não realizada") # Caso selecione uma opção diferente de 'az', o código deverá mudar
        else:
            print("\033[1;32;48m Listagem ", option ," realizada") # Se o código mudar, a listagem funcionou

def check_products():
    products = ["item_0_title_link","item_1_title_link","item_2_title_link","item_3_title_link","item_4_title_link","item_5_title_link"]
    for product in products:
        product_main = driver.find_element_by_id(product).find_element_by_class_name("inventory_item_name").text
        driver.find_element_by_id(product).click()
        product_new = driver.find_element_by_xpath("//*[@id=\"inventory_item_container\"]/div/div/div[2]/div[1]").text
        if product_new == product_main:
            print("\033[1;32;48m Sucesso no redirecionamento")
        elif "NOT FOUND" in product_new:
            print("\033[1;31;48m ITEM NÃO ENCONTRADO") 
        else:
            print("\033[1;31;48m FALHA NO REDIRECIONAMENTO DO PRODUTO: ", product_main)
        
        price = driver.find_element_by_xpath("//*[@id=\"inventory_item_container\"]/div/div/div[2]/div[3]").text

        if "-" in price:
            print("\033[1;31;48m PREÇO DO PRODUTO ERRADO")
        else:
            print("\033[1;32;48m Preço correto")
        
        driver.find_element_by_xpath("//*[@id=\"back-to-products\"]").click()

for user in username:
    print("\033[1;37;48m==============================") # perfumaria
    print("==== TESTANDO USUÁRIO:  ", user) # perfumaria
    print("==============================") # perfumaria
    login(user, password)
    user_logged = validate_login()

    if user_logged == True:
        check_images()
        list_products()
        check_products()
    driver.get("https://www.saucedemo.com/")