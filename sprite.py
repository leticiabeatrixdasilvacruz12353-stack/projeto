import arcade

def create_sprite(path, WIDTH, HEIGHT):
    sprite = arcade.Sprite(path)

    sprite.scale = max(
        WIDTH / sprite.width,
        HEIGHT / sprite.height
    )

    sprite.center_x = WIDTH / 2
    sprite.center_y = HEIGHT / 2

    return sprite