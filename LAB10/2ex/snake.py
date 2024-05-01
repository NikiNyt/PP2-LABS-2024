import pygame
import psycopg2
import time
import random
from config import data
 
pygame.init()

config = psycopg2.connect(**data)

current = config.cursor()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
Food = 0

font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

username = input("Enter your name:")
select = '''
    SELECT * FROM snaketable WHERE player_name = %s;
'''
current.execute(select, [username])
DICT = current.fetchone()

if DICT == None:
    insert = '''
        INSERT INTO snaketable VALUES(%s, 0, 0);
    '''
    current.execute(insert, [username])
    config.commit()
pygame.init()

current.execute(select, [username])
DICT = current.fetchone()

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

hiscore = int(DICT[1])
level = int(DICT[2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width // 2
    y1 = dis_height // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    GameScore = 0
    hiscore = int(DICT[1])
    level = int(DICT[2])
    Food = 0
    Mright = False
    Mleft = False
    Mdown = False
    Mup = False
    
    ctimer = 0

    foodx = round(random.randrange(0, dis_width) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height) / 10.0) * 10.0

    while not game_over:
       
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press R-Restart or Q-Quit", red)
            Your_score(GameScore)
            pygame.display.update()
            sql = '''
                UPDATE snaketable SET player_score = %s, player_level = %s WHERE player_name = %s;
                '''
            current.execute(sql, [GameScore, level, username])
            config.commit()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        def FoodCreation():
         foodx = round(random.randrange(0, dis_width) / 10.0) * 10.0
         foody = round(random.randrange(0, dis_height) / 10.0) * 10.0
         Food = random.randrange(0,2)
         ctimer = pygame.time.get_ticks()
         return foodx, foody, Food, ctimer
        
        timer = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and Mright != True:
                    x1_change = -snake_block
                    y1_change = 0
                    Mright = False
                    Mleft = True
                    Mdown = False
                    Mup = False
                elif event.key == pygame.K_RIGHT and Mleft != True:
                    x1_change = snake_block
                    y1_change = 0
                    Mright = True
                    Mleft = False
                    Mdown = False
                    Mup = False
                elif event.key == pygame.K_UP and Mdown != True:
                    y1_change = -snake_block
                    x1_change = 0
                    Mright = False
                    Mleft = False
                    Mdown = False
                    Mup = True
                elif event.key == pygame.K_DOWN and Mup != True:
                    y1_change = snake_block
                    x1_change = 0
                    Mright = False
                    Mleft = False
                    Mdown = True
                    Mup = False

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        if Food == 0:
         pygame.draw.rect(dis, (0, 255, 0), [foodx, foody, snake_block, snake_block])
        if Food == 1:
         pygame.draw.rect(dis, (255, 0, 0), [foodx, foody, snake_block * 2, snake_block * 2])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(GameScore)
        if GameScore > hiscore:
           hiscore = GameScore
        if GameScore - 10 == 0:
           level += 1
        pygame.display.update()
        if Food == 0:
         if x1 == foodx and y1 == foody:
            Length_of_snake += 1
            GameScore += 1
            foodx, foody, Food, ctimer = FoodCreation()
        elif Food == 1:    
            if x1 in (foodx, foodx+10) and y1 in (foody, foody+10):
             Length_of_snake += 2
             GameScore += 10
             foodx, foody, Food, ctimer = FoodCreation()
        if timer > ctimer + 6000:
           foodx, foody, Food, ctimer = FoodCreation()
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

sql = '''
        UPDATE snaketable SET player_score = %s, player_level = %s WHERE player_name = %s;
    '''
current.execute(sql, [hiscore, level, username])
config.commit()
current.close()
config.close()
