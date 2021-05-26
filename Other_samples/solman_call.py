import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(wd):
    wd.until(EC.title_is("Login"))
    wd.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("andrey.yuryev@t-systems.com")
    wd.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("CiAm2016")
    wd.until(EC.presence_of_element_located((By.ID, "submit"))).click()


def set_profile(wd):
    wd.until(EC.element_to_be_clickable((By.ID, "YSOLMANPRO"))).click()
#    solman_profile = brws.find_element_by_id("YSOLMANPRO")
#    if solman_profile is not None:
#        solman_profile.click()


def set_frame(wd):
    wd.until(EC.title_contains("Home"))
    wd.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'CRMApplicationFrame')))
    wd.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'WorkAreaFrame1')))
#    brws.switch_to.frame(frame_reference='CRMApplicationFrame')
    #brws.switch_to.frame(frame_reference='WorkAreaFrame1')


def set_worklist(wd):
    #wd.until(EC.title_contains("Home"))
    wd.until(EC.presence_of_element_located((By.LINK_TEXT, "Worklist"))).click()


def search_cd(wd, cdnr):
    wd.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search_parameters[1].FIELD")]')))\
        .send_keys(Keys.ARROW_DOWN)
    #field = brws.find_element_by_xpath('//input[contains(@id, "search_parameters[1].FIELD")]')
    #if field is not None:
    #    field.send_keys(Keys.ARROW_DOWN)
    wd.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@key, "OBJECT_ID")]'))).click()
    #brws.find_element_by_xpath('//*[contains(@key, "OBJECT_ID")]').click()
    time.sleep(1)
    wd.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search_parameters[1].VALUE1")]')))\
        .send_keys(cdnr)
    #vals = browser.find_elements_by_xpath('//input[contains(@id, "search_parameters[1].VALUE1")]')
    #for itm in vals:
    #    print(itm.text)
    #value1 = browser.find_element_by_xpath('//*[contains(@id, "search_parameters[1].VALUE1")]')
    #if value1 is not None:
    #    #value1.send_keys(cdnr)
    #    print(value1.text)
    #    value1.send_keys("3065128352")
    #time.sleep(1)
    wd.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "Searchbtn")]'))).click()

    #search_btn = brws.find_element_by_xpath('//*[contains(@id, "Searchbtn")]')
    #if search_btn is not None:
    #    search_btn.click()
    time.sleep(1)
    wd.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "result_table[1].description")]'))).click()
    #brws.find_element_by_xpath('//*[contains(@id, "result_table[1].description")]').click()
    time.sleep(5)
    #wd.until(EC.title_contains("Change:"))
    #brws.find_element_by_xpath('//*[contains(@id, "result_table[1].description")]').click()


def double_check(wd):
    #time.sleep(1)
    wd.until(EC.title_contains("Change"))
    wd.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "EDIT")]'))).click()
    #brws.find_element_by_xpath('//*[contains(@id, "EDIT")]').click()
    time.sleep(2)
    wd.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "ACTIONS")]'))).send_keys(Keys.ARROW_DOWN)
    #brws.find_element_by_xpath('//*[contains(@id, "ACTIONS")]').send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    action = wd.until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "ACTIONS__items")]')))
    action[0].send_keys(Keys.ENTER)
    #act = brws.find_elements_by_xpath('//a[contains(@id, "ACTIONS__items")]')
    #if act is not None:
    #    act[0].send_keys(Keys.ENTER)
    time.sleep(2)
    wd.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "SAVE")]'))).click()
    #brws.find_element_by_xpath('//*[contains(@id, "SAVE")]').click()


def show_msg(brws):
    time.sleep(2)
    msg = brws.find_elements_by_xpath('//*[contains(@id,"CRMMessageLine")]')
    for itm in msg:
        print(itm.text)

if __name__ == "__main__":

    browser = webdriver.Chrome(executable_path='C:\\Users\\ayuryev\\PycharmProjects\\chromedriver.exe')
    browser.get('https://onesolman.one-erp.telekom.de/sap(bD1lbiZjPTEwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm')
    wait = WebDriverWait(browser, 15)
    try:
        # login form
        login(wait)

        # profile
        set_profile(wait)

        #time.sleep(5)

        # set frame
        #assert "Home" in browser.title
        set_frame(wait)

        set_worklist(wait)

        #time.sleep(3)

        # search CD
        #assert 'Worklist' in browser.title
        #cd = str("3065128352")
        cd = str("3065128806")
        #cd = str("3065128834")
        search_cd(wait, cd)

        #time.sleep(5)
        # set double click and save
        #assert "Change:" in browser.title
        double_check(wait)

        # show message
        #show_msg(browser)


    finally:
        pass
        #browser.quit()
