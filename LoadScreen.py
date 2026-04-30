import arcade
import arcade.gui

class load(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()   
        self.manager.enable()

    def on_show_view(self):

        box = arcade.gui.UIBoxLayout()
        load_button = arcade.gui.UIFlatButton(text = 'load', width = 100)
        box.add(load_button)

        adicionar_load = arcade.gui.UIAnchorLayout()
        adicionar_load.add(
            box,
            anchor_x="center",
            anchor_y="center"
        )
        self.manager.add(adicionar_load)

    def on_draw(self):
        self.manager.draw()
