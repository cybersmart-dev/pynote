
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton,MDRaisedButton
from kivymd.uix.snackbar import MDSnackbar
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField
from Components.AddItem import addNewItemContents
from Components.list import myList
from Screens.SettingsScreen import SettingsScreen
from Screens.Manager import SM
from kivymd.uix.list import IconRightWidget
from Screens.ViewNoteScreen import ViewNoteScreen

Builder.load_string('''
<HomeScreen>
    MDScreen:
        MDBoxLayout:
            orientation:'vertical'
            MDTopAppBar:
                title:'PyNote'
                anchor_title:'left'
                left_action_items:[['menu', lambda x: drawer.set_state('open'), 'Menu']]
                right_action_items:[['dots-vertical', lambda x: x, 'More Action']]
                
            MDScreen: 
                MDBoxLayout:
                    orientation:'vertical'
                    
                    MDBoxLayout:
                        orientation:'horizontal'
                        size_hint_y:None
                        height:self.minimum_height
                        padding:20
                        spacing:10
                        
                        MDTextField:
                            id:search
                            mode:'round'
                            helper_text:'Search'
                            hint_text:'Search item '
                            padding:'20dp'
                            icon_right:'magnify'
                            radius:[5,5,0,0]
                            on_text:root.handle_input(search)
                            
                        MDFloatingActionButton:
                            elevation:2
                            icon:'plus'
                            type:'small'
                            on_press:root.add_new_item()
                            
                        
                    MDScrollView:
                        MDList:
                            id:container
                            
        MDNavigationDrawer:
            radius:0
            id:drawer
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title:'PyNote'
                    padding: "12dp", 0, 0, "56dp"
                    text: "Keep Your Note Safe"
                    spacing:'4dp'
                    
                MDNavigationDrawerItem:
                    icon:'home'
                    text:'HOME' 
                    selected:True
                    right_text:'current'
                    on_press:drawer.set_state('close')
                    
                MDNavigationDrawerItem:
                    icon:'cog'
                    text:'SETTINGS' 
                    selected:False
                    right_text:''
                    on_press:root.open_screen('settings')
                    
                MDNavigationDrawerLabel:
                    text:'More'
                    MDNavigationDrawerDivider:
                    
                MDNavigationDrawerItem:
                    icon:'door'
                    text:'EXIT' 
                    selected:True
                    right_text:''
                    on_press:drawer.set_state('close')
<CustomOneLineIconListItem>:
    IconLeftWidget:
        icon:root.icon
        
''')
class HomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = [
            {'title':'The Home','icon':'home', 'body':'This Is Home'},
            {'title':'The bank','icon':'bank', 'body':'this is bank'},
            {'title':'The card','icon':'card', 'body':'this is card'},
            {'title':'The school','icon':'school', 'body':'this is school'},
            {'title':'The bell','icon':'bell', 'body': 'this is bell'}
        ]
        
        self.manager:SM = self.manager
        
        
        self.display(self.items)
        
    def open_screen(self, screen_name = 'home'):
        print('Config ', self.manager.get_config().get('data', 'items'))
        if self.manager.has_screen(screen_name):
           self.manager.remove_widget(self.manager.get_screen(screen_name))
           
        self.manager.add_widget(SettingsScreen(name='settings'))
        
        if screen_name == 'settings':
            self.ids.drawer.set_state('close')
            
        self.manager.current = screen_name
        
    def add_new_item(self):
        add = addNewItemContents(app=self, type=addNewItemContents.TYPE_ADD())
        dialog = MDDialog(
                type='custom',
                content_cls = add
            )
        add.on_load(self.handle_load(dialog))
        print(addNewItemContents.TYPE_ADD())
        dialog.open()
        
        
    def handle_load(self,d):
        return d
    
    def edit_item(self,data:dict, dialog:MDDialog):
        dialog.dismiss()
        
        t = data.get('title')
        i = data.get('icon')
        b = data.get('body')
        id = data.get('id')
        
        data = {
           'title':t,
           'icon':i,
           'body':b,
           'id':id
       }
        
        add = addNewItemContents(app=self, type=addNewItemContents.TYPE_EDIT(),data=data)
        dialog = MDDialog(
                type='custom',
                content_cls = add
            )
        add.on_load(self.handle_load(dialog))
        dialog.open()
        
    def on_start(self):
        # self.display(self.items)
        # print(self.root.ids.container.children)
        ...
        
    def handle_press(self, w):
       if self.manager.has_screen('view'):
           self.manager.remove_widget(self.manager.get_screen('view'))
        
       title = w.getText
       icon = w.getIcon
       body = w.getBody
       id = w.getItemId
       data = {
           'title':title,
           'icon':icon,
           'body':body,
           'id':id
       }
       
       self.manager.add_widget(ViewNoteScreen(name='view',parsing_data_dict=data))
       if self.manager.has_screen('view'):
           self.manager.current = 'view'
    
    def handle_list_action(self, w:IconRightWidget):
        ins = None
        
        wd = [wid for wid in w.walk(loopback=True)]
        for wi in range(1,len(wd)):
            if isinstance(wd[wi], myList):
                ins = wd[wi] 
        w = ins
        
        title = w.getText
        icon = w.getIcon
        body = w.getBody
        id = w.getItemId
       
        data = {
           'title':title,
           'icon':icon,
           'body':body,
           'id':id
        }
       
        dialog = MDDialog(title=w.getText,text=f"You Select {w.getText}", buttons = [
           
           MDRectangleFlatButton(
               text="Ok",
               on_press=(lambda x: dialog.dismiss()),     
           ),
           
           MDRectangleFlatButton(
               text='Delete',
               line_color='red',
               text_color='red',
               on_press=(lambda event: self.remove_item(event=event,instance=w, dialog=dialog) )
           ),
           MDRectangleFlatButton(
               text='Edit',
               line_color='green',
               text_color='green',
               on_press=(lambda event: self.edit_item(data=data,dialog=dialog) )
           )
           
       ])
        dialog.auto_dismiss = False
        dialog.open()
    
    def remove_item(self,event:MDRaisedButton, instance:myList,dialog:MDDialog = None):
        
        dialog.dismiss()
        
        toast(text=f'{instance.getText} Deleted')
        
        del self.items[instance.getItemId]
        self.display(self.items)
         
    def display(self, items:list):
        if self.ids.container.children != []:
            self.ids.container.clear_widgets()
            
        for i in range(len(items)):
            item = items[i]
            mylist = myList(
                    text=f'{item['title']}',
                    secondary_text=item['body'],
                    icon=item['icon'], 
                    itemId=i,
                    on_press=self.handle_press)
            
            action = IconRightWidget(icon='dots-horizontal', on_press=self.handle_list_action)
            mylist.add_widget(action)
            self.ids.container.add_widget(mylist)
            
    def handle_input(self, input:MDTextField):
        text = input.text
        input.icon_right = 'close'
        if self.ids.search.text != '':
            input.icon_right = 'close'
        else:
            input.icon_right = 'magnify'
        result = self.search(self.items, query=text)
        self.display(result)
    
    def search(self, items:list, query:str):
        result = []
        
        for i in range(len(items)):
            title = self.items[i].get('title')
            body = self.items[i].get('body')
            
            if query.lower() in title.lower():
                if items[i] not in result:
                    result.append(items[i])
                    
            if query.lower() in body.lower():
                if items[i] not in result:
                    result.append(items[i])
        return result
        
