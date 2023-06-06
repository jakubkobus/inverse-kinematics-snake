from Segment import Segment
from Brain import Brain
from AppleGenerator import AppleGenerator

from math import sin, cos

import pygame as pg
pg.init()

WIDTH, HEIGHT = SIZE = 600, 600

win = pg.display.set_mode(SIZE)
pg.display.set_caption("Inverse kinematics snake")

brain: Brain = Brain(300, 300, 0, 100)
head: Segment = Segment(0, 0, 0)
tail: [Segment, ...] = [head]

apple: AppleGenerator = AppleGenerator(WIDTH, HEIGHT)
apple.new()

direction: int = 0 # left = -1 ; right = 1

def events() -> bool:
    global direction
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            return False

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_LEFT:
                direction = -1
            if e.key == pg.K_RIGHT:
                direction = 1
                
        if e.type == pg.KEYUP:
            if e.key == pg.K_LEFT:
                direction = 0
            if e.key == pg.K_RIGHT:
                direction = 0
        
    return True

def update(dt: float) -> None:
    global apple, tail
    
    appleDelta = brain.pos - apple.pos
    
    if abs(appleDelta.x) <= apple.radius and abs(appleDelta.y) <= apple.radius:
        last = tail[-1]
        tail.append(Segment(last.end.x, last.end.y, last.angle))
        apple.new()
    
    brain.update(dt)
    
    head.update(dt)
    head.follow(brain.pos.x, brain.pos.y)
    
    for idx, seg in enumerate(tail):
        if idx == 0: continue
        seg.update(dt)
        last = tail[idx - 1].end
        seg.follow(last.x, last.y)
        
    if direction != 0:
        brain.turn(direction)
    
def draw() -> None:
    win.fill((30, 30, 30))
    
    for t in tail:
        t.draw(win)
        
    apple.draw(win)
    
    pg.display.update()

while events():
    dt = pg.time.Clock().tick(60) * .001
    
    update(dt)
    draw()
