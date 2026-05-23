from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

KV = '''
<HomeScreen>

    name: "home"
    
    MDBoxLayout:
       orientation: "vertical"
       
       MDTopAppBAr:
           title: "Cursos Tequixquiac"
           elevation: 4
           
        ScrollView:
            
            MDBoxLayout:
               orientation: "vertical"
               adaptive_height: True
               spacing: "20dp"
               padding: "20dp"
               
               # =====================
               # BANNER PRINCIPAL
               # =====================
               MDCard:
                   orientation: "vertical"
                   size_hint_y: None
                   height: "220dp"
                   radius: [25]
                   elevation: 6
                   padding: "20dp"
                   
                   FitImage:
                       source: "assets/images/banner.jpg"
                       radius: [25,25,0,0]
                       
                    MDBoxLayout:
                       orientation: "vertical"
                       padding: "10dp"
                       
                       MDLabel:
                       text: "Bienvenido"
                       font_style: "H5"
                       bold: True
                       
                       MDLabel:
                       text: "Administra todos los cursos del centro de Tequixquiac."
                       theme_text_color: "Secondary"
                       
                # =====================
                # ESTADISTICAS
                # =====================
                
                MDGridLayout:
                    cols: 2
                    adaptive_height: True
                    spacing: "15dp"
                    
                    MDCard:
                        orientation: "vertical"
                        padding: "15dp"
                        radius: [20]
                        elevation: 3
                        size_hint_y: None
                        height: "120dp"
                        
                        MDLabel:
                            text: "24"
                            halign: "center"
                            font_style: "H3"
                            theme_text_color: "Custom"
                            text_color: 0, 0.6, 1, 1
                            
                        MDLabel:
                            text: "Cursos"
                            halign: "center"
                            
                    MDCard:
                        orientation: "vertical"
                        padding: "15dp"
                        radius: [20]
                        elevation: 3
                        size_hint_y: None
                        height: "120dp"
                        
                        MDLabel:
                            text: "120"
                            halign: "center"
                            font_style: "H3"
                            theme_text_color: "Custom"
                            text_color: 0, 0.8, 0.4, 1
                            
                        MDLabel:
                            text: "Alumnos"
                            halign: "center"
                            
                # ======================
                # CARD CURSOS
                # ======================

                MDCard:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"
                    radius: [20]
                    elevation: 3
                    size_hint_y: None
                    height: "180dp"

                    MDLabel:
                        text: "Explorar Cursos"
                        font_style: "H5"
                        bold: True

                    MDLabel:
                        text: "Consulta todos los cursos disponibles."
                        theme_text_color: "Secondary"

                    MDRaisedButton:
                        text: "Ver Cursos"
                        pos_hint: {"center_x": .5}
                        on_release:
                            app.change_screen("courses")

                # ======================
                # CARD ADMIN
                # ======================

                MDCard:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"
                    radius: [20]
                    elevation: 3
                    size_hint_y: None
                    height: "180dp"

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
                            app.change_screen("login")

'''

Builder.load_string(KV)


class HomeScreen(MDScreen):
    pass