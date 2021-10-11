# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:55:26 2021

@author: kccistc
"""

import pygame
from random import *

# 숫자 섞기 (이 프로젝트에서 가장 중요)
def shuffle_red():
    global grid, rows, columns, cell_size
    
    while True:
        row_idx = randrange(0, rows)
        col_idx = randrange(0, columns)
        
        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = 2;
            break

# pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start, start_ticks
    
    if start: # 게임이 시작했으면?
        check_key(pos)
    elif pos == "Enter":
        start = True
    # elif start_button.collidepoint(pos): # 게임 시작버튼을 눌렀을 때
    #     start = True
    

def check_key(pos):
    global way
    
    if way == "Right" and pos == "Left" or \
       way == "Left" and pos == "Right" or \
       way == "Up" and pos == "Down" or \
       way == "Down" and pos == "Up":
        return

    way = pos
    snake_move()

def snake_move():
    global way, grid, snake_x, snake_y, rows, columns
    
    if way == "Right":
        if snake_x[len(snake_x)-1] == columns - 1: # 화면 가장자리에 부딪히는 경우
            game_over()
        elif grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] + 1] == 0: # 뱀 머리의 오른쪽이 비엇을경우
            grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] + 1] = 1 # 뱀 머리의 오른쪽칸을 1로
            grid[snake_y[0]][snake_x[0]] = 0;   # 뱀 꼬리칸을 0으로
            snake_x.append(snake_x[len(snake_x)-1] + 1)
            snake_x.pop(0)
            snake_y.append(snake_y[len(snake_y)-1])
            snake_y.pop(0)
        elif grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] + 1] == 2:
            grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] + 1] = 1
            snake_x.append(snake_x[len(snake_x)-1] + 1)
            snake_y.append(snake_y[len(snake_y)-1])
            shuffle_red()
        elif grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] + 1] == 1:
            game_over()
    elif way == "Left":
        if snake_x[len(snake_x)-1] == 0:
            game_over()
        elif grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] - 1] == 0:
            grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] - 1] = 1
            grid[snake_y[0]][snake_x[0]] = 0;
            snake_x.append(snake_x[len(snake_x)-1] - 1)
            snake_x.pop(0)
            snake_y.append(snake_y[len(snake_x)-1])
            snake_y.pop(0)
        elif grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] - 1] == 2:
            grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] - 1] = 1
            snake_x.append(snake_x[len(snake_x)-1] - 1)
            snake_y.append(snake_y[len(snake_y)-1])
            shuffle_red()
        elif grid[snake_y[len(snake_y) - 1]][snake_x[len(snake_x)-1] - 1] == 1:
            game_over()
    elif way == "Up":
        if snake_y[len(snake_y)-1] == 0:
            game_over()
        elif grid[snake_y[len(snake_y) - 1] - 1][snake_x[len(snake_x)-1]] == 0:
            grid[snake_y[len(snake_y) - 1] - 1][snake_x[len(snake_x)-1]] = 1 
            grid[snake_y[0]][snake_x[0]] = 0;
            snake_x.append(snake_x[len(snake_x)-1])
            snake_x.pop(0)
            snake_y.append(snake_y[len(snake_y)-1] - 1)
            snake_y.pop(0)
        elif grid[snake_y[len(snake_y) - 1] - 1][snake_x[len(snake_x)-1]] == 2:
            grid[snake_y[len(snake_y) - 1] - 1][snake_x[len(snake_x)-1]] = 1 
            snake_x.append(snake_x[len(snake_x)-1])
            snake_y.append(snake_y[len(snake_y)-1] - 1)
            shuffle_red()
        elif grid[snake_y[len(snake_y) - 1] - 1][snake_x[len(snake_x)-1]] == 1:
            game_over()
    elif way == "Down":
        if snake_y[len(snake_y)-1] == rows - 1:
            game_over()
        elif grid[snake_y[len(snake_y) - 1] + 1][snake_x[len(snake_x)-1]] == 0:
            grid[snake_y[len(snake_y) - 1] + 1][snake_x[len(snake_x)-1]] = 1 
            grid[snake_y[0]][snake_x[0]] = 0;   # 뱀 꼬리칸을 0으로
            snake_x.append(snake_x[len(snake_x)-1])
            snake_x.pop(0)
            snake_y.append(snake_y[len(snake_y)-1] + 1)
            snake_y.pop(0)
        elif grid[snake_y[len(snake_y) - 1] + 1][snake_x[len(snake_x)-1]] == 2:
            grid[snake_y[len(snake_y) - 1] + 1][snake_x[len(snake_x)-1]] = 1 
            snake_x.append(snake_x[len(snake_x)-1])
            snake_y.append(snake_y[len(snake_y)-1] + 1)
            shuffle_red()
        elif grid[snake_y[len(snake_y) - 1] + 1][snake_x[len(snake_x)-1]] == 1:
            game_over()
            
# 시작 화면 보여주기
def display_start_screen():
    #pygame.draw.rect(screen, WHITE, [screen_width/2, screen_height/2, 50, 10], 60, 5)
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button 의 중심좌표를 따라가고,
    # 반지름은 60, 선 두께는 5
    make_grid()
    
    startImg = pygame.image.load("pressEnterToPlay.png")
    startImg_rect = startImg.get_rect()
    startImg_rect.centerx = screen_width / 2
    startImg_rect.y = 380
    screen.blit(startImg, startImg_rect)
    
    """
    msg = game_font.render("Start", True, BLACK)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)
    """

# 게임 화면 보여주기
def display_game_screen():
    global grid, rows, columns, cell_size, screen_left_margin, screen_top_margin
    text = game_font.render("Game",True,(0,0,0))
    txt = text.get_rect(center=(screen_width/2 - 55,screen_height/2))
    screen.blit(text,txt)
    make_grid()

def make_grid():
    global grid, rows, columns, cell_size, screen_left_margin, screen_top_margin
    for row in range(rows):
        for col in range(columns):
            x = screen_left_margin + (col * cell_size)
            y = screen_top_margin + (row * cell_size)
            if grid[row][col] == 1:
                pygame.draw.rect(screen, BLACK, [x, y, cell_size, cell_size])
            elif grid[row][col] == 2:
                pygame.draw.rect(screen, RED, [x, y, cell_size, cell_size])
            else:
                pygame.draw.rect(screen, GRAY, [x, y, cell_size, cell_size])

# 게임 종료 처리. 메시지도 보여줌
def game_over():
    global running
    running = False
    
    msg = game_font.render("Game Over", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)


# 초기화
pygame.init()
pygame.font.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
game_font = pygame.font.SysFont("arialrounded", 100) # 폰트 정의 (Pyinstaller 패키징을 위해 폰트 명시)

"""
# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (screen_width / 2, 380)
"""

# 색깔
BLACK = (0, 0, 0) # RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# 게임판
grid = []
snakes = []

rows = 13
columns = 15
cell_size = 50 # 각 Grid cell 별 가로, 세로 크기

screen_left_margin = 265 # 전체 스크린 왼쪽 여백
screen_top_margin = 20 # 전체 스크린 위쪽 여백

grid = [[0 for col in range(columns)] for row in range(rows)] # 13 x 15

# 초기 뱀 위치
snake_x = [4, 5]
snake_y = [6, 6]

for idx in range(len(snake_x)):
    grid[snake_y[idx]][snake_x[idx]] = 1
# 초기 열매 위치
grid[6][10] = 2

way = "Right" # 뱀 진로방향

# 게임 시작 여부
start = False

# 게임 루프
running = True # 게임이 실행중인가?

while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실행중이 아님
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을때
            click_pos = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                click_pos = "Enter"
            if event.key == pygame.K_LEFT:
                click_pos = "Left"
            if event.key == pygame.K_RIGHT:
                click_pos = "Right"
            if event.key == pygame.K_UP:
                click_pos = "Up"
            if event.key == pygame.K_DOWN:
                click_pos = "Down"


    # 화면 전체를 까맣게 칠함
    screen.fill(WHITE)

    if start:
        display_game_screen() # 게임 화면 표시
        snake_move()
    else:
        display_start_screen() # 시작 화면 표시

    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()
    pygame.time.delay(100)

# 5초 정도 보여줌
pygame.time.delay(3000)

# 게임 종료
pygame.quit()

