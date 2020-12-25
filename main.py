import pygame
import random
from pygame import mixer
import pyglet
import time


pygame.init()
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()
global img_g
img_g = []
for img in range(1,6):
    image = pygame.image.load(f'./img/a{img}.png')
    pygame.transform.rotozoom(image,0,2)
    img_g.append(image)
bg = pygame.image.load('theme.png')
background = pygame.image.load('sasha.png')
background1 = pygame.image.load('bg3a.png')
background2 = pygame.image.load('bg4.png')

background3 = pygame.image.load('bg5.png')
background4 = pygame.image.load('bg6.png')
intro1 = pygame.image.load('erenvstitan.png')
intro2 = pygame.image.load('stage10.png')
intro3 = pygame.image.load('erenvsfemalett.png')
intro4 = pygame.image.load('intro4.png')
crashed_user = pygame.image.load('crashed_user.png')
crashed_user2 = pygame.image.load('levis_crashed.png')
crashed_user3 = pygame.image.load('crashed_tt3.png')
crashed_user4 = pygame.image.load('crashed_mikasa.png')
sprite_image = pygame.image.load("lose.gif").convert_alpha()
user = pygame.image.load('head2.png')
user1 = pygame.image.load('eren.png')
user2 = pygame.image.load('levis.png')
user3 = pygame.image.load('tt3.png')
user4 = pygame.image.load('mikasa.png')
chicken = pygame.image.load('potato.png')
tt = pygame.image.load('tt.png')
tt2 = pygame.image.load('beast_titan.png')
tt3 = pygame.image.load('ftt.png')
tt4 = pygame.image.load('tt4.png')
score = 0
clock = pygame.time.Clock()

time = 80
x = 2
mixer.music.load('./song/titan1.mp3')
mixer.music.play(-1)


def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'Score: ' + str(score)
    text_img = font.render(score_text, True, (0,255,0))
    screen.blit(text_img, [20, 10])

def display_animation(file):
    animation = pyglet.image.load_animation(file)
    animSprite = pyglet.sprite.Sprite(animation)


    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r,g,b,alpha = 0.5,0.5,0.8,0.5


    pyglet.gl.glClearColor(r,g,b,alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()




    pyglet.app.run()
    window.clear()




def display_lose():
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text = 'You lose'
    text_img = font.render(text, True, (255,0,0))
    screen.blit(text_img, [100, 140])
    for i in img_g:
        screen.blit(i,[0, 240])
        pygame.display.update()
        pygame.time.wait(700)

def display_stage():
    global x
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text = f'Stage {x}'
    text_img = font.render(text, True, (0,0,255))
    screen.blit(text_img, [100, 100])

    if x > 1 and x < 5:
        screen.blit(intro1,(0,210))
    elif x >= 5 and x < 15:
        screen.blit(intro2,(0,210))
    elif x >= 15 and x < 25:
        screen.blit(intro3,(0,210))
    elif x >= 25:
        screen.blit(intro4,(0,210))

    x += 1



def display_win(text):
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text = text
    text_img = font.render(text, True, (0,255,0))
    screen.blit(text_img, [100, 140])
    # screen.blit(img_g[1],[0, 140])







def crashed(idx):
    global score
    global keep_alive
    global time
    global user_x
    global x
    score = score + 30
    # print('crashed with chicken', idx)
    chicken_y[idx] = random_offset()

    if x > 2 and x < 6:
        screen.blit(crashed_user, [user_x,490])
        pygame.display.update()
        pygame.time.wait(50)
        mixer.Sound('./song/slash.mp3').play()
    elif x>= 6 and x < 16:
        screen.blit(crashed_user2, [user_x,490])
        pygame.display.update()
        pygame.time.wait(50)
        mixer.Sound('./song/slash.mp3').play()
    elif x>= 16 and x < 26:
        screen.blit(crashed_user3, [user_x,490])
        pygame.display.update()
        pygame.time.wait(50)
        mixer.Sound('./song/slash.mp3').play()
    elif x>= 26:
        screen.blit(crashed_user4, [user_x,490])
        pygame.display.update()
        pygame.time.wait(50)
        mixer.Sound('./song/slash.mp3').play()

    else:
        mixer.Sound('./song/crash.mp3').play()
    # mixer.Sound.play('./song/crash.mp3')
    if score < -300:
        # pygame.display.update()
        display_lose()
        pygame.display.update()

        pygame.time.wait(5000)
        score = 0
        chicken_y[0] = random_offset()
        chicken_y[1] = random_offset()
        chicken_y[2] = random_offset()
        # keep_alive = False
    if score >= 100:

        chicken_y[0] = random_offset()
        chicken_y[1] = random_offset()
        chicken_y[2] = random_offset()
        display_win('You Won')
        pygame.display.update()
        pygame.time.wait(3000)
        if x > 1 and x< 5:
            screen.blit(background1, (0, 0))

        elif x >= 5 and x < 15:
            screen.blit(background2, (0, 0))
        elif x >= 15 and x < 25:
            screen.blit(background3, (0, 0))
        elif x >= 25 and x < 31:
            screen.blit(background4, (0, 0))
        elif x >= 31:

            screen.blit(background4, (0, 0))
            display_win('The End')
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.display.quit()
            display_animation('finalone.gif')

            x = -999
            return x

        else:
            screen.blit(background, (0, 0))

        score = 0
        time = time + 50
        display_stage()
        pygame.display.update()
        pygame.time.wait(5000)


def random_offset():
    return -1*random.randint(100, 1500)


chicken_y = [random_offset(), random_offset(), random_offset()]


def update_chicken_pos(idx):
    global user_x
    global score
    if chicken_y[idx] > 600:
        chicken_y[idx] = random_offset()
        score -= 20
        # print(score)
    else:
        chicken_y[idx] = chicken_y[idx] + 5

user_x = 150


keep_alive = True

screen.blit(bg, [0, 0])
font = pygame.font.SysFont('Comic Sans MS', 50)
font1 = pygame.font.SysFont('Linotext', 40)
text = f'Stage 1'
text_img = font.render(text, True, (0,0,255))
text1 = 'Attack On Titan'
text_img1 = font1.render(text1, True, (255,0,0))
screen.blit(text_img, [80, 130])
screen.blit(text_img1, [60, 100])


# screen.blit(background, [0,0])
# display_win('Attack on Titan \n'
#             'Stage 1')
pygame.display.update()
pygame.time.wait(5000)


while keep_alive:
    if score < -300:
        # pygame.display.update()
        display_lose()
        pygame.display.update()

        pygame.time.wait(5000)
        score = 0
        chicken_y[0] = random_offset()
        chicken_y[1] = random_offset()
        chicken_y[2] = random_offset()
    if x > 2 and x < 6:
        screen.blit(background1, [0,0])
        screen.blit(user1, [user_x,490])
        screen.blit(tt, [0, chicken_y[0]])
        screen.blit(tt, [150, chicken_y[1]])
        screen.blit(tt, [280, chicken_y[2]])


    elif x >= 6 and x < 16:
        screen.blit(background2, [0,0])
        screen.blit(user2, [user_x,490])
        screen.blit(tt2, [0, chicken_y[0]])
        screen.blit(tt2, [150, chicken_y[1]])
        screen.blit(tt2, [280, chicken_y[2]])

    elif x >= 16 and x < 26 :
        screen.blit(background3, [0,0])
        screen.blit(user3, [user_x,490])
        screen.blit(tt3, [0, chicken_y[0]])
        screen.blit(tt3, [150, chicken_y[1]])
        screen.blit(tt3, [280, chicken_y[2]])

    elif x >= 26  :
        screen.blit(background4, [0,0])
        screen.blit(user4, [user_x,490])
        screen.blit(tt4, [0, chicken_y[0]])
        screen.blit(tt4, [150, chicken_y[1]])
        screen.blit(tt4, [280, chicken_y[2]])

    else:
        screen.blit(background, [0,0])
        screen.blit(user, [user_x,490])
        screen.blit(chicken, [0, chicken_y[0]])
        screen.blit(chicken, [150, chicken_y[1]])
        screen.blit(chicken, [280, chicken_y[2]])


    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 280:
        user_x += 10
    if keys[pygame.K_LEFT] and user_x > 0 :
        user_x -= 10

    update_chicken_pos(0)
    update_chicken_pos(1)
    update_chicken_pos(2)





    if chicken_y[0] > 500 and user_x < 80:
        crashed(0)

    if chicken_y[1] > 500 and user_x > 70 and user_x <220:
        crashed(1)

    if chicken_y[2] > 500 and user_x > 210:
        crashed(2)

    if x == -999:
        break
    display_score(score)
    pygame.display.update()
    clock.tick(time)
