import arcade
import arcade.gui

class Menu(arcade.View):
    def __init__(self): #constructor
        super().__init__()
        self.manager = arcade.gui.UIManager() #gerenciador de interface gráfica
        self.manager.enable() #habilita o gerenciador
    
    def on_show_view(self):
        arcade.set_background_color(arcade.color.PINK)

        box = arcade.gui.UIBoxLayout() 
        start_button = arcade.gui.UIFlatButton(text = 'start', width = 200)
        box.add(start_button)

        adicionar_butoes = arcade.gui.UIAnchorLayout() #layout para adicionar os botões
        adicionar_butoes.add(box, anchor_x = "cen'ter_x", anchor_y = "center_y") #alinha os botões no centro da tela
        self.manager.add(adicionar_butoes) #adiciona o layout ao gerenciador


    def on_draw(self):
        self.clear()
        self.manager.draw() 
        