import time
from selenium import webdriver as Webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

class SolmanItemFailed(Exception):
    pass

class SolmanCheckFailed(Exception):
    pass

class SolmanWorklistFailed(Exception):
    pass

class BrowserFailed(Exception):
    pass

class BrowserCloseFailed(Exception):
    pass

class AuthentificationFailed(Exception):
    pass


class SeleniumBrowser(object):
    def __init__(self, path, endpoint):
        try:
            chrome_options = Options()
            #            chrome_options.add_argument("--headless")
            #            driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
            self.driver = Webdriver.Chrome(executable_path=path, options=chrome_options)
            self.driver.get(endpoint)
            self.wait_driver = WebDriverWait(self.driver, 30)
        except WebDriverException:
            raise BrowserFailed('Browser open error')

    def auth(self, username, password, solpro=False):
        try:
            self.wait_driver.until(EC.title_contains("Login"))
            self.wait_driver.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
            self.wait_driver.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
            self.wait_driver.until(EC.presence_of_element_located((By.ID, "submit"))).click()
            # skip solman added profile
            if solpro:
                self.wait_driver.until(EC.element_to_be_clickable((By.ID, "YSOLMANPRO"))).click()

            self.wait_driver.until(EC.title_contains("Home"))
            self.wait_driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'CRMApplicationFrame')))
            self.wait_driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'WorkAreaFrame1')))

        except WebDriverException:
            raise AuthentificationFailed('Authentification error')

    def open_request(self, CD):
        if CD == "":
            raise SolmanCheckFailed("Empty CD number")

        try:
            self.driver.until(EC.presence_of_element_located((By.LINK_TEXT, "Worklist"))).click()
        except WebDriverException:
            raise SolmanWorklistFailed('Worklist select failed')

        try:
            self.driver.until(
                EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search_parameters[1].FIELD")]'))) \
                .send_keys(Keys.ARROW_DOWN)
            self.driver.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@key, "OBJECT_ID")]'))).click()
            time.sleep(1)
            self.driver.until(
                EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search_parameters[1].VALUE1")]'))) \
                .clear()
            self.driver.until(
                EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "search_parameters[1].VALUE1")]'))) \
                .send_keys(CD)
            self.driver.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "Searchbtn")]'))).click()
            time.sleep(1)
            self.driver.until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "result_table[1].description")]'))).click()
            time.sleep(3)

        except WebDriverException:
            raise SolmanItemFailed('Request select failed')

    def double_check(self):
        pass

    def close(self):
        try:
            self.driver.close()
        except WebDriverException:
            raise BrowserCloseFailed('Browser close error')