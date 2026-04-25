from pygame import *
window = display.set_mode((700,500))
display.set_caption("Пинг-Понг")
BLUE = (0, 0, 255)
game = True
while game:
    events = event.get()
    for i in events:
        if i.type == QUIT:
            game = False
    window.fill(BLUE)    
    display.update()
