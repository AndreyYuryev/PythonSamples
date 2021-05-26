from solman import SolutionManager
import time

URL = 'https://onesolman.one-erp.telekom.de/sap(bD1lbiZjPTEwMCZkPW1pbg==)/bc/bsp/sap/crm_ui_start/default.htm'
PATH = 'C:\\Users\\ayuryev\\PycharmProjects\\chromedriver.exe'
USER = 'andrey.yuryev@t-systems.com'
PASS = 'CiAm2016'
CD = '3065128860'
#CD = '4065128353'


slm = SolutionManager(solman_url=URL, driver_path=PATH, username=USER, password=PASS, solpro=True)
rqt = slm.request(cd_number=CD)
time.sleep(5)
#rqt2 = slm.request(cd_number=CD)
#rqt.check()
#time.sleep(5)
#slm.close()



