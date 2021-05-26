import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import os
from os import path
import pandas as pd
import configparser

SOLMAN_URL = 'https://onesolman.one-erp.telekom.de/sap(bD1lbiZjPTEwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm'
IN_DEV = 'In Development'
QS_CHK = 'QS-Check'
QS_DBL = 'Double-Check successful'


class ConnectError(WebDriverException):
    pass


class OpenRequestError(WebDriverException):
    pass


class ActionError(WebDriverException):
    pass


class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config_file = configparser.ConfigParser()

    def get_config(self):
        self.config_file.read(self.config_path, encoding='utf-8')
        username = self.config_file.get('config', 'username')
        driver_path = self.config_file.get('config', 'path')
        password = self.config_file.get('config', 'password')
        return username, password, driver_path


class ZDCIFile(object):
    def __init__(self, file_name):
        self.full_path = path.join(os.path.join(os.path.expanduser('~'), 'downloads'), file_name + '.xlsx')

    def has_error(self):
        sheet1 = pd.read_excel(self.full_path, sheet_name='Sheet1')
        msg = sheet1.count()
        if msg['Errors'] > 0:
            return True
        else:
            return False


class SolutionManagerDriver(object):
    def __init__(self, driver_path):
        chrome_options = Options()
        download_path = os.path.join(os.path.expanduser('~'), 'downloads')
        chrome_options.add_argument("download.default_directory=" + download_path)
        service = Service(executable_path=driver_path)
        #            chrome_options.add_argument("--headless")
        #            driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
        self.WebDriver = webdriver.Chrome(options=chrome_options, service=service)
        self.WebDriver.get(SOLMAN_URL)
        self.driver = WebDriverWait(self.WebDriver, 20)

    def wait_title(self, text):
        self.driver.until(EC.title_contains(text))

    def change_language(self):
        self.driver.until(EC.presence_of_element_located((By.ID, "language-selection")))
        select = Select(self.driver.until(EC.presence_of_element_located((By.ID, "language-selection"))))
        select.select_by_visible_text('English')

    def sign_in(self, username, password):
        self.driver.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
        self.driver.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        self.driver.until(EC.presence_of_element_located((By.ID, "submit"))).click()

    def sel_profile(self):
        self.driver.until(EC.element_to_be_clickable((By.ID, "YSOLMANPRO"))).click()

    def crm_frame(self):
        self.driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'CRMApplicationFrame')))
        self.driver.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'WorkAreaFrame1')))

    def work_list(self):
        self.driver.until(EC.presence_of_element_located((By.LINK_TEXT, "Worklist"))).click()

    def sel_request(self, cd_number):
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

    def press_edit(self):
        self.driver.until(EC.title_contains("Change"))
        self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "EDIT")]'))).click()
        time.sleep(2)

    def press_save(self):
        self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "SAVE")]'))).click()

    def press_cancel(self):
        self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "CANCEL")]'))).click()

    def press_action(self):
        self.driver.until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "ACTIONS")]'))).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        action = self.driver.until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "ACTIONS__items")]')))
        action[0].send_keys(Keys.ENTER)
        time.sleep(3)

    def cd_state(self):
        return self.driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "btadminh_lcstatus")]')))

    def go_to_transport(self):
        self.driver.until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@title, "Go To")]'))).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        action = self.driver.until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "__items__")]')))
        for itm in action:
            if itm.text == 'Transport Management':
                itm.send_keys(Keys.ENTER)
                return True
        return False

    def transport_name(self):
        rows = self.driver.until(
            # EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "ConfCellTable")]')))
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, ".trorder_number")]')))
        # cont_text = f'bttransreq_table[{len(rows)}].trorder_number'
        # cells = self.driver.until(
        #    EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, cont_text)]')))
        transport = rows[len(rows) - 1].text
        return f'ZDCI_{transport}'

    def go_to_attachments(self):
        self.driver.until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@title, "Go To")]'))).send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        action = self.driver.until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "__items__")]')))
        for itm in action:
            if itm.text == 'Attachments':
                itm.send_keys(Keys.ENTER)
                return True
        return False

    def download(self, transport_name):
        action = self.driver.until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@id, "kw_relative_url")]')))
        for itm in action:
            if itm.text == transport_name:
                itm.click()
                time.sleep(6)
                return True
        else:
            return False

    def close(self):
        self.WebDriver.close()
        time.sleep(1)


class Request(object):
    def __init__(self, manager_driver, request_number):
        self.manager_driver = manager_driver
        self.request_number = request_number
        self.status = str()

    def open(self):
        try:
            self.manager_driver.work_list()
            self.manager_driver.sel_request(cd_number=self.request_number)
            self.status = self.manager_driver.cd_state().text
        except WebDriverException:
            OpenRequestError(f'Error by opening request {self.request_number}')

    def complete(self):
        try:
            if self.status == QS_CHK and self.manager_driver.go_to_transport():
                ta_name = self.manager_driver.transport_name()
                if self.manager_driver.go_to_attachments():
                    if self.manager_driver.download(transport_name=ta_name):
                        inspect = ZDCIFile(file_name=ta_name)
                        if not inspect.has_error():
                            print("Execute action")
                            self.manager_driver.press_edit()
                            self.manager_driver.press_action()
                            self.manager_driver.press_save()
                        else:
                            print('Action is not possible. Error in protocol')
                    else:
                        print(f'File {ta_name} is not found')
            else:
                print(f'Action for status {self.status} is not possible')
        except WebDriverException:
            self.manager_driver.press_cancel()
            ActionError(f'Error by execute action for request {self.request_number}')


class SolutionManager(object):
    def __init__(self, driver_path, username, password, sol_profile=False):
        self.manager_driver = SolutionManagerDriver(driver_path=driver_path)

        try:
            self.manager_driver.wait_title("Login")
            self.manager_driver.change_language()
            self.manager_driver.sign_in(username=username, password=password)
            if sol_profile:
                self.manager_driver.sel_profile()
            self.manager_driver.wait_title("Home")
            self.manager_driver.crm_frame()
        except WebDriverException:
            ConnectError(f'Error by login user {username}')

    def change_request(self, request_number) -> Request:
        request = Request(manager_driver=self.manager_driver, request_number=request_number)
        request.open()
        return request

    def close(self):
        self.manager_driver.close()

def main():
    # get parameters
    cd = str(input('Please enter CD number:'))
    config_path = path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
    cfg = Config(config_path=config_path)
    user, pswd, chrome_driver_path = cfg.get_config()

    # execute double check
    solman = SolutionManager(driver_path=chrome_driver_path, username=user, password=pswd, sol_profile=True)
    chg_request = solman.change_request(request_number=cd)
    chg_request.complete()
    input('Please enter to exit')


if __name__ == "__main__":
    main()
