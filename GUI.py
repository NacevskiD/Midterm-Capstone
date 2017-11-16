from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.listview import ListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem, TabbedPanelHeader
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_string("""
<MyLabel>:
    font_size: 18
    halign: 'left'
    text_size: self.size
    
""")


import Database

class adminScreen(Screen):
    def __init__(self,**kwargs):
        super(adminScreen,self).__init__(**kwargs)

        db = Database.myDB()
        tab1 = TabbedPanel()
        tab1.do_default_tab = False

        th = TabbedPanelHeader(text='Admin')
        tab1.set_def_tab(th)
        tab1.add_widget(th)
        layout = GridLayout()
        layout.cols = 1

        th.content = layout

        th2 = TabbedPanelHeader(text = "Employees")
        tab1.add_widget(th2)
        layout2 = GridLayout()
        layout2.rows =1
        second = Label(text="Password")
        layout2.add_widget(second)
        th2.content = layout2
        data = db.getAll()
        simple_list_adapter = SimpleListAdapter(
            data=[str(i) for i in data],
            cls=MyLabel)

        list_view = ListView(adapter=simple_list_adapter)

        layout.add_widget(list_view)
        self.add_widget(tab1)



    def on_pre_enter(self):
        Window.size = (800, 600)


class MyLabel(Label):
    def __init__(self, **kwargs):


        super(MyLabel, self).__init__(**kwargs)


class LoginScreen(Screen):


    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = GridLayout()

        layout.rows = 3
        firstLabel = Label(text = "Username")
        layout.add_widget(firstLabel)
        self.userName = TextInput(multiline=False, font_size=20)
        #userName.bind(text =self.on_enter)
        layout.add_widget(self.userName)
        secondLabel = Label(text="Password")
        layout.add_widget(secondLabel)
        self.password = TextInput( multiline=False,font_size=20,password = True)
        layout.add_widget(self.password)
        login = Button(text = "Login")
        login.bind(on_press = self.callback)
        layout.add_widget(login)
        self.add_widget(layout)

    def on_pre_enter(self):
        Window.size = (300, 100)



    def callback(self,instance):
        print("Username: " + self.userName.text)
        print("Passowrd: " + self.password.text)
        db = Database.myDB()
        checkLogin,user = db.checkLogin(self.userName.text,self.password.text)
        if checkLogin:
            if user == 1:
                self.manager.current = 'screen2'




    #def on_enter(self,instace,value):
     #       print ("Input:" + value)



class MyApp(App):

    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = LoginScreen(name='screen1')
        screen2 = adminScreen(name='screen2')
        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        return my_screenmanager





if __name__ == '__main__':
    MyApp().run()