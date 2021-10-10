# imports
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise

# creating the window
app = Ursina()

window.borderless = True
window.color = color.rgb(0, 200, 211)
window.exit_button.visible = False

scene.fog_color = color.rgb(255, 0, 0)
scene.fog_density = 0.04

grass_stroke_texture = 'grass_texture.png'


# key inputs
def input(key):
    if key == 'q':
        quit()


# runs every frame
def update():
    pass


terrain = Entity(model='None', collider='None')
noise = PerlinNoise(octaves=2, seed=2021)
amp = 6
freq = 24

terrain_width = 32
for i in range(terrain_width * terrain_width):
    ent_cube = Entity(model='cube', color=color.green)
    ent_cube.x = floor(i / terrain_width)
    ent_cube.z = floor(i % terrain_width)
    ent_cube.y = floor((noise([ent_cube.x / freq, ent_cube.z / freq])) * amp)
    ent_cube.parent = terrain

terrain.combine()
terrian

# create first person player
player = FirstPersonController()
player.cursor.visible = False
player.gravity = 0.5
player.x = player.z = 5
player.y = 12

# create a sky
Sky()

# start the game
app.run()
