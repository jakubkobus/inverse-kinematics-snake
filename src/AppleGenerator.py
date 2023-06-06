from random import randint

import pygame as pg
from pygame.math import Vector2

class AppleGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.radius = 5
        self.pos = None
        
    def new(self):
        self.pos = Vector2(randint(self.radius, self.width - self.radius), randint(self.radius, self.height - self.radius))
        
    def draw(self, win):
        pg.draw.circle(win, (255, 20, 20), self.pos, self.radius)