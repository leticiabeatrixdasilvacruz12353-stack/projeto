from window import largura, altura, titulo
import arcade
import Menu

class Main(arcade.Window):
    def __init__(self, largura, altura, titulo):
        super().__init__(largura, altura, titulo)

    def menu(self):
        menu = Menu.Menu()
        self.show_view(menu)


game = Main(largura, altura, titulo) #criarndo a janela
game.menu() #criando o menu

arcade.run() #iniciar o jogo
