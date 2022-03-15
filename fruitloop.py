import random
import pygame

def generate_random_fruits(fruit, data):
    fruit_path = "sources/images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x' : random.randint(100,500),
        'y' : 800,
        'speed_x': random.randint(-10,10),
        'speed_y': random.randint(-80, -60),
        'throw': False,
        't': 0,
        'hit': False,
    }
    if random.random() >= 0.75:
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False
    return data[fruit]