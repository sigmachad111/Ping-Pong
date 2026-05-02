from pygame import *
font.init()
font = font.Font(None,50)
count1 = 0
count2 = 0
font1 = font.render("Player 1 loses",True,(255, 0, 0))
font2 = font.render("Player 2 loses",True,(255,0,0))
window = display.set_mode((700,500))
display.set_caption("Пинг-Понг")
BLUE = (0, 0, 255)
game = True
finish = False
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
first_racket = Player('ракетка.png',30.0,250.0,1.0,20,70)
second_racket = Player('ракетка.png',670.0,250.0,1.0,20,70)
ball = GameSprite('мяч.jpg',350.0,250.0,3,50,50)
speed_x = 1
speed_y = 1
while game:
    window.fill(BLUE)
    events = event.get()
    for i in events:
        if i.type == QUIT:
            game = False
    if finish != True:
        font11 = font.render("Счёт:"+str(count1),True,(255,255,255))
        font22 = font.render("Счёт:"+str(count2),True,(255,255,255))
        first_racket.reset()
        first_racket.movement1()  
        second_racket.reset()
        second_racket.movement2()
        ball.reset()
        ball.rect.y += speed_y
        ball.rect.x += speed_x
        if ball.rect.y > 450.0:
            speed_y*=-1
        if ball.rect.y < 50.0:
            speed_y*=-1
        if sprite.collide_rect(first_racket,ball):
            speed_x*=-1
            count1+=1
        if sprite.collide_rect(second_racket,ball):
            count2+=1
            speed_x*=-1
        if ball.rect.x >= 650.0:
            window.blit(font2,(250,250))
            finish = True
        if ball.rect.x <= 0.0:
            window.blit(font1,(250,250))
            finish = True
        window.blit(font11,(20,30))
        window.blit(font22,(580,30))
        display.update()
