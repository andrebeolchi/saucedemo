from func import *

option = Options()
option.headless = False
driver = webdriver.Chrome(executable_path=('chromedriver.exe'),options=option)

driver.get("https://www.saucedemo.com/")

html = driver.page_source

username = ["standard_user", "problem_user"]#, "locked_out_user", "performance_glitch_user"]
password = "secret_sauce"

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

        add_remove()

        cart()

    driver.get("https://www.saucedemo.com/")
