from pygame import *


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

speed = 50

clock = time.Clock()
FPS = 60

x1 = 100
y1 = 400

x2 = 500
y2 = 100

win_width = 700
win_height = 500

finish = False

font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN',True,(255,215,0))
lose = font.render('LOSE',True,(255,215,0))

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,w,h):
        super().__init__()
        self.image = transform.scale (image.load(player_image), (w, h))
        self.speed = player_speed

        self.rect = self.image.get_rect ()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed    

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_2, color_3, color_4, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_2 = color_2
        self.color_3 = color_3
        self.color_4 = color_4
        self.width = wall_width
        self.height= wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_2,color_3,color_4))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

player = Player('sprite1.png', 5, 250,4,35,35)
monster = Enemy('sprite2.png', win_width - 80,280,2,65,65)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0,100,100)

w1 = Wall(184,158,31,100,400,65,5)
w2 = Wall(184,158,31,90,400,5,50)
w3 = Wall(184,158,31,90,450,350,5)
w4 = Wall(184,158,31,90,335,150,5)
w5 = Wall(184,158,31,240,335,5,65)
w6 = Wall(184,158,31,90,90,5,250)
w7 = Wall(184,158,31,90,90,350,5)
w8 = Wall(184,158,31,440,90,5,70)
w9 = Wall(184,158,31,375,160,75,5)
w10 = Wall(184,158,31,375,160,5,150)
w11 = Wall(184,158,31,440,240,5,220)
w12 = Wall(184,158,31,300,180,5,200)
w13 = Wall(184,158,31,300,380,150,5)
w14 = Wall(184,158,31,150,280,150,5)
w15 = Wall(184,158,31,150,180,5,100)
w16 = Wall(184,158,31,210,180,90,5)
w17 = Wall(184,158,31,0,100,90,5)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish !=True:
        window.blit(background,(0,0))
        if sprite.collide_rect(player,final):
            window.blit(win, (200,200))
            finish = True
            money.play()
        if sprite.collide_rect(player,w1) or  sprite.collide_rect(player,w2) or  sprite.collide_rect(player,w3) or  sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7) or sprite.collide_rect(player,w8) or sprite.collide_rect(player,w9) or sprite.collide_rect(player,w10) or sprite.collide_rect(player,w11) or sprite.collide_rect(player,w12) or sprite.collide_rect(player,w13) or sprite.collide_rect(player,w14) or sprite.collide_rect(player,w15) or sprite.collide_rect(player,w16) or sprite.collide_rect(player,w17) : 
            window.blit(lose, (200,200))
            finish = True
            kick.play()

        player.reset()
        player.update()
        monster.reset()
        monster.update()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()
       


    display.update()
    clock.tick(FPS)


    