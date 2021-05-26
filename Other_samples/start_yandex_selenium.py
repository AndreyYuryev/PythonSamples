from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

time.sleep(4)
browser = webdriver.Chrome(executable_path='C:\\Users\\ayuryev\\PycharmProjects\\chromedriver.exe')
browser.implicitly_wait(10)
#browser.get('http://yandex.ru')
browser.get('https://onesolman.one-erp.telekom.de/sap(bD1lbiZjPTEwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm')

assert "Login" in browser.title
userform = browser.find_element_by_id('_loginForm_')
username = userform.find_element_by_id('username')
password = userform.find_element_by_id('password')
button = userform.find_element_by_id("submit")

username.send_keys("andrey.yuryev@t-systems.com")
password.send_keys("CiAm2016")
button.click()

time.sleep(2)
browser.find_element_by_id("YSOLMANPRO").click()

time.sleep(5)
assert "Home" in browser.title
#frame = browser.find_elements_by_xpath('//*[@id="crmUIHostFrameContainer"]//child::iframe')
browser.switch_to.frame(frame_reference='CRMApplicationFrame')
browser.switch_to.frame(frame_reference='WorkAreaFrame1')
browser.find_element_by_link_text('Worklist').click()

time.sleep(3)
assert 'Worklist' in browser.title
field = browser.find_element_by_xpath('//input[contains(@id, "search_parameters[1].FIELD")]')
if field is not None:
    field.send_keys(Keys.ARROW_DOWN)

browser.find_element_by_xpath('//*[contains(@key, "OBJECT_ID")]').click()

time.sleep(2)
value1 = browser.find_element_by_xpath('//input[contains(@id, "search_parameters[1].VALUE1")]')
if value1 is not None:
#    value1.send_keys("3065128834")
    value1.send_keys("3065128352")

time.sleep(2)
srsh = browser.find_element_by_xpath('//*[contains(@id, "Searchbtn")]')
if srsh is not None:
    srsh.click()

time.sleep(1)
browser.find_element_by_xpath('//*[contains(@id, "result_table[1].description")]').click()

time.sleep(5)
assert "Change:" in browser.title
browser.find_element_by_xpath('//*[contains(@id, "EDIT")]').click()

time.sleep(2)
browser.find_element_by_xpath('//*[contains(@id, "ACTIONS")]').send_keys(Keys.ARROW_DOWN)

time.sleep(1)
act = browser.find_elements_by_xpath('//a[contains(@id, "ACTIONS__items")]')
if act is not None:
    act[0].send_keys(Keys.ENTER)

time.sleep(2)
browser.find_element_by_xpath('//*[contains(@id, "SAVE")]').click()

time.sleep(2)
msg = browser.find_elements_by_xpath('//*[contains(@id,"CRMMessageLine")]')
for itmm in msg:
    print(itmm.text)
