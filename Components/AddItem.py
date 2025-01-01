
import typing
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.icon_definitions import md_icons
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu

Builder.load_string('''
<addNewItemContents>:
    padding:'5dp'
    size_hint_y:None
    height: "320dp"
    BoxLayout:
        orientation:'vertical'
        padding:15
        spacing:25
        MDLabel:
            id:dialog_title
            
            font_style:'H5'
            halign:'center'
            
        MDTextField:
            id:title
            mode:'fill'
            helper_text:'Title of your item'
            hint_text:'Title'
            padding:'20dp'
            radius:[5,5,0,0]
            required:True
            
        MDTextField:
            id:icon
            mode:'rectangle'
            helper_text:'Icon of your item'
            hint_text:'Icon'
            padding:'20dp'
            icon_right:'icon'
            radius:[5,5,0,0]
            required:True
            on_focus:root.show_icon(icon)
            on_text:root.handle_icon_change(icon)
            
        MDTextField:
            id:body
            mode:'rectangle'
            helper_text:'body of your new item'
            hint_text:'body'
            padding:'20dp'
            size_hint_y:None
            height:"30dp"
            radius:[5,5,0,0]
            required:True
           
        MDRaisedButton:
            text:'Save'
            pos_hint:{'center_x':.5}
            on_press:root.save(title,icon, body)            
''')

class addNewItemContents(MDScreen):
    
    def __init__(self,app=None,dialog=None,type=None, data:dict=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.dialog:MDDialog = dialog
        self.type:int = type
        self.data = data
        
        self.items = [
            {
                'viewclass':'CustomOneLineIconListItem',
                'text':icon_name,
                'icon':icon_name,
                'on_press':lambda x= icon_name : self.callback(x)
                
            }for icon_name in md_icons.keys()
        ]
        
        
        if type == 1:
            self.ids.title.text = data.get('title')
            self.ids.icon.text = data.get('icon')
            self.ids.body.text = data.get('body')
            self.ids.dialog_title.text = 'Edit Item'
        else:    
            self.ids.dialog_title.text = 'Add New Item'

    def show_icon(self, w):
        
        self.menu = MDDropdownMenu(
            items=self.items,
            caller=w
        )
        self.menu.open()
        
    def callback(self, x):
        self.ids.icon.text = x
    def handle_icon_change(self, input:MDTextField):
        input.icon_right = input.text
        
    def save(self, title:MDTextField,icon:MDTextField, body:MDTextField):
        if self.type == 0:
            item = {'title':title.text,'icon':icon.text,'body':body.text}
            self.app.items.append(item)
            self.app.display(self.app.items)
            self.dialog.dismiss()
            
        elif self.type == 1:
            id = self.data.get('id')
            item:dict = self.app.items[id]
            item['title'] = title.text
            item['icon'] = icon.text
            item['body'] = body.text
            
            self.app.display(self.app.items)
            self.dialog.dismiss()
        
    def on_load(self,calable:typing.Callable[[bool], None]):
        self.dialog = calable
    
    @staticmethod
    def TYPE_EDIT() -> int:
        return 1
    
    @staticmethod 
    def TYPE_ADD() -> int:
        return 0
