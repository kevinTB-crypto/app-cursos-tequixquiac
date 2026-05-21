from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

KV = """
MDScreen:

    md_bg_color: 1, 1, 1, 1

    MDTopAppBar:
        title: "Cursos Tequixquiac"
        pos_hint: {"top": 1}

    MDLabel:
        text: "Bienvenido"
        halign: "center"
        font_style: "H4"
        pos_hint: {"center_y": .6}

    MDRaisedButton:
        text: "Ver Cursos"
        pos_hint: {"center_x": .5, "center_y": .4}
"""


class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        return Builder.load_string(KV)


MainApp().run()
