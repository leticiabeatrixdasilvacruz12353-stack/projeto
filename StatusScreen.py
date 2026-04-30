import arcade
import arcade.gui

class status(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()   
        self.manager.enable()

    def on_show_view(self):

        box = arcade.gui.UIBoxLayout()
        status_button = arcade.gui.UIFlatButton(text = 'status', width = 100)
        box.add(status_button)

        adicionar_status = arcade.gui.UIAnchorLayout()
        adicionar_status.add(
            box,
            anchor_x="center",
            anchor_y="center"
        )
        self.manager.add(adicionar_status)

    def on_draw(self):
        self.manager.draw()