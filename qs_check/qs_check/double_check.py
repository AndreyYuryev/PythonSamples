import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import argparse
import os


class Check:
    def __init__(self, path, url):
        self.driver_path = path
        self.url = url

    def browser(self):
        self.webdriver = webdriver.Chrome(executable_path=self.driver_path)
        self.webdriver.get(self.url)
        self.driver = WebDriverWait(self.webdriver, 60)

    def login(self, username, password):
        self.driver.until(EC.title_contains("Login"))
        self.driver.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
        self.driver.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        self.driver.until(EC.presence_of_element_located((By.ID, "submit"))).click()

    def skip_pro(self):
        self.driver.until(EC.element_to_be_clickable((By.ID, "YSOLMANPRO"))).click()

    def select_request(self, cd_number):
        self.driver.until(EC.title_contains("Home"))
        self.driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'CRMApplicationFrame')))
        self.driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'WorkAreaFrame1')))
        self.driver.until(EC.presence_of_element_located((By.LINK_TEXT, "Worklist"))).click()
        self.driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search_parameters[1].FIELD")]'))) \
            .send_keys(Keys.ARROW_DOWN)
        self.driver.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@key, "OBJECT_ID")]'))).click()
        time.sleep(1)
        self.driver.until(
            EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search_parameters[1].VALUE1")]'))) \
            .send_keys(cd_number)
        self.driver.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "Searchbtn")]'))).click()
        time.sleep(1)
        self.driver.until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "result_table[1].description")]'))).click()
        time.sleep(5)


    def check(self):
        self.driver.until(EC.title_contains("Change"))
        self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "EDIT")]'))).click()
        time.sleep(3)
        self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "ACTIONS")]'))).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        action = self.driver.until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "ACTIONS__items")]')))
        action[0].send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "SAVE")]'))).click()

    def close_double(self):
        self.webdriver.close()
        time.sleep(1)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--d', '--path', help='Path webdriver')
    parser.add_argument('--u', '--username', help='Username')
    parser.add_argument('--p', '--password', help='Password')
    parser.add_argument('--c', '--cd', help='CD number')
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.d is not None and namespace.u is not None and namespace.p is not None and namespace.c is not None:
        username = namespace.u
        password = namespace.p
        cd_number = namespace.c
        path = os.path.join(namespace.d, 'chromedriver.exe')
    try:

        url = 'https://onesolman.one-erp.telekom.de/sap(bD1lbiZjPTEwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm'
        double_check = Check(path=path, url=url)
        double_check.browser()
        double_check.login(username=username, password=password)
        double_check.select_request(cd_number=cd_number)
        double_check.check()

    finally:
        pass
