from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from database.db import Database

KV = """

<EditCourseScreen>

    name: "edit_course"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Editar Curso"

            left_action_items:
                [["arrow-left",
                lambda x: app.change_screen("admin")]]

        ScrollView:

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "20dp"
                padding: "20dp"

                MDTextField:
                    id: title_field
                    hint_text: "Título"

                MDTextField:
                    id: description_field
                    hint_text: "Descripción"

                MDTextField:
                    id: duration_field
                    hint_text: "Duración"

                MDRaisedButton:
                    text: "Actualizar curso"
                    pos_hint: {"center_x": .5}
                    on_release:
                        root.update_course()

                MDLabel:
                    id: message_label
                    text: ""
                    halign: "center"

"""

Builder.load_string(KV)


class EditCourseScreen(MDScreen):

    course_id = None

    def load_course(self, course_id, title, description, duration):

        self.course_id = course_id

        self.ids.title_field.text = title
        self.ids.description_field.text = description
        self.ids.duration_field.text = duration

    def update_course(self):

        db = Database()

        db.update_course(
            self.course_id,
            self.ids.title_field.text,
            self.ids.description_field.text,
            self.ids.duration_field.text,
        )

        self.ids.message_label.text = "Curso actualizado"
