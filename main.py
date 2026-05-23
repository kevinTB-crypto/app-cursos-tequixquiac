from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.fitimage import FitImage

from screens.home import HomeScreen
from screens.courses import CoursesScreen
from screens.register import RegisterScreen
from screens.admin import AdminScreen
from database.db import Database
from screens.edit_course import EditCourseScreen
from screens.login import LoginScreen


class MainApp(MDApp):
    def build(self):
        return MDLabel(
            text="",    
            theme_text_color="RED"
        )


    def build(self):

        # MODIFICACIÓN: Cambiado de "Blue" a "DeepPurple"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        db = Database()

        courses = db.get_courses()

        if len(courses) == 0:

            db.add_course("Panadería", "Aprende elaboración de pan.", "3 meses")

            db.add_course("Computación", "Curso básico de informática.", "2 meses")

            db.add_course("Belleza", "Curso profesional de estilismo.", "4 meses")

        sm = ScreenManager()

        sm.add_widget(HomeScreen())
        sm.add_widget(CoursesScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(AdminScreen())
        sm.add_widget(EditCourseScreen())
        sm.add_widget(LoginScreen())

        return sm

    def change_screen(self, screen_name):
        self.root.current = screen_name


MainApp().run()
