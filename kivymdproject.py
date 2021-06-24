import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root
from kivymd.uix.dialog import MDDialog

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class KivyMDproject(MDApp):  # NOQA: N801

    data = {
        "Chi siamo": "account-group",
        "Assistenza": "face-agent",
        "FAQ": "frequently-asked-questions"
    }

    def __init__(self, **kwargs):
        super(KivyMDproject, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "First App"

        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.primary_hue = "200"

        self.theme_cls.accent_palette = "Red"
        self.theme_cls.accent_hue = "400"

        self.theme_cls.theme_style = "Dark"

    def build(self):
        return Root()

