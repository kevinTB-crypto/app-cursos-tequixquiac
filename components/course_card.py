from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.fitimage import FitImage


class CourseCard(MDCard):

    def __init__(
        self,
        title,
        description,
        duration,
        button_text="Ver más",
        button_callback=None,
        **kwargs,
    ):

        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = "12dp"
        self.spacing = "10dp"
        self.size_hint_y = None
        self.height = "320dp"
        self.radius = [20]
        self.elevation = 3

        image = FitImage(
            source="assets/images/banner.jpg",
            size_hint_y=None,
            height="140dp",
            radius=[15],
        )

        title_label = MDLabel(
            text=title, bold=True, font_style="H6", adaptive_height=True
        )

        desc_label = MDLabel(
            text=description, theme_text_color="Secondary", adaptive_height=True
        )

        duration_label = MDLabel(text=f"Duración: {duration}", adaptive_height=True)

        button = MDRaisedButton(text=button_text, pos_hint={"center_x": 0.5})

        if button_callback:
            button.bind(on_release=button_callback)

        self.add_widget(image)
        self.add_widget(title_label)
        self.add_widget(desc_label)
        self.add_widget(duration_label)
        self.add_widget(button)
