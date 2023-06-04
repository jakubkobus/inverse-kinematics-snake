import pygame as pg
from math import sin, cos, atan2

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def get(self):
        return (self.x, self.y)
    
    def set(self, x ,y):
        self.x = x
        self.y = y
        
    def multiply(self, f1, f2 = 1):
        self.x *= f1
        self.y *= f2 if f2 != 1 else f1

class Segment:
    def __init__(self, x, y, angle):
        self.angle = angle
        self.length = 40
        self.start = Vector(x, y)
        self.end = None
        
    def calculateEnd(self) -> (float, float):
        dx = cos(self.angle) * self.length
        dy = sin(self.angle) * self.length
        self.end = Vector(self.start.x + dx, self.start.y + dy)
    
    def follow(self, tx, ty) -> None:
        ox, oy = tx - self.start.x, ty - self.start.y
        direction = Vector(ox, oy)
        self.angle = atan2(direction.x, direction.y)
        
        
        self.start.set(tx, ty)
    
    def update(self, dt) -> None:
        self.calculateEnd()
    
    def draw(self, win) -> None:
        pg.draw.line(win, (255, 255, 255), self.start.get(), self.end.get())