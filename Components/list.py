
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivy.lang import Builder
from kivymd.uix.behaviors import TouchBehavior
import Screens.HomeScreen

Builder.load_string('''
<myList>:
    IconLeftWidgetWithoutTouch:
        icon:root.icon
''')

class myList(TouchBehavior,TwoLineAvatarIconListItem):
    def __init__(self,icon,itemId=None, *args, **kwargs):
        self.icon = icon
        self.itemId = itemId
        self.text = kwargs.get('text')
        self.body = kwargs.get('secondary_text')
        
        super().__init__(*args, **kwargs)
       
    def action(self):
        # home = Screens.HomeScreen.HomeScreen()
        # home.handle_list_action(self)
        ...
    @property
    def getText(self):
        return self.text
    
    @property
    def getBody(self) -> str:
        return self.body
    
    @property
    def getIcon(self) -> str:
        return self.icon
    
    @property
    def getItemId(self) -> int:
        return self.itemId

    def on_long_touch(self, touch, *args):
        return super().on_long_touch(touch, *args)