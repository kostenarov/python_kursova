import pygame
#import sys


pygame.init()

screen = pygame.display.set_mode((800, 500))


def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (144, 238, 144), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (144, 238, 144), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 150, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def button2(screen, position, text):
    font = pygame.font.SysFont("Arial", 24)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def buildings_menu():
    global buy_factory, buy_cleaning, buy_windturbine
    buy_factory = button2(screen, (500, 100), "          BUY FACTORY         ")
    buy_cleaning = button2(screen, (500, 150), "BUY CLEANING STATION")
    buy_windturbine = button2(screen, (500, 200), "          BUY WINDMILL         ")


def menu():
    global buy_factory, buy_cleaning, buy_windturbine
    b1 = button(screen, (100, 100), "      ")
    b2 = button(screen, (200, 100), "      ")
    b3 = button(screen, (300, 100), "      ")
    b4 = button(screen, (100, 200), "      ")
    b5 = button(screen, (200, 200), "      ")
    b6 = button(screen, (300, 200), "      ")
    b7 = button(screen, (100, 300), "      ")
    b8 = button(screen, (200, 300), "      ")
    b9 = button(screen, (300, 300), "      ")

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(mx, my):
                    buildings_menu()
                elif b2.collidepoint(mx, my):
                    buildings_menu()
                elif b3.collidepoint(mx, my):
                    buildings_menu()
                elif b4.collidepoint(mx, my):
                    buildings_menu()
                elif b5.collidepoint(mx, my):
                    buildings_menu()
                elif b6.collidepoint(mx, my):
                    buildings_menu()
                elif b7.collidepoint(mx, my):
                    buildings_menu()
                elif b8.collidepoint(mx, my):
                    buildings_menu()
                elif b9.collidepoint(mx, my):
                    buildings_menu()
                if buy_factory.collidepoint(pygame.mouse.get_pos()):
                    print("factory")
                if buy_cleaning.collidepoint(pygame.mouse.get_pos()):
                    print("cleaning station")
                if buy_windturbine.collidepoint(pygame.mouse.get_pos()):
                    print("windturbine")
        pygame.display.update()
menu()