from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
MDScreen:
    MDTopAppBar:
        title: "Cursos Tequixquiac"
        pos_hint: {"top": 1}

    MDRaisedButton:
        text: "Ver Cursos"
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class CursosApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


CursosApp().run()
