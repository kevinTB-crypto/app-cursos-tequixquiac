from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

# Importaciones de tus pantallas y base de datos
from screens.home import HomeScreen
from screens.courses import CoursesScreen
from screens.register import RegisterScreen
from screens.admin import AdminScreen
from screens.edit_course import EditCourseScreen
from screens.login import LoginScreen
from database.db import Database


class MainApp(MDApp):

    def build(self):
        # Configuración del tema gráfico
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        # Inicialización y población inicial de la Base de Datos
        db = Database()
        courses = db.get_courses()
        
        if len(courses) == 0:
            db.add_course("Panadería", "Aprende elaboración de pan.", "3 meses")
            db.add_course("Computación", "Curso básico de informática.", "2 meses")
            db.add_course("Belleza", "Curso profesional de estilismo.", "4 meses")

        # Configuración del Administrador de Pantallas
        sm = ScreenManager()

        # Asignamos nombres explícitos para que funcionen perfectamente con change_screen
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CoursesScreen(name="courses"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(AdminScreen(name="admin"))
        sm.add_widget(EditCourseScreen(name="edit_course"))
        sm.add_widget(LoginScreen(name="login"))

        # Definimos la pantalla con la que arrancará la app (ejemplo: login)
        sm.current = "login" 

        return sm

    def change_screen(self, screen_name):
        """Cambia la pantalla actual de la aplicación."""
        if self.root.has_screen(screen_name):
            self.root.current = screen_name
        else:
            print(f"Error: La pantalla '{screen_name}' no existe en el ScreenManager.")


if __name__ == "__main__":
    MainApp().run()
