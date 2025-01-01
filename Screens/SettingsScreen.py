
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string('''
<SettingsScreen>:
    MDScreen:
        MDBoxLayout:
            orientation:'vertical'
            MDTopAppBar:
                title:'Settings'
                anchor_title:'left'
                left_action_items:[['arrow-left', lambda x: root.back(), 'Back']]
                right_action_items:[['dots-vertical', lambda x: x, 'More Action']]
                
            MDScreen:
                spacing:'10dp'
                padding:'4dp','4dp','10dp','0dp'
                MDNavigationDrawerMenu:
                    MDNavigationDrawerItem:
                        icon:'brightness-3'
                        text:'Dark Mode' 
                        selected:True
                        right_text:'light'
                        
                    MDNavigationDrawerItem:
                        icon:'contacts'
                        text:'Contact Us' 
                        selected:False
                        right_text:''
                        
                        
                    MDNavigationDrawerLabel:
                        text:'More'
                        MDNavigationDrawerDivider:
                        
                    MDNavigationDrawerItem:
                        icon:'lock'
                        text:'PRIVACY' 
                        selected:True
                        right_text:''
                              
''')

class SettingsScreen(MDScreen):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def back(self):
        self.manager.current = 'home'
        