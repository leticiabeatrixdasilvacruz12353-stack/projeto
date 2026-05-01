import arcade

def setSound(src):
    musica = arcade.load_sound(src)
    player = arcade.play_sound(musica, looping=True)