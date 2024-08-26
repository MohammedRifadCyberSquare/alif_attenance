from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from pages.landing_page import LandingPage
from pages.admin_dashboard import AdminDashboard


Builder.load_file('kv/landing_page.kv')
Builder.load_file('kv/admin_dashboard.kv')


class MyScreenManager(ScreenManager):
    """
    Custom ScreenManager for handling different screens in the app.
    """
    pass

class AttendanceApp(MDApp):
     def build(self):
           sm = MyScreenManager()
        #    self.theme_cls.primary_palette = "Blue"  
        #    self.theme_cls.theme_style = "Light" 
           sm.add_widget(LandingPage(name='landing'))
           sm.add_widget(AdminDashboard(name='admin_dashboard'))

           sm.current = 'landing'
           return sm
     
if __name__ == '__main__':
    AttendanceApp().run()