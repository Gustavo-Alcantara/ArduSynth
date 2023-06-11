import pygame as pg
from pygame import mixer

pg.init()
pg.mixer.set_num_channels(50)
timer = pg.time.Clock()
fps = 60
screen = pg.display.set_mode([800,640])
pg.display.set_caption("Synthesizer")

keys = ['a','s','d','f','g','h','j']
files = ["C4","D4","E4","F4","G4","A4","B4"]
notes = []

for f in files:
    notes.append(mixer.Sound(f'python/assets/{f}.wav'))


while True:
    timer.tick(fps)
    screen.fill('black')
    for event in pg.event.get():

        if event.type == pg.QUIT:
            break
        elif event.type == pg.TEXTINPUT:
            for i,k in enumerate(keys):
                if k in event.text:
                    notes[i].play(0,1000)
    pg.display.flip()

pg.quit()