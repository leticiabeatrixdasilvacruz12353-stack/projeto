import arcade
import arcade.gui

class inventory(arcade.View):
    def __init__(self):
        super(). __init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

    def on_show_View(self):
        box = arcade.gui.UIBoxLayout()
        inventory_button = arcade.gui.UIFlatButton(text = 'inventory', width = 200)
        box.add(inventory_button)

        adicionar_inventory = arcade.gui.UIAnchorLayout()
        adicionar_inventory.add(
            box,
            anchor_x = 'center',
            anchor_y = 'center'
        )

        self.manager.add(adicionar_inventory)

    def on_draw(self):
        self.manager.draw()
