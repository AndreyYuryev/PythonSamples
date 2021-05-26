# from solman import Application
from solman_api import SolManAPI, BrowserFailed,BrowserCloseFailed, AuthentificationFailed

def main():
#    app = Application()
#    app.workflow()
    slmn = SolManAPI(driver_path="C:\\Users\\ayuryev\\PycharmProjects\\chromedriver.exe")
    slmn.auth(username="andrey.yuryev@t-systems.com", password="CiAm2016", skip_profile=True)
    rqst = slmn.request(CD_number='3065128860')
    rqst.qs_check()
    slmn.exit()

if __name__ == '__main__':
    main()

