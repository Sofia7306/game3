from pygame import *


class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
      super().__init__()
      self.image = transform.scale(image.load(player_image),(w,h))
      self.speed=speed  
      self.rect =self.image.get_rect()
      self.rect.x = x 
      self.rect.y = y

    def reset (self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_a]and self.rect.x >0 :
            self.rect.x -= self.speed
        if  keys[K_w]and self.rect.y >0 :
            self.rect.y -= self.speed
        if keys[K_d]and self.rect.x <700 :
            self.rect.x += self.speed
        if  keys[K_s]and self.rect.y <500 :
            self.rect.y += self.speed

    direction = "right"
    def move2(self):
        if self.rect.x > 500:
            self.direction ="left"
        if self.rect.x < 100:
            self.direction ="right"  

        if self.direction == "right" :
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed 

    direction = "down"
    def move3(self):
        if self.rect.y > 500:
            self.direction ="down"
        if self.rect.y < 100:
            self.direction ="up"  

        if self.direction == "up" :
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed           


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window =display.set_mode((800,600))
picture =transform.scale(image.load("images.jpg"),(800,600))

#створення персонажів
hamster1 =Object('hamter1.png',500,400,100,80,10)
hamster2 =Object('hamster2.png',200,200,100,80,10)
hamster3 =Object("hamster2.png",500,100,100,80,10)

#створення стін
wall1 = Wall (208,0,97,300,100,200,10)
wall2 = Wall (37,229,153,100,200,10,200)
wall3 = Wall (208,0,97,500,300,200,10)
wall4 = Wall (37,229,153,10,100,200,10)
wall5 = Wall (208,0,97,300,600,200,10)


clock = time.Clock()

x1,y1 = 100,100
x2,y2 = 100,200
game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False





    window.blit(picture,(0,0))
    hamster1.reset()
    hamster2.reset()
    hamster3.reset()
    hamster1.move()
    hamster2.move2()
    hamster3.move3()

    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
   

    if sprite.collide_rect(hamster1,hamster2):
        game = False

   
   
   
   
   
   
    display.update()
    clock.tick(60)
