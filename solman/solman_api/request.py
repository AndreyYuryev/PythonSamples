

class ChangeRequest(object):
    def __init__(self, browser, CD_number):
        self.cd_number = CD_number
        self.browser = browser

    def qs_check(self):
        self.browser.open_request(CD=self.cd_number)
        self.browser.qs_check()
