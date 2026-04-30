import arcade
import arcade.gui

class combat(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

    def on_show_view(self):
    
        box = arcade.gui.UIBoxLayout()
        combat_button = arcade.gui.UIFlatButton(text = 'combat', width = 200)
        box.add(combat_button)

        adicionar_combat = arcade.gui.UIAnchorLayout()
        adicionar_combat.add(
            box,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        self.manager.add(adicionar_combat)

    def on_draw(self):
        self.manager.draw()
