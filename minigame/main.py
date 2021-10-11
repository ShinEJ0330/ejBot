# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#from tkinter import *
import pygame
#import multiprocessing

def impo_memory():
    import MemoryGame

def impo_snake():
    import snake

# def worker(file):
#     # your subprocess code
#     print("worker")

def display_game_screen():
    msg = game_font.render("Memory", True, BLACK)
    msg_rect = msg.get_rect(center=memoryButton.center)
    screen_main.blit(msg, msg_rect)

    msg2 = game_font.render("Snake", True, BLACK)
    msg_rect2 = msg2.get_rect(center=snakeButton.center)
    screen_main.blit(msg2, msg_rect2)

def check_buttons(pos):
    if memoryButton.collidepoint(pos):
        impo_memory()
    elif snakeButton.collidepoint(pos):
        impo_snake()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #open('C:\\Users\\kccistc\\PycharmProjects\\minigame\\MemoryGame.py', 'r', encoding='UTF8')
    #exec(compile(open(MemoryGame, "rb").read(), MemoryGame, 'exec'))
    # exec(open('snake.py').read())
    print("Main")
    # root = Tk()
    # width = 300
    # height = 300
    # wi = root.winfo_screenwidth()
    # he = root.winfo_screenheight()
    # root.geometry("%dx%d+%d+%d" % (width, height, wi/2-width/2, he/2-height/2))
    # root.title = "Main Page"
    # btn = Button(root, width = "20", text = "기억력게임", commend = impo()).grid(row = 1, column = 1)
    # root.mainloop()

    # files = ["C:\\Users\\kccistc\\PycharmProjects\\minigame\\MemoryGame.py", "C:\\Users\\kccistc\\PycharmProjects\\minigame\\snake.py"]
    # for i in files:
    #     p = multiprocessing.Process(target=worker, args=(i,))
    #     p.start()

    # 초기화
    pygame.init()
    pygame.font.init()
    screen_width = 1280  # 가로 크기
    screen_height = 720  # 세로 크기
    screen_main = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Main Page")
    game_font = pygame.font.SysFont("arialrounded", 100)  # 폰트 정의 (Pyinstaller 패키징을 위해 폰트 명시)

    # 기억력 게임 버튼
    memoryButton = pygame.Rect(0, 0, 120, 120)
    memoryButton.center = (screen_width / 4, screen_height / 2)

    # 뱀 게임 버튼
    snakeButton = pygame.Rect(0, 0, 120, 120)
    snakeButton.center = (screen_width / 4 * 3, screen_height / 2)

    # 색깔
    BLACK = (0, 0, 0)  # RGB
    WHITE = (255, 255, 255)
    GRAY = (50, 50, 50)

    # 게임 루프
    running = True  # 게임이 실행중인가?
    while running:
        click_pos = None

        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트인가?
                running = False  # 게임이 더 이상 실행중이 아님
            elif event.type == pygame.MOUSEBUTTONUP:  # 사용자가 마우스를 클릭했을때
                click_pos = pygame.mouse.get_pos()

        screen_main.fill(WHITE)

        display_game_screen()

        # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
        if click_pos:
            check_buttons(click_pos)
        # 화면 업데이트
        pygame.display.update()

    # 5초 정도 보여줌
    # pygame.time.delay(5000)

    # 게임 종료
    pygame.quit()
