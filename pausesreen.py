from typing import Self

import arcade
import arcade.gui
 
class pause(arcade.View):

    def __init__():
        super().__init__()

    Self.manager = arcade.gui.UIManager()
    Self.manager.enable()
    
    def on_show_view(self):
        box = arcade.gui.UIBoxLayout
        pause_button = arcade.gui.UIFlatButton
        box 