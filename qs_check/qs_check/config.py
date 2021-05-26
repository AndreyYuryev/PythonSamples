import configparser


class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        self.username = str()
        self.path = str()
        self.url = str()
        self.username, self.path, self.url = self.get_config()

    def get_config(self):
        config_file = configparser.ConfigParser()
        config_file.read(self.config_path, encoding='utf-8')
        username = config_file.get('config', 'username')
        path = config_file.get('config', 'path')
        url = config_file.get('config', 'url')
        return username, path, url

    def set_config(self, username):
        config_file = configparser.ConfigParser()
        config_file.read(self.config_path, encoding='utf-8')
        config_file.set('config', 'username', username)
        with open(self.config_path, 'w', encoding='utf-8') as cnf_file:
            config_file.write(cnf_file)

    def is_exist_username(self):
        if self.username is not None and self.username != "":
            return True
        else:
            return False
