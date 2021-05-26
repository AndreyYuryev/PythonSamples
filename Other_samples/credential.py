import getpass
import keyring
import sys

my_server = 'python_password'

def windows_credential():
    # look there: cmd -> control userpasswords2 -> Advanced -> Manage passwd -> Windows Credential
    #passwd = getpass.getpass(prompt='Please input password for account: ')
    try:
        #keyring.set_password(my_server, getpass.getuser(), passwd)
        keyring.set_password(my_server,"andrey.yuryev@t-systems.com", "CiAm2016")
        print('The Windows credential was sucessfully created for host: {} and user: {}'.format(my_server, getpass.getuser()))
    except Exception as error:
        print('Error: {}'.format(error))

def get_passwd():
    passwd = keyring.get_password(my_server, "andrey.yuryev@t-systems.com")
    #passwd = keyring.get_password(my_server, getpass.getuser())
    if passwd is None:
        print('Please create windows credential for host')
        sys.exit(1)
    return passwd



windows_credential()

print(get_passwd())
