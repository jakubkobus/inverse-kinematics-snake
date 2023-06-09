from math import cos, sin, atan2 #, sqrt

import pygame as pg
from pygame.math import Vector2

class Segment:
    def __init__(self, x, y, angle):
        self.angle = angle
        self.length = 10
        self.start = None
        self.end = Vector2(x, y)

    def calculateStart(self) -> (float, float):
        dx = cos(self.angle) * self.length
        dy = sin(self.angle) * self.length
        self.start = Vector2(self.end.x + dx, self.end.y + dy)
    
    def follow(self, tx, ty) -> None:
        target = Vector2(tx, ty)
        direction = target - self.end
        self.angle = atan2(direction.y, direction.x)
        
        # divider = sqrt(direction.x ** 2 + direction.y ** 2)
        # divider = divider if divider != 0 else .001
        # lengthFactor = self.length / divider
        # direction *= -lengthFactor
        
        direction.clamp_magnitude_ip(self.length, self.length)
        
        self.end = target + direction * -1
        
    def update(self, dt) -> None:
        self.calculateStart()
    
    def draw(self, win) -> None:
        pg.draw.line(win, (255, 255, 255), self.start, self.end)