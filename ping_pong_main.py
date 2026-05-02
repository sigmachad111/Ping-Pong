from pygame import *
window = display.set_mode((700,500))
display.set_caption("Пинг-Понг")
BLUE = (0, 0, 255)
game = True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,sprite_width,sprite_height):
        super().__init__()
        self.width = sprite_width
        self.height = sprite_height
        self.image = transform.scale(image.load(player_image),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,sprite_width,sprite_height):
        super().__init__(player_image,player_x,player_y,player_speed,sprite_width,sprite_height)
    def movement1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
    def movement2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
first_racket = Player('ракетка.png',30,250,1,20,70)
second_racket = Player('ракетка.png',670,250,1,20,70)
ball = GameSprite('мяч.jpg',350,250,3,50,50)
while game:
    window.fill(BLUE)
    events = event.get()
    for i in events:
        if i.type == QUIT:
            game = False
    first_racket.reset()
    first_racket.movement1()  
    second_racket.reset()
    second_racket.movement2()
    ball.reset()
    display.update()
