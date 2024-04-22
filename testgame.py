import pygame as py
import sys

py.init()
screen = py.display.set_mode((640,480))
py.display.set_caption("tester")

clock = py.time.Clock()
screen.fill((0,0,0))

class Player():
    def __init__(self):
        py.draw.circle(screen,(255,255,255),screen.get_height() / 2)


while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
    
    
    py.display.update()
    clock.tick(60)