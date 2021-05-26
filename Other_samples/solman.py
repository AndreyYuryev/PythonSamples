import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


class SolmanLoginFailed(Exception):
    pass


class SolmanWorklistFailed(Exception):
    pass


class SolmanItemFailed(Exception):
    pass


class SolmanCheckFailed(Exception):
    pass


class SolutionManager(object):
    def __init__(self, solman_url, driver_path, username, password, solpro=False):
        try:
            chrome_options = Options()
#            chrome_options.add_argument("--headless")
#            driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
            self.webdriver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
            self.webdriver.get(solman_url)
            self.driver = WebDriverWait(self.webdriver, 30)
            self.driver.until(EC.title_contains("Login"))
            self.driver.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
            self.driver.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
            self.driver.until(EC.presence_of_element_located((By.ID, "submit"))).click()

            # skip solman profile
            if solpro:
                self.driver.until(EC.element_to_be_clickable((By.ID, "YSOLMANPRO"))).click()

            self.driver.until(EC.title_contains("Home"))
            self.driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'CRMApplicationFrame')))
            self.driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'WorkAreaFrame1')))

        except WebDriverException:
            raise SolmanLoginFailed('Login error')

    def request(self, cd_number):
        if cd_number == "":
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
                .send_keys(cd_number)
            self.driver.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "Searchbtn")]'))).click()
            time.sleep(1)
            self.driver.until(
                EC.element_to_be_clickable((By.XPATH, '//*[contains(@id, "result_table[1].description")]'))).click()
            time.sleep(3)
            return Request(cd_number, self.driver)

        except WebDriverException:
            raise SolmanItemFailed('Request select failed')

    def close(self):
        self.webdriver.close()
        time.sleep(1)


class Request(object):
    def __init__(self, cd_number, driver):
        self.driver = driver
        self.number = cd_number

    def check(self):
        try:
            self.driver.until(EC.title_contains("Change"))
            self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "EDIT")]'))).click()
            time.sleep(3)
            self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "ACTIONS")]'))).send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            action = self.driver.until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "ACTIONS__items")]')))
            action[0].send_keys(Keys.ENTER)
            time.sleep(3)
            self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "SAVE")]'))).click()

        except WebDriverException:
            raise SolmanCheckFailed('Action failed')
