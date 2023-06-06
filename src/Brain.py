from math import cos, sin, pi

import pygame as pg
from pygame.math import Vector2

class Brain:
    def __init__(self, x, y, angle, velocity):
        self.pos = Vector2(x, y)
        self.angle = angle
        self.direction = Vector2(cos(self.angle), sin(self.angle))
        self.velocity = velocity
        
    def update(self, dt):
        self.direction = Vector2(cos(self.angle), sin(self.angle))
        self.pos += self.direction * self.velocity * dt
        
    def turn(self, direction_):
        self.angle += direction_ * pi / 60