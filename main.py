import os


os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.uix.transition import MDSwapTransition
from Screens.Manager import SM
from Screens.HomeScreen import HomeScreen
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window,WindowBase
from kivymd.uix.list import OneLineIconListItem

kv ="""
# import SM Screens.Manager
# import HomeScreen Screens.HomeScreen'


"""

Window.size = (420,670)
from kivy.properties import StringProperty

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
    
class myapp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
         
        
    def build_config (self, config):
        config.setdefaults('data ', {
            'items':[
                {'title':'The Home','icon':'home', 'body':'This Is Home'},
            ]
        })
        return super().build_config(config)
        
    def build(self):
        sm = SM(transition=MDSwapTransition(), config=self.config)
        
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = 'Light'
        
        sm.add_widget(HomeScreen(name='home'))
        
        return sm
    
    def handle_keyboard(self, key, *args):
        print(key)
    
        
myapp().run()