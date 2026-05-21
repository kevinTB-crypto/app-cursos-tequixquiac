from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from database.db import Database
from components.course_card import CourseCard

KV = """

<AdminScreen>

    name: "admin"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Administrador"

            left_action_items:
                [["arrow-left", lambda x: app.change_screen("home")]]

        ScrollView:

            MDBoxLayout:
                id: admin_box
                orientation: "vertical"
                adaptive_height: True
                spacing: "20dp"
                padding: "20dp"

"""

Builder.load_string(KV)


class AdminScreen(MDScreen):

    def on_enter(self):

        self.load_admin_panel()

    def load_admin_panel(self):

        self.ids.admin_box.clear_widgets()

        db = Database()

        courses = db.get_courses()

        for course in courses:

            card = CourseCard(
                title=course[1],
                description=course[2],
                duration=course[3],
                button_text="Editar",
                button_callback=lambda x, course=course: self.edit_course(course),
            )

            self.ids.admin_box.add_widget(card)

    def edit_course(self, course):

        edit_screen = self.manager.get_screen("edit_course")

        edit_screen.load_course(course[0], course[1], course[2], course[3])

        self.manager.current = "edit_course"

    def delete_course(self, course_id):

        db = Database()

        db.delete_course(course_id)

        self.load_admin_panel()
