from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = """
<AdminScreen>

    name: "admin"

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Administrador"

            left_action_items:
                [["arrow-left", lambda x: app.change_screen("home")]]

        MDLabel:
            text: "Panel administrador"
            halign: "center"
"""

Builder.load_string(KV)


class AdminScreen(MDScreen):
    pass
