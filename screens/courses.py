from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = """
<CoursesScreen>

    name: "courses"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Cursos"

            left_action_items:
                [["arrow-left", lambda x: app.change_screen("home")]]

        ScrollView:

            MDList:

                OneLineListItem:
                    text: "Curso de Panadería"

                OneLineListItem:
                    text: "Curso de Belleza"

                OneLineListItem:
                    text: "Curso de Computación"

                OneLineListItem:
                    text: "Curso de Inglés"
"""

Builder.load_string(KV)


class CoursesScreen(MDScreen):
    pass
