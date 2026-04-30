import arcade
import arcade.gui

class Diary(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

    def on_show_view(self):
        box = arcade.gui.UIBoxLayout()
        diary_button = arcade.gui.UIFlatButton(text = 'diary', width = 100)
        box.add(diary_button)

        adicionar_diary = arcade.gui.UIAnchorLayout()
        adicionar_diary.add(
            box,
            anchor_x="center",
            anchor_y="center"
        )
        self.manager.add(adicionar_diary)

    def on_draw(self):
        self.manager.draw()