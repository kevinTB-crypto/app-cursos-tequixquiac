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

        db = Database()

        courses = db.get_courses()

        for course in courses:

            card = CourseCard(
                title=course[1], description=course[2], duration=course[3]
            )

            self.ids.courses_box.add_widget(card)
