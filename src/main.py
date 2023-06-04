from Segment import Segment

import pygame as pg
pg.init()

WIDTH, HEIGHT = SIZE = 600, 600

win = pg.display.set_mode(SIZE)

head = Segment(300, 300, 0)

def events() -> bool:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            return False
    
    return True

def update(dt: float) -> None:
    head.update(dt)
    head.follow(*pg.mouse.get_pos())

def draw() -> None:
    win.fill((30, 30, 30))
    head.draw(win)
    pg.display.update()

while events():
    dt = pg.time.Clock().tick(60) * .001
    
    update(dt)
    draw()