import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))


def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def start():
    print("Ok, let's go")


def menu():
    """ This is the menu that waits you to click the s key to start """
    b1 = button(screen, (100, 100), "1")
    b2 = button(screen, (300, 100), "2")
    b3 = button(screen, (500, 100), "3")
    b4 = button(screen, (100, 200), "1")
    b5 = button(screen, (300, 200), "2")
    b6 = button(screen, (500, 200), "3")
    b7 = button(screen, (100, 300), "1")
    b8 = button(screen, (300, 300), "2")
    b9 = button(screen, (500, 300), "3")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b5.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b6.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b7.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b8.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b9.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
        pygame.display.update()
menu()