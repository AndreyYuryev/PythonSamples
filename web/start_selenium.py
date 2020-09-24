import webbrowser, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os

browser = webdriver.Firefox(executable_path='C:\\Users\\home\\geckodriver.exe')
browser.implicitly_wait(40)
browser.get('http://yandex.ru')

