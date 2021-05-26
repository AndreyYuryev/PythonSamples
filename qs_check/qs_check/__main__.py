from qs_check import Application, Config, Check, Credential, RequestNumber, SolutionManager, Request


def main():
    try:
        config = Config(config_path='config.ini')
        credential = Credential(alias='Python_QS_check', config=config)
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
