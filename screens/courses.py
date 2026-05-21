from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from components.course_card import CourseCard

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

            MDBoxLayout:
                id: courses_box
                orientation: "vertical"
                adaptive_height: True
                spacing: "20dp"
                padding: "20dp"
"""

Builder.load_string(KV)


class CoursesScreen(MDScreen):

    def on_enter(self):

        self.ids.courses_box.clear_widgets()

        courses = [
            {
                "title": "Panadería",
                "description": "Aprende elaboración de pan y repostería.",
                "duration": "3 meses",
            },
            {
                "title": "Belleza",
                "description": "Curso profesional de estilismo.",
                "duration": "4 meses",
            },
            {
                "title": "Computación",
                "description": "Ofimática y herramientas digitales.",
                "duration": "2 meses",
            },
            {
                "title": "Inglés",
                "description": "Curso básico e intermedio.",
                "duration": "6 meses",
            },
        ]

        for course in courses:

            card = CourseCard(
                title=course["title"],
                description=course["description"],
                duration=course["duration"],
            )

            self.ids.courses_box.add_widget(card)
