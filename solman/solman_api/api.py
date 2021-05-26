from .browser import SeleniumBrowser
from .request import ChangeRequest


class SolManAPI(object):
    """
    Implements the API that makes it possible to interact with
    Solution Manager account
    """
    def __init__(
        self,
        driver_path="./chromedriver",
        api_endpoint="https://onesolman.one-erp.telekom.de/sap(bD1lbiZjPTEwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm"
    ):
        self.driver_path = driver_path
        self.api_endpoint = api_endpoint
        self.browser = SeleniumBrowser(self.driver_path, self.api_endpoint)

    def auth(self, username, password, skip_profile=False):
        self.browser.auth(username=username,password=password,solpro=skip_profile)

    def request(self, CD_number):
        request = ChangeRequest(browser=self.browser, CD_number=CD_number)
        return request

    def exit(self):
        self.browser.close()