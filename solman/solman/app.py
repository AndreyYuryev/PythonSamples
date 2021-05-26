from solman import ProgramWindow, Config
from os import path
CONFIG_PATH = 'config.ini'

class Application():
    def __init__(self, credential, request, double_check):
        #config_path = path.join(path.abspath((path.dirname(__file__))), CONFIG_PATH)
        self.config = Config(config_path=CONFIG_PATH)
        self.prg_wnd = ProgramWindow(title="Double check", config=self.config, credential=credential,
                          request=request, double_check=double_check)

    def workflow(self):
        self.prg_wnd.run()
        self.prg_wnd.mainloop()
