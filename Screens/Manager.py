
from kivymd.uix.screenmanager import MDScreenManager

class SM(MDScreenManager):
    def __init__(self,config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config
        
    def get_config(self):
        return self.config