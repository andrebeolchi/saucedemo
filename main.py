from func import *

username = ["standard_user", "problem_user", "not_valid_user", "locked_out_user", "performance_glitch_user"]
password = "secret_sauce"

for user in username:
    userPrint(user)
    
    login(user, password)

    user_logged = validate_login()

    if user_logged == True:

        check_images()

        list_products()

        check_products()

        add_remove()

        cart()

    driver.get("https://www.saucedemo.com/")