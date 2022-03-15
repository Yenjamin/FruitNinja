import pygame
import fruitloop

WIDTH = 800
HEIGHT = 500
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']
data = {}
for fruit in fruits:
    data[fruit] = fruitloop.generate_random_fruits(fruit, data)
clock = pygame.time.Clock()
background = pygame.image.load("sources/back.jpg") 

def display():
    pygame.init()
    pygame.display.set_caption("Fruity Ninja")
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    gameloop(window)

def gameloop(display):
    score = 0
    playerLives = 3
    FPS = 11
    font = pygame.font.Font("sources/comic.ttf", 42)
    scoreText = font.render("Score : " + str(score), True, (255, 255, 255))
    first = True
    while True:
        if first == True:
            frontScreen(display, first, score)
            first = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(background, (0, 0))
        display.blit(scoreText, (0, 0))
        drawUsedLives(display, 690, 5, playerLives, "sources/images/white_lives.png")
        drawRemainLives(display, 760, 5, playerLives, "sources/images/red_lives.png")
        for name, value in data.items():
            if value["throw"]:
                value["x"] += value["speed_x"]
                value["y"] += value["speed_y"]
                value["speed_y"] += (1 * value["t"])
                value["t"] += 1
                if value['y'] <= 800:
                    display.blit(value['img'], (value['x'], value['y']))
                else:
                    data[name] = fruitloop.generate_random_fruits(name, data)
                position = pygame.mouse.get_pos()
                if not value['hit'] and position[0] > value['x'] and position[0] < value['x']+60 and position[1] > value['y'] and position[1] < value['y']+60:
                    if name == "bomb":
                        playerLives -= 1
                        half_fruit_path = "sources/images/explosion.png"
                        if playerLives == 0:
                            frontScreen(display, first, score)
                            score = 0
                            playerLives = 3
                            FPS = 11
                    else:
                        half_fruit_path = "sources/images/half_" + name + ".png"
                    value["img"] = pygame.image.load(half_fruit_path)
                    value["speed_x"] += 10
                    if name != "bomb" :
                        if score % 10 == 0:
                            if FPS < 20:
                                FPS += 1
                        score += 1
                    scoreText = font.render('Score : ' + str(score), True, (255, 255, 255))
                    value['hit'] = True
            else:
                data[name] = fruitloop.generate_random_fruits(name, data)
        pygame.display.update()
        clock.tick(FPS)

def draw_text(display, text, size, x, y):
    fontName = pygame.font.match_font("sources/comic.ttf")
    font = pygame.font.Font(fontName, size)
    textDraw = font.render(text, True, (255,255,255))
    rect = textDraw.get_rect()
    rect.midtop = (x, y)
    display.blit(textDraw, rect)

def drawUsedLives(display, x, y, lives, image) :
    for i in range(lives):
        img = pygame.image.load(image)
        rect = img.get_rect()
        rect.x = int(x + 35 * i)
        rect.y = y
        display.blit(img, rect)

def drawRemainLives(display, x, y, lives, image) :
    for i in range (3 - lives):
        img = pygame.image.load(image)
        rect = img.get_rect()
        rect.x = int(x - 35 * i)
        rect.y = y
        display.blit(img, rect)

def frontScreen(display, first, score):
    display.blit(background, (0,0))
    draw_text(display, "FRUIT NINJA!", 90, WIDTH / 2, HEIGHT / 4)
    if not first:
        draw_text(display,"Score : " + str(score), 50, WIDTH / 2, HEIGHT /2)

    draw_text(display, "Press a key to begin!", 64, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                waiting = False
