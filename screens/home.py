from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = """

<HomeScreen>

    name: "home"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Cursos Tequixquiac"
            elevation: 4

        ScrollView:

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "20dp"
                padding: "20dp"

                FitImage:
                    source: "assets/images/banner.jpg"
                    size_hint_y: None
                    height: "220dp"
                    radius: [20]

                MDLabel:
                    text: "Bienvenido"
                    halign: "center"
                    font_style: "H3"
                    bold: True

                MDLabel:
                    text: "Administra y consulta todos los cursos disponibles del centro de Tequixquiac."
                    halign: "center"
                    theme_text_color: "Secondary"

                MDCard:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"
                    size_hint_y: None
                    height: "180dp"
                    radius: [20]
                    elevation: 3

                    MDLabel:
                        text: "Cursos Disponibles"
                        font_style: "H5"
                        bold: True

                    MDLabel:
                        text: "Consulta talleres y capacitaciones disponibles."
                        theme_text_color: "Secondary"

                    MDRaisedButton:
                        text: "Ver Cursos"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("courses")

                MDCard:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"
                    size_hint_y: None
                    height: "180dp"
                    radius: [20]
                    elevation: 3

                    MDLabel:
                        text: "Registro"
                        font_style: "H5"
                        bold: True

                    MDLabel:
                        text: "Regístrate para participar en cursos."
                        theme_text_color: "Secondary"

                    MDRaisedButton:
                        text: "Ir a Registro"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("register")

                MDCard:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"
                    size_hint_y: None
                    height: "180dp"
                    radius: [20]
                    elevation: 3

                    MDLabel:
                        text: "Administrador"
                        font_style: "H5"
                        bold: True

                    MDLabel:
                        text: "Gestiona cursos y contenido."
                        theme_text_color: "Secondary"

                    MDRaisedButton:
                        text: "Panel Admin"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("admin")
"""

Builder.load_string(KV)


class HomeScreen(MDScreen):
    pass
