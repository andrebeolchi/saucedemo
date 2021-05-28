from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

option = Options()
option.headless = False # True = Segundo Plano, False = Executa na tela
driver = webdriver.Chrome(executable_path=('chromedriver.exe'),options=option)
driver.get("https://www.saucedemo.com/")
html = driver.page_source

def userPrint(user):
    if user == "standard_user":
        print("\033[1;37;48m╔═════════════════════════════════════════════════╗\033[0m") # Perfumaria
        print("\033[1;37;48m║                USUÁRIO: STANDART_USER           ║") # Perfumaria
        print("\033[1;37;48m╟═════════════════════════════════════════════════╣\033[0m") # Perfumaria
    elif user == "problem_user":
        print("\033[1;37;48m╔═════════════════════════════════════════════════╗\033[0m") # Perfumaria
        print("\033[1;37;48m║                USUÁRIO: PROBLEM_USER            ║") # Perfumaria
        print("\033[1;37;48m╟═════════════════════════════════════════════════╣\033[0m") # Perfumaria
    elif user == "not_valid_user":
        print("\033[1;37;48m╔═════════════════════════════════════════════════╗\033[0m") # Perfumaria
        print("\033[1;37;48m║               USUÁRIO: NOT_VALID_USER           ║") # Perfumaria
        print("\033[1;37;48m╟═════════════════════════════════════════════════╣\033[0m") # Perfumaria
    elif user == "locked_out_user":
        print("\033[1;37;48m╔═════════════════════════════════════════════════╗\033[0m") # Perfumaria
        print("\033[1;37;48m║              USUÁRIO: LOCKED_OUT_USER           ║") # Perfumaria
        print("\033[1;37;48m╟═════════════════════════════════════════════════╣\033[0m") # Perfumaria
    else:
        print("\033[1;37;48m╔═════════════════════════════════════════════════╗\033[0m") # Perfumaria
        print("\033[1;37;48m║          USUÁRIO: PERFORMANCE_GLITCH_USER       ║") # Perfumaria
        print("\033[1;37;48m╟═════════════════════════════════════════════════╣\033[0m") # Perfumaria

def login(username, password): # Realiza o login no site
    start = time.time()
    try:
        driver.find_element_by_xpath("//*[@id=\"user-name\"]").send_keys(username) # Digita username
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(password) # Digita senha
        driver.find_element_by_xpath("//*[@id=\"login-button\"]").click() # Clica pra login
    except Exception:
        print("\033[1;31;48m╟═════════════════════════════════════════════════╣\033[0m") # Perfumaria
        print("\033[1;31;48m║   Tentativa falha de preencher campos de login  ║\033[0m") # Perfumaria
        print("\033[1;31;48m╚═════════════════════════════════════════════════╝\033[0m") # Perfumaria
    end = time.time()

    if end - start > 0.5:
        print("\033[1;33;48m║   PROBLEMA DE PERFORMANCE AO REALIZAR O LOGIN   ║\033[0m") # Perfumaria

def validate_login(): # Valida o login no site
    try:
        error = driver.find_element_by_xpath("//*[@id=\"login_button_container\"]/div/form/div[3]/h3") # Salva o campo de erro da página
        if "locked out" in error.text: # Se encontrar 'locked out' no campo de erro, reconhece usuário bloqueado
            
            print("\033[1;31;48m║               USUÁRIO BLOQUEADO                 ║\033[0m") # Perfumaria
            print("\033[1;31;48m╚═════════════════════════════════════════════════╝\033[0m") # Perfumaria

            user_logged = False
        elif "not match any user" in error.text: # Se encontrar 'not match...', reconhece que o username/senha está errado

            print("\033[1;31;48m║               USUÁRIO/SENHA ERRADO              ║\033[0m") # Perfumaria
            print("\033[1;31;48m╚═════════════════════════════════════════════════╝\033[0m") # Perfumaria

            user_logged = False
    except Exception:
        print("\033[1;32;48m║      Nenhum erro durante o login encontrado     ║\033[0m") # # Se não encontrar o campo de erro da página, reconhece que foi realizado com sucesso o login no site
        user_logged = True
    return user_logged

def check_images(): # Checa imagem do produto
    html = driver.page_source # Salva o html novamente
    if "sl-404.168b1cce.jpg" in html: # Procura se a imagem do cachorro está na página
        print("\033[1;31;48m║             IMAGEM ERRADA ENCONTRADA            ║")
    else:
        print("\033[1;32;48m║           Todas as imagens estão certas         ║")

def list_products(): # Realiza a listagem dos produtos
    start = time.time()
    html = driver.page_source
    options = ["za", "az", "lohi", "hilo"] # Define as opções do DropDown
    for option in options:
        select = Select(driver.find_element_by_class_name('product_sort_container')) # Define qual é o DropDown
        select.select_by_value(option) # Seleciona uma opção
        newHtml = driver.page_source

        if  newHtml == html:
            print("\033[1;31;48m║              LISTAGEM  NÃO REALIZADA            ║ >> ", option.upper()) # Caso selecione uma opção diferente de 'az', o código deverá mudar
        else:
            print("\033[1;32;48m║                 Listagem realizada              ║ >> ", option.upper()) # Se o código mudar, a listagem funcionou
        html = newHtml
    end = time.time()
    if end - start > 0.5:
        print("\033[1;33;48m║ PROBLEMA DE PERFORMANCE PARA LISTAR OS PRODUTOS ║\033[0m") # Perfumaria

def check_products(): # Checa se os produtos estão sendo redirecionados para a página certa
    start = time.time()
    products = ["item_0_title_link","item_1_title_link","item_2_title_link","item_3_title_link","item_4_title_link","item_5_title_link"]
    for product in products:
        product_main = driver.find_element_by_id(product).find_element_by_class_name("inventory_item_name").text # Pega o nome do produto na pagina inicial
        driver.find_element_by_id(product).click() # Clica no produto
        product_new = driver.find_element_by_xpath("//*[@id=\"inventory_item_container\"]/div/div/div[2]/div[1]").text # Pega o nome do produto na pagina do produto
        if product_new == product_main: # Verifica se o nome do produto da pagina inicial é igual a da pagina do produto

            print("\033[1;32;48m║           Sucesso no redirecionamento           ║")

        elif "NOT FOUND" in product_new: # Verifica se o nome do produto não foi encontrado
            print("\033[1;31;48m║                ITEM NÃO ENCONTRADO              ║ >>", product_main.upper()) 

        else:
            print("\033[1;31;48m║      FALHA NO REDIRECIONAMENTO DO PRODUTO       ║ >>", product_main.upper()) # Se os nomes não forem iguais ocorreu uma falha no redirecionamento
        
        price = driver.find_element_by_xpath("//*[@id=\"inventory_item_container\"]/div/div/div[2]/div[3]").text # Pega o preço do produto

        if "-" in price: # Verifica se o produto tem valor negativo
            print("\033[1;31;48m║              PREÇO DO PRODUTO ERRADO            ║") # Se tiver, o preço está errado
        else:
            print("\033[1;32;48m║                   Preço correto                 ║") # Se não tiver, o preço está certo
        
        driver.find_element_by_xpath("//*[@id=\"back-to-products\"]").click() # Volta para a tela inicial
    end = time.time()
    if end - start > 1.2:
        print("\033[1;33;48m║  PROBLEMA DE PERFORMANCE PARA CHECAR PRODUTOS   ║ \033[0m") # Perfumaria

def add_remove(): # Checa se o botão adicionar/remover está funcionando
    start = time.time()
    add_buttons = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light","add-to-cart-sauce-labs-bolt-t-shirt","add-to-cart-sauce-labs-fleece-jacket","add-to-cart-sauce-labs-onesie","add-to-cart-test.allthethings()-t-shirt-(red)"]
    remove_buttons = ["remove-sauce-labs-backpack", "remove-sauce-labs-bike-light","remove-sauce-labs-bolt-t-shirt","remove-sauce-labs-fleece-jacket","remove-sauce-labs-onesie","remove-test.allthethings()-t-shirt-(red)"]

    for x in range(len(add_buttons)): # Testa todos os botões
        try:
            driver.find_element_by_id(add_buttons[x]).click() # Adiciona ao carrinho
            try: # Tenta remover
                driver.find_element_by_id(remove_buttons[x]).click() # Remove do carrinho
                print("\033[1;32;48m║    Adicionar/Remover ao carrinho com sucesso    ║")
            except Exception:
                print("\033[1;31;48m║      ERRO AO ADICIONAR/REMOVER DO CARRINHO      ║") # Se não remover, ocorreu uma falha
        except Exception:
            print("\033[1;31;48m║              ITEM ADICIONADO ERRADO             ║")
    end = time.time()
    if end - start > 0.6:
        print("\033[1;33;48m║  PROBLEMA DE PERFORMANCE PARA ADICIONAR/REMOVER ║ \033[0m") # Perfumaria

def cart(): # Realiza a compra do produto
    start = time.time()

    driver.find_element_by_xpath("//*[@id=\"shopping_cart_container\"]/a").click() # Abre o carrinho
    driver.find_element_by_xpath("//*[@id=\"checkout\"]").click() # Clica para comprar

    firstname = driver.find_element_by_xpath("//*[@id=\"first-name\"]")
    firstname.send_keys('first') # Preenche campo de first name

    lastname = driver.find_element_by_xpath("//*[@id=\"last-name\"]")
    lastname.send_keys('last') # Preenche campo de last name

    postalcode = driver.find_element_by_xpath("//*[@id=\"postal-code\"]")
    postalcode.send_keys('postal') #Preenche campo de postal code

    if firstname.get_attribute("value") == "first" and lastname.get_attribute("value") == "last" and postalcode.get_attribute("value") == "postal": # Se TODOS os campos estiverem preenchidos, clica para comprar
        driver.find_element_by_xpath("//*[@id=\"continue\"]").click()    

        print("\033[1;32;48m║      Sucesso em preencher campos da compra      ║")

        driver.find_element_by_xpath("//*[@id=\"finish\"]").click() # Finalizar a compra

        if driver.find_element_by_xpath("//*[@id=\"checkout_complete_container\"]/h2").text == "THANK YOU FOR YOUR ORDER": # Se aparecer 'Thank you" a compra foi realizada com sucesso
            
            print("\033[1;32;48m║          Sucesso em realizar a compra           ║")
            print("\033[1;32;48m╚═════════════════════════════════════════════════╝\033[0m") # Perfumaria

        else:


            print("\033[1;31;48m║            FALHA EM REALIZAR A COMPRA           ║")
            print("\033[1;31;48m╚═════════════════════════════════════════════════╝\033[0m") # Perfumaria

    else: # Se pelo menos um campo estiver em branco
        driver.find_element_by_xpath("//*[@id=\"continue\"]").click()  
        error = driver.find_element_by_xpath("//*[@id=\"checkout_info_container\"]/div/form/div[1]/div[4]/h3").text # Clica em continuar a compra para capturar o erro (e o campo está vazio)
        
        print("\033[1;31;48m║        ERRO AO PREENCHER CAMPOS DA COMPRA       ║ >> ", error)
        print("\033[1;31;48m╚═════════════════════════════════════════════════╝\033[0m") # Perfumaria

    end = time.time()
    if end - start > 0.6:
        print("\033[1;33;48m║  PROBLEMA DE PERFORMANCE AO REALIZAR A COMPRA   ║\033[0m") # Perfumaria
        print("\033[1;33;48m╚═════════════════════════════════════════════════╝\033[0m") # Perfumaria
