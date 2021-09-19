from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CheckSeparatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, world!", halign="center")


CheckSeparatorApp().run()
