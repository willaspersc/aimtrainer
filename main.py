import pygame #imports the pygame module which allows pygame to operate
import random #imports a random number generator if needed during the pygame
import os #imports and operating system module so python can interact with the computer such as file searching

WIDTH = 1920 #the width of the window stored in a variable
HEIGHT = 1080 #the height of the window stored in a variable
FPS = 60 #the frame count limit for the window so it loops 60 times per second

#colours
#this is so i can easily call on colour value which are stored in variables
RED = (255,0,0) #the rgb value for red
GREEN = (0,255,0) #the rgb value for blue
BLUE = (0,0,255) #the rgb value for green
WHITE = (255,255,255) #the rgb value for white
BLACK = (0,0,0) #the rgb value for black

#images
background = pygame.image.load("background.jpg")
crosshair = pygame.image.load("crosshair.png")
target_img = pygame.image.load("target.png")

#sprites
class Player(pygame.sprite.Sprite):#defines the class
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale((crosshair), (70,70))
       self.rect = self.image.get_rect()#its hitbox is itself
       self.radius = 8
    def update(self):
        self.rect.center = (move)

class Target(pygame.sprite.Sprite):#defines the class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = (target_img)
        self.rect = self.image.get_rect()#its own hitbox
    def update(self):
        self.rect.center = (random.randrange(0,1500), random.randrange(0,700))

#score

score = 0 

#creates window
pygame.init() #intialises the window
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #sets the dinwo size to the width and the height stored in the variable above
pygame.display.set_caption("My Game") #sets the name of window to "My Game"
clock = pygame.time.Clock() #sets the clock speed of the window in a varibale called clock
pygame.mouse.set_visible(False)#removes the cursor on screen

player = Player()
aim = Target()
all_sprites = pygame.sprite.Group()
target = pygame.sprite.Group()
all_sprites.add(player)
target.add(aim)

#game loop
running = True
while running:
    #tick speed
    clock.tick(FPS) #sets the frame count to the FPS value at the start of the code
    #procesess input
    for event in pygame.event.get():
        move = pygame.mouse.get_pos()#sets the mouse postition in "move"
        player.update()#updates the postition of the player to the mouse position
        #check for closing window
        if event.type == pygame.QUIT: #allows for the user to x out of the game and it closes
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:#detects when the user clicks a mouse button
            if pygame.sprite.collide_circle(player, aim):
                score += 1
                aim.update()#updates the sprites postition
                print("your score is",score)
        #update
        all_sprites.update()
        #render
        screen.blit(background, (0, 0))
        target.draw(screen)
        all_sprites.draw(screen)
        #flip display
        pygame.display.flip() #sets the window so it shows the image

pygame.quit()
