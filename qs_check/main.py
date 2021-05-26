from qs_check import *
import configparser


class NewCredential(Credential):
    def get_credential(self):
        username = self.config.username
        config_file = configparser.ConfigParser()
        config_file.read(self.config.config_path, encoding='utf-8')
        self.password = config_file.get('config', 'password')

    def save(self, password):
        config_file = configparser.ConfigParser()
        config_file.read(self.config.config_path, encoding='utf-8')
        config_file.set('config', 'password', password)
        with open(self.config.config_path, 'w', encoding='utf-8') as cnf_file:
            config_file.write(cnf_file)


def main():
    try:
        config = Config(config_path='config.ini')
        credential = NewCredential(alias='Python_QS_check', config=config)
        request = RequestNumber()
        double_check = Check(path=config.path, url=config.url)
        app = Application(title="Double check", config=config, credential=credential,
                          request=request, double_check=double_check)
        app.run()
        app.mainloop()

    finally:
        pass


if __name__ == '__main__':
    main()