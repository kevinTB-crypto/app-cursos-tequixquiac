from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = """
<RegisterScreen>

    name: "register"

    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "20dp"

        MDTopAppBar:
            title: "Registro"

            left_action_items:
                [["arrow-left", lambda x: app.change_screen("home")]]

        MDTextField:
            hint_text: "Nombre"

        MDTextField:
            hint_text: "Apellido"

        MDTextField:
            hint_text: "Teléfono"

        MDRaisedButton:
            text: "Registrarse"
            pos_hint: {"center_x": .5}
"""

Builder.load_string(KV)


class RegisterScreen(MDScreen):
    pass
