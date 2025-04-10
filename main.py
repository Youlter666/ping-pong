from pygame import *

width = 700
height = 500
display.set_caption("клутая иглушка")
window = display.set_mode((width,height))
window.fill((234, 200, 177))







game = True
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()