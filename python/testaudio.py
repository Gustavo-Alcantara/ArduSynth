import pygame as pg
from pygame import mixer

pg.init()
pg.mixer.set_num_channels(50)
timer = pg.time.Clock()
fps = 60
screen = pg.display.set_mode([800,640])
pg.display.set_caption("Synthesizer")

files = ["C4","D4","E4","F4","G4","A4","B4"]
notes = []

for f in files:
    notes.append(mixer.Sound(f'assets/{f}.wav'))


while True:
    timer.tick(fps)
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            break
    pg.display.flip()

pg.quit()