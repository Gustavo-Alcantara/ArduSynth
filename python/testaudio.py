import pygame as pg
from pygame import mixer

pg.init()
pg.mixer.set_num_channels(50)
timer = pg.time.Clock()
fps = 60
screen = pg.display.set_mode([800,640])
pg.display.set_caption("Synthesizer")

keys = ['a','s','d','f','g','h','j','k']
files_piano = ["C4","D4","E4","F4","G4","A4","B4","C5"]
files_drum = ["kick1","cl_hihat","snare","tom1","handclap","hightom","claves","open_hh"]
notes_piano = []
notes_drum = []
pressed = []

for f in files_piano:
    notes_piano.append(mixer.Sound(f'python/assets/piano/{f}.wav'))
for f in files_drum:
    notes_drum.append(mixer.Sound(f'python/assets/drum/{f}.wav'))

notes = notes_drum
while True:
    timer.tick(fps)
    screen.fill('black')
    for event in pg.event.get():

        if event.type == pg.QUIT:
            break
        elif event.type == pg.TEXTINPUT:
            for i,k in enumerate(keys):
                if k in event.text and k not in pressed:
                    pressed.append(k)
                    notes[i].play(0,1000)
        elif event.type == pg.KEYUP:
            for i,k in enumerate(keys):
                if k == event.unicode:
                    pressed.remove(k)
                


    pg.display.flip()

pg.quit()