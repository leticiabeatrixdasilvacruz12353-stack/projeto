import arcade
import arcade.gui
from window import largura, altura, titulo
from sprite import create_sprite
from audio.sound import setSound
from motor_particulas import particles_list, move_particles

class Menu(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

    def on_show_view(self):
        self.sprites = arcade.SpriteList()
        self.background = create_sprite("imagens/menu2.png", 900, 600)
        self.sprites.append(self.background)

        self.particles = particles_list(
            "a1.png",
            "a2.png",
            "a3.png",
        )

         # música
        self.musica = arcade.load_sound("audio/mu.mp3")
        self.player = arcade.play_sound(self.musica, volume=0.1)

        box = arcade.gui.UIBoxLayout()
        start_button = arcade.gui.UIFlatButton(text='Start', width=200)
        box.add(start_button)

        adicionar_butoes = arcade.gui.UIAnchorLayout() #layout para adicionar os botões
        adicionar_butoes.add(box, anchor_x = "center_x", anchor_y = "center_y") #alinha os botões no centro da tela
        self.manager.add(adicionar_butoes) #adiciona o layout ao gerenciador

    def on_mouse_press(self, x, y, button, modifiers):
        if 850 < x < 880 and 565 < y < 595:
            arcade.close_window()

    def on_update(self, delta_time):
        if not self.player.playing:
            self.player = arcade.play_sound(self.musica, volume=0.5)
        move_particles(self.particles, delta_time)

    def on_draw(self):
        self.clear()
        self.sprites.draw()
        self.particles.draw()

        # barra superior
        arcade.draw_lbwh_rectangle_filled(0, 560, 900, 40, arcade.color.DARK_BLUE)

        # botão fechar
        arcade.draw_lbwh_rectangle_filled(850, 565, 30, 30, arcade.color.DARK_CANDY_APPLE_RED)

        arcade.draw_text(titulo, 20, 572, arcade.color.WHITE, 14)
        arcade.draw_text("X", 858, 570, arcade.color.WHITE, 18)

        self.manager.draw()
