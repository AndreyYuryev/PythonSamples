import pyodata
import requests
from pyodata.v2.service import GetEntitySetFilter as sef


# SERVICE_URL = 'http://erpcixpl01:8001/sap/opu/odata/sap/ZCS_EBGCP_SRV/'
SERVICE_URL = 'https://psl-e.one-erp.telekom.de/sap/opu/odata/SAP/ZPSL_GWSAMPLE_BASIC_SRV/$metadata?sap-client=400&sap-language=EN'

session = requests.Session()
session.auth = ('44544331', 'Fhm9Z2478p!EW')


# response = requests.get(SERVICE_URL, session)
# print(response.status_code)     # To print http response code
# print(response.text)
# r = response.text.json()
services = pyodata.Client(SERVICE_URL, session)

bp_request = services.entity_sets.BusinessPartnerSet.get_entities().select('BusinessPartner').execute()
bp_request = bp_request.filter("BusinessPartnerID EQ '0100000000'")
# print(bp_request)
for itm in bp_request.execute():
    print(itm)
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

