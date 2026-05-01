import arcade
import random

# 🔥 cria uma partícula
def create_particle(image, direction="random"):
    particle = arcade.Sprite("particulas/" + image)

    particle.center_x = random.randint(0, 800)
    particle.center_y = random.randint(0, 600)

    speed = random.uniform(1, 3)

    # 🎯 DIREÇÕES
    if direction == "up":
        particle.change_x = random.uniform(-1, 1)
        particle.change_y = speed

    elif direction == "left":
        particle.change_x = -speed
        particle.change_y = random.uniform(-1, 1)

    elif direction == "right":
        particle.change_x = speed
        particle.change_y = random.uniform(-1, 1)

    elif direction == "down":
        particle.change_x = random.uniform(-1, 1)
        particle.change_y = -speed

    elif direction == "diag_up_left":
        particle.change_x = -speed
        particle.change_y = speed

    elif direction == "diag_up_right":
        particle.change_x = speed
        particle.change_y = speed

    elif direction == "diag_down_left":
        particle.change_x = -speed
        particle.change_y = -speed

    elif direction == "diag_down_right":
        particle.change_x = speed
        particle.change_y = -speed

    else:  # random
        particle.change_x = random.uniform(-2, 2)
        particle.change_y = random.uniform(-2, 2)

    particle.lifetime = random.randint(80, 90)
    particle.scale = 0.5

    particle.alpha = 0
    particle.fade_in = True

    return particle

# 🔥 cria lista inicial (poucas partículas)
def particles_list(p1, p2, p3, direction="random"):
    particles = arcade.SpriteList()
    imagens = [p1, p2, p3]

    for _ in range(1):
        img = random.choice(imagens)
        particle = create_particle(img, direction)
        particles.append(particle)

    return particles

# 🔥 atualiza tudo
def move_particles(particles, delta_time):
    for particle in particles:

        # 🛑 proteção absoluta contra bug de scale
        if isinstance(particle.scale, tuple):
            particle.scale = particle.scale[0]

        # movimento
        particle.center_x += particle.change_x
        particle.center_y += particle.change_y
        particle.change_y -= 0.05  # gravidade

        # FADE IN
        if particle.fade_in:
            particle.alpha += 8
            if particle.alpha >= 255:
                particle.alpha = 255
                particle.fade_in = False

        # VIDA + FADE OUT
        else:
            particle.lifetime -= 1

            if particle.lifetime < 30:
                particle.alpha -= 8

                # só diminui se for número
                if isinstance(particle.scale, (int, float)):
                    particle.scale -= 0.01

        # remover suavemente
        if particle.alpha <= 0 or (
            isinstance(particle.scale, (int, float)) and particle.scale <= 0
        ):
            particle.kill()

    # 🔥 SPAWN CONTÍNUO (não nasce tudo junto)
    if random.random() < 0.05:
        new_particle = create_particle(random.choice([
            "a1.png",
            "a2.png",
            "a3.png",
        ])  , direction="diag_down_right")
        particles.append(new_particle)