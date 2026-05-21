from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.home import HomeScreen
from screens.courses import CoursesScreen
from screens.register import RegisterScreen
from screens.admin import AdminScreen


class MainApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        sm = ScreenManager()

        sm.add_widget(HomeScreen())
        sm.add_widget(CoursesScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(AdminScreen())

        return sm

    def change_screen(self, screen_name):
        self.root.current = screen_name


MainApp().run()
