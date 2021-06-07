import pyodata
import requests


# SERVICE_URL = 'http://erpcixpl01:8001/sap/opu/odata/sap/ZCS_EBGCP_SRV/'
SERVICE_URL = 'https://psl-e.one-erp.telekom.de/sap/opu/odata/sap/ZCS_EBGCP_SRV/$metadata?sap-client=300&sap-language=EN$format=xml'

session = requests.Session()
session.auth = ('44544331', 'bFdn2RY8A!5u')

theservice = pyodata.Client(SERVICE_URL, session)

order = theservice.entity_sets.PMOrderSet.get_entity('000300229310')

# print(order._entity_key._proprties.items())
# print(order._entity_key.items())

