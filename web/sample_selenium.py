from selenium import webdriver

# Указываем полный путь к geckodriver.exe на вашем ПК.
executable_path = "C\:\\Users\\home\\geckodriver.exe"
driver = webdriver.Firefox() #  executable_path=executable_path)
driver.get("http://www.google.com")