from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from components.course_card import CourseCard
from database.db import Database

KV = """

<CoursesScreen>

    name: "courses"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Cursos"

            left_action_items:
                [["arrow-left",
                lambda x: app.change_screen("home")]]

        MDTextField:
            id: search_field
            hint_text: "Buscar curso..."
            size_hint_x: .95
            pos_hint: {"center_x": .5}
            on_text:
                root.search_courses(self.text)

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

        self.load_courses()

    def load_courses(self):

        self.ids.courses_box.clear_widgets()

        db = Database()

        courses = db.get_courses()

        self.show_courses(courses)

    def show_courses(self, courses):

        self.ids.courses_box.clear_widgets()

        for course in courses:

            card = CourseCard(
                title=course[1], description=course[2], duration=course[3]
            )

            self.ids.courses_box.add_widget(card)

    def search_courses(self, text):

        db = Database()

        if text == "":

            courses = db.get_courses()

        else:

            courses = db.search_courses(text)

        self.show_courses(courses)
