import pyodata
import requests


SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

northwind = pyodata.Client(SERVICE_URL, requests.Session())

employees = northwind.entity_sets.Employees.get_entities().select('EmployeeID,LastName').execute()
for employee in employees:
    print(employee.EmployeeID, employee.LastName)

print('test')