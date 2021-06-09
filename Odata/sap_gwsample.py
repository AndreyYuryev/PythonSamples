import pyodata
import requests
from pyodata.v2.model import PolicyFatal, PolicyWarning, PolicyIgnore, ParserError, Config


SERVICE_URL = 'http://psl-e.one-erp.telekom.de/sap/opu/odata/SAP/ZPSL_GWSAMPLE_BASIC_SRV/'

session = requests.Session()
# 400
session.auth = ('44544331', 'Fhm9Z2478p!EW')
# 200
# session.auth = ('44544331', 'xmXxPj6GXZHa!')
session.params = {'sap-client': 400, 'sap-language': 'EN'}

namespaces = {
    'atom': 'http://www.w3.org/2005/Atom',
    'app': 'http://www.w3.org/2007/app'
}
custom_config = Config(xml_namespaces=namespaces,
                       default_error_policy=PolicyFatal(),
                       custom_error_policies={
         ParserError.ANNOTATION: PolicyWarning(),
         ParserError.ASSOCIATION: PolicyIgnore()
    })

services = pyodata.Client(url=SERVICE_URL,connection=session, config=custom_config)
bp_request = services.entity_sets.BusinessPartnerSet.get_entities()
for item in bp_request.execute():
    print(item.BusinessPartnerID, item.CompanyName)