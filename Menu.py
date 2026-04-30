import arcade
import arcade.gui
from window import largura, altura, titulo
class Menu(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

    def on_show_view(self):
        self.sprites = arcade.SpriteList()

        box = arcade.gui.UIBoxLayout()
        start_button = arcade.gui.UIFlatButton(text='Start', width=200)
        box.add(start_button)

        adicionar_butoes = arcade.gui.UIAnchorLayout() #layout para adicionar os botões
        adicionar_butoes.add(box, anchor_x = "cen'ter_x", anchor_y = "center_y") #alinha os botões no centro da tela
        self.manager.add(adicionar_butoes) #adiciona o layout ao gerenciador

        self.manager.add(layout)

    def on_mouse_press(self, x, y, button, modifiers):
        if 850 < x < 880 and 565 < y < 595:
            arcade.close_window()

    def on_draw(self):
        self.clear()

        # barra superior
        arcade.draw_lbwh_rectangle_filled(0, 560, 900, 40, arcade.color.DARK_BLUE)

        # botão fechar
        arcade.draw_lbwh_rectangle_filled(850, 565, 30, 30, arcade.color.DARK_CANDY_APPLE_RED)

        arcade.draw_text(titulo, 20, 572, arcade.color.WHITE, 14)
        arcade.draw_text("X", 858, 570, arcade.color.WHITE, 18)

        self.manager.draw()