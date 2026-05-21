from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from database.db import Database

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
                orientation: "vertical"
                adaptive_height: True
                spacing: "20dp"
                padding: "20dp"

                MDLabel:
                    text: "Agregar nuevo curso"
                    halign: "center"
                    font_style: "H5"

                MDTextField:
                    id: title_field
                    hint_text: "Título del curso"

                MDTextField:
                    id: description_field
                    hint_text: "Descripción"

                MDTextField:
                    id: duration_field
                    hint_text: "Duración"

                MDRaisedButton:
                    text: "Guardar curso"
                    pos_hint: {"center_x": .5}
                    on_release:
                        root.save_course()

                MDLabel:
                    id: message_label
                    text: ""
                    halign: "center"
                    theme_text_color: "Primary"

"""

Builder.load_string(KV)


class AdminScreen(MDScreen):

    def save_course(self):

        title = self.ids.title_field.text
        description = self.ids.description_field.text
        duration = self.ids.duration_field.text

        if title == "" or description == "" or duration == "":

            self.ids.message_label.text = "Completa todos los campos"
            return

        db = Database()

        db.add_course(title, description, duration)

        self.ids.message_label.text = "Curso agregado correctamente"

        self.ids.title_field.text = ""
        self.ids.description_field.text = ""
        self.ids.duration_field.text = ""
