import keyring


class Credential:
    def __init__(self, alias, config):
        self.alias = alias
        self.config = config
        self.password = str()

    def get_credential(self):
        username = self.config.username
        password = keyring.get_password(self.alias, username)
        self.password = password

    def is_exist(self):
        if self.config.username is not None and self.config.username != '' and\
                self.password is not None and self.password != '':
            return True
        else:
            return False

    def save(self, password):
        try:
            keyring.set_password(self.alias, self.config.username, password)
        except Exception as error:
            print('Error: {}'.format(error))
