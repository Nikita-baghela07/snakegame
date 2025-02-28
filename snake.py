import pygame as p
import random as r
import os
p.mixer.init()

p.init()


clock = p.time.Clock()
screen_width = 900
screen_height = 400

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

rgb = (173, 216, 230)  
p.display.set_caption("Snake Game")
game_window = p.display.set_mode((screen_width, screen_height))

bing= p.image.load("snake1.png")
bing1= p.image.load("snake.jpg")
bing = p.transform.scale(bing, (screen_width, screen_height)).convert_alpha()
bing1 = p.transform.scale(bing1, (screen_width, screen_height)).convert_alpha()
p.display.update()



font = p.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(game_window, color, snk, snake_size):
    for x, y in snk:
        p.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(white)
        game_window.blit(bing1, (0, 0))
        text_screen("snap ki duniya ma shuahgat hai", black, 220, 150)
        text_screen("khelne ka liya Space Bar click kara", black, 222, 200)
        for event in p.event.get():
            if event.type == p.QUIT:
                exit_game = True

            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    p.mixer.music.load("song.mp3")
                    p.mixer.music.play()
                    gameloop()

        p.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    fps = 60
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = r.randint(20, screen_width)
    food_y = r.randint(20, screen_height)
    score = 0
    snk = []
    snk_length = 1
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
      highscore = f.read()
      if not highscore:
            highscore = 0
      else:
            highscore = int(highscore)

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(highscore))

            game_window.fill(white)
            game_window.blit(bing, (0, 0))
            text_screen("ohh shit! game over ho gaya....", black, 100, 200)
            text_screen("phir se khelne ka liya enter click kara", black, 100, 240)
            text_screen("score: "+str(score), black, 300, 280)
            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game = True
                    

                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        gameloop()
        else:
            for event in p.event.get():
                if event.type == p.QUIT:
                    exit_game = True

                if event.type == p.KEYDOWN:
                    if event.key == p.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == p.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == p.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == p.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    
                    if event.key == p.K_a:
                        score += 5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                snk_length += 3
                if score > int(highscore):
                    highscore = score

                food_x = r.randint(20, screen_width )
                food_y = r.randint(20, screen_height )

            game_window.fill(rgb)
            
            text_screen("Score: " +   str(score )  +  "  Highscore:"+ str(highscore), red, 5, 5)
            p.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk.append(head)
            if len(snk) > snk_length:
                del snk[0]

            if head in snk[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                p.mixer.music.load("song1.mp3")
                p.mixer.music.play()
                

            plot_snake(game_window, black, snk, snake_size)
        clock.tick(fps)
        p.display.update()

    p.quit()
    quit()
welcome()
gameloop()