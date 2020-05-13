import pygame, random, time, sys,pygame_menu
from pygame import  mixer
pygame.init()
window = pygame.display.set_mode((720,720))
speed = 5
bird = pygame.image.load("marinka.png")
birdv2 = pygame.image.load("marinkav2.png")
bird_dead = pygame.image.load("marinkadie.png")

def set_difficulty(value, difficulty):
    global speed
    #print(value)
    #print(difficulty)
    if difficulty == 1:
        speed = 5
    if difficulty == 2:
        speed = 10

def customization(value,Character):
    global bird
    global birdv2
    global bird_dead
    if Character == 1:
        bird = pygame.image.load("marinka.png")
        birdv2 = pygame.image.load("marinkav2.png")
        bird_dead = pygame.image.load("marinkadie.png")
    if Character == 2:
        bird = pygame.image.load("aelitka.png")
        birdv2 = pygame.image.load("aelitav2.png")
        bird_dead = pygame.image.load("aelitkadie.png")

def start_the_game():
    mixer.Sound('bruh.wav').play()
    global speed
    global bird
    global birdv2
    global bird_dead
    pygame.display.set_icon(pygame.image.load("onima.jpg"))
    pygame.font.init()
    pygame.display.set_caption('school bird')
    bg = pygame.image.load("onima.jpg")
    mixer.music.load('rap_god.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    font = pygame.font.SysFont('Arial', 72)
    font2 = pygame.font.SysFont('Arial', 36)
    clock = pygame.time.Clock()
    start = False
    vel = 7.   #gravitation(only for jump)
    ypos = 300
    hscore = 0
    pipe = [720,random.randint(0,380)]     #x1,y1  width , height
    tscore = 0
    died = False
    caption = font2.render('Press SPACE to Start', True, (0, 0, 0), None)

    def difficulty(difficult):
        if difficult == "easy":
            return pipe[0] - 5.12
        if difficult == "hard":
            return pipe[0] - 7.5

    while True:

        window.fill((120,120,255))
        pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_SPACE]:
        #     mixer.Sound('sfx_wing.wav').play()
        #     print("pressed")
        if pressed[pygame.K_ESCAPE]:
            mixer.Sound('sfx_wing.wav').play()
            menu.mainloop(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if start == False:
                    ypos, start = 300, True
                vel = 7.

        if start:
            window.blit(bg,(0,0))
            window.blit(bird,(50,ypos))

            ypos, vel, pipe[0] = ypos - vel, vel - 0.5, pipe[0]-speed
            if vel>0:
                window.blit(birdv2, (50, ypos))
          #  if vel>0:
          #mixer.Sound('sfx_wing.wav').play()

            pygame.draw.rect(window,(0,255,0),(pipe[0],0,50,pipe[1]))                      #pipe[0] = 720 pipe[1] = random.randint(0,380)                                          (pipe[0]у нас 715()
                                                                                                                                                                                   
            pygame.draw.rect(window,(0,255,0),(pipe[0],pipe[1]+300,50,720))
                                                                                    #x1,y1,x2,x2   - mani release
                                                                                    
            window.blit(font2.render('Score: ' + str(tscore), False, (0,0,0), None),(10,10))   #render(text, antialias, color, background=None) -> Surface

            if pipe[0] < -50:                                             
                pipe, tscore = [720, random.randint(0,380)], tscore + 1   
                if tscore > hscore:
                    hscore = tscore
                # if tscore == 2:   #TODO TODO
                #     mixer.Sound('anime-wow-sound-effect-mp3cut.mp3').play()
                # if tscore == 10:
                #     mixer.Sound('sfx_wing.wav').play()
                # if tscore == 15:
                #     mixer.Sound('sfx_wing.wav').play()
                # if tscore == 20:
                #     mixer.Sound('Anime NANI MANGA.mp3').play()


        else:
            if died: #death screen
                #mixer.Sound('bruh.wav').play(1)
                window.blit(bird_dead,(100,500))

            window.blit(font.render('school bird', True, (0,0,0), None),(100,100))
            window.blit(caption,(100,300))
            window.blit(font2.render('High score - ' + str(hscore), True, (0,0,0), None),(100,400))

        if ypos >= 528 or ((pipe[0] < 164 and pipe[0] > 14) and (ypos+192 > pipe[1]+300 or ypos < pipe[1])):    #720-head size= 528 #164 на листе
            ypos = 528
            start = False
            tscore = 0
            pipe[0] = 720
            died = True
            caption = font2.render('You died. Press SPACE to restart game.', True, (0, 0, 0), None)

        elif ypos < 0: ######################
            ypos =-abs(vel)
            vel = 0
        clock.tick(60)
        pygame.display.flip()

menu = pygame_menu.Menu(720, 720, 'Welcome',
                       theme=pygame_menu.themes.THEME_SOLARIZED)
menu.add_text_input('Name :', default='Ricardo')
menu.add_selector('Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)  #value=('Easy', 1)-mi ne juzaem , difficulty=1
menu.add_selector('Character', [('Marinka', 1), ('Aelitka', 2)], onchange=customization)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(window)