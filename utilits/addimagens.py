import arcade

def add_imagens(src_imagens):
    # Carregar as imagens
    imagem_fundo = arcade.load_texture("src_imagens")
    imagem_personagem = arcade.load_texture("imagens/personagem.png")
    imagem_inimigo = arcade.load_texture("imagens/inimigo.png")
    
    return imagem_fundo, imagem_personagem, imagem_inimigo