import pyodata
import requests


# SERVICE_URL = 'http://erpcixpl01:8001/sap/opu/odata/sap/ZCS_EBGCP_SRV/'
SERVICE_URL = 'https://psl-e.one-erp.telekom.de/sap/opu/odata/sap/ZCS_EBGCP_SRV/$metadata?sap-client=400&sap-language=EN$format=xml'

session = requests.Session()
session.auth = ('44544331', 'MyPassword')

theservice = pyodata.Client(SERVICE_URL, session)