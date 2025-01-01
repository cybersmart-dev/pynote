
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import ScreenManager

Builder.load_string('''
<ViewNoteScreen>:
    MDBoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            id:toolbar
            title:'PyNote'
            anchor_title:'left'
            left_action_items:[['arrow-left', lambda x: root.back() , 'arrow-left']]
            right_action_items:[['dots-vertical', lambda x: x, 'More Action']]
            
        MDScreen:
            MDLabel:
                id:body                
''')
class ViewNoteScreen(MDScreen):
    def __init__(self,parsing_data_dict:dict={}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        body:MDLabel = self.ids.body
        
        body.allow_copy = True

        body.text = parsing_data_dict.get('body')
        self.ids.toolbar.title = parsing_data_dict.get('title')
        
        self.manager:ScreenManager = self.manager
        
    def back(self):
        self.manager.current = 'home'