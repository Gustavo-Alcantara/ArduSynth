import pygame as pg
from pygame import mixer

pg.init()

pg.mixer.set_num_channels(50)
timer = pg.time.Clock()
fps = 60
screen = pg.display.set_mode([800,640])
pg.display.set_caption("Synthesizer")

while True:
    timer.tick(fps)
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            break
    pg.display.flip()

pg.quit()