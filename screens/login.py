from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = """

<LoginScreen>

    name: "login"

    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "30dp"

        MDTopAppBar:
            title: "Login Administrador"

            left_action_items:
                [["arrow-left",
                lambda x: app.change_screen("home")]]

        Widget:

        MDLabel:
            text: "Acceso Administrador"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: username_field
            hint_text: "Usuario"

        MDTextField:
            id: password_field
            hint_text: "Contraseña"
            password: True

        MDRaisedButton:
            text: "Iniciar sesión"
            pos_hint: {"center_x": .5}
            on_release:
                root.login()

        MDLabel:
            id: message_label
            text: ""
            halign: "center"
            theme_text_color: "Error"

        Widget:

"""

Builder.load_string(KV)


class LoginScreen(MDScreen):

    def login(self):

        username = self.ids.username_field.text
        password = self.ids.password_field.text

        admin_user = "admin"
        admin_password = "1234"

        if username == admin_user and password == admin_password:

            self.ids.message_label.text = ""

            self.manager.current = "admin"

        else:

            self.ids.message_label.text = "Usuario o contraseña incorrectos"
