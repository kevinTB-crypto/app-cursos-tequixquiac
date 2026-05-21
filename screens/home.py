from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = """
<HomeScreen>

    name: "home"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Cursos pip Tequixquiac"

        MDLabel:
            text: "Bienvenido"
            halign: "center"
            font_style: "H4"

        MDRaisedButton:
            text: "Ver Cursos"
            pos_hint: {"center_x": .5}
            on_release:
                app.root.current = "courses"

        MDRaisedButton:
            text: "Registro"
            pos_hint: {"center_x": .5}
            on_release:
                app.root.current = "register"
"""

Builder.load_string(KV)


class HomeScreen(MDScreen):
    pass
