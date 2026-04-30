import arcade
import arcade.gui

class options(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

    def on_show_view(self):
        box = arcade.gui.UIBoxLayout()
        options_button = arcade.gui.UIFlatButton(text = 'options', width = 200)
        box.add(options_button)

        adicionar_options = arcade.gui.UIAnchorLayout()
        adicionar_options.add(
            box,
            anchor_x="center",
            anchor_y="center"
        )
        self.manager.add(adicionar_options)  

    def on_draw(self):
        self.manager.draw()