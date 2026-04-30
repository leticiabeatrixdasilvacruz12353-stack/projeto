import arcade
import arcade.gui

class status(arcade.View):
    def __init__(self):
        super().__init__()
       
        self.manager = arcade.gui.UIManager()
        self.manager.enable()   

    def on_show_view(self):

        box = arcade.gui.UIBoxLayout()
        save_button = arcade.gui.UIFlatButton(text = 'save', width = 100)
        box.add(save_button)

        adicionar_save = arcade.gui.UIAnchorLayout()
        adicionar_save.add(
            box,
            anchor_x="center",
            anchor_y="center"
        )
        self.manager.add(adicionar_save)

    def on_draw(self):
        self.manager.draw()
       