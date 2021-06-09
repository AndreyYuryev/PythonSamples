import pyodata
import requests
from pyodata.v2.service import GetEntitySetFilter as sef
from pyodata.v2.model import PolicyFatal, PolicyWarning, PolicyIgnore, ParserError, Config


SERVICE_URL = 'http://psl-e.one-erp.telekom.de/sap/opu/odata/SAP/ZPSL_GWSAMPLE_BASIC_SRV/'
# SERVICE_URL = 'http://psl-e.one-erp.telekom.de/sap/opu/odata/SAP/ZPSL_GWSAMPLE_BASIC_SRV/?sap-client=400&sap-language=EN'

session = requests.Session()
# session.auth = ('44544331', 'Fhm9Z2478p!EW')
session.auth = ('44544331', 'xmXxPj6GXZHa!')
session.param = {'sap-client': '200', 'sap-language': 'EN'}

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


# response = requests.get(SERVICE_URL,session)
# print(response.status_code)     # To print http response code
# print(response.text)
# r = response.text.json()
services = pyodata.Client(url=SERVICE_URL,connection=session, config=custom_config)

bp_request = services.entity_sets.BusinessPartnerSet.get_entities().execute()
#bp_request = bp_request.filter("BusinessPartnerID EQ '0100000000'")
# print(bp_request)
#for itm in bp_request.execute():
#    print(itm)
# bp_request = bp_request.filter(sef.and_(bp_request.Address['City'] == 'Waldorf', bp_request.
#                                         Address['PostalCode'] == '69190'))
# for bp in bp_request.execute():
#     print(bp.PostalCode)

# print(partners.Address)
# r = partners.Address
# for itm in r['City']:
#     print(itm)
# partner = partners.select('City, PostalCode').execute()
# for item in partner.execute():
#     print(item)
# order = services.entity_sets.PMOrderSet.get_entity('000300229310')
# for service in services.entity_sets._entity_sets:
#     print(service)
# print(order._entity_key._proprties.items())
# print(order._entity_key.items())
print('test')

