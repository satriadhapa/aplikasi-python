from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class ConverterApp(MDApp):
    def flip(self):
        # a function for the the "flip" icom
        # changes the state of the app
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = "enter a decimal number"
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "enter a binary number"
        self.converted.text = ""
        self.label.text = ""

    def convert(self, args):
        # a function to fint the decimal / binary equivallent
        if self.state == 0:
            # binary to decimal
            val = str(int(self.input.text, 2))
            self.label.text = "in Decimal is : "
        else:
            # decimal to Binary
            val = bin(int(self.input.text,2))
            self.label.text = "in binary is : "
        self.converted.text = val
    def build(self):
        screen = MDScreen

        self.toolbar = MDToolbar(title = "Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        screen.toolbal.right_action_items = [
            ["rotate-3d-variant", lambda x : self.flip()]]
        screen.add_widget(self.toolbar)

        #logo
        screen.add_widget(Image(
            source = "logos.png",
            pos_hint = {"center_x": 0.5, "center_y" : 0.7},
            font_size = 22
        ))
        # collect user input
        self.input = MDTextField(
            text = "enter a binary number",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x" : 0.5, "center_y": 0.5},
            font_size = 22
        )
        screen.add_widget(self.input)
        
        #secondary + primary labels
        self.label = MDLabel(
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )
        self.converted = MDLabel(
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y" : 0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        
        # convert button
        
        screen.add_widget(MDFillRoundFlatButton(
            text = "Convert",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y" : 0.15},
            on_press = self.convert
        ))
        return screen

if __name__ == '__main__':
    ConverterApp().run()