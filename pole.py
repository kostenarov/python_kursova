import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))

counter = 0


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


def button2(screen, position, text, color):
    font = pygame.font.SysFont("Arial", 24)
    if color == "blue":
        text_render = font.render(text, 1, (0, 0, 255))
    elif color == "green":
        text_render = font.render(text, 1, (0, 255, 0))
    elif color == "red":
        text_render = font.render(text, 1, (255, 0, 0))
    elif color == "pink":
        text_render = font.render(text, 1, (255, 182, 193))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def buildings_menu():
    global buy_factory, buy_cleaning, buy_windturbine, exit
    buy_factory = button2(screen, (500, 100), "          BUY FACTORY         ", "red")
    buy_cleaning = button2(screen, (500, 150), "BUY CLEANING STATION", "blue")
    buy_windturbine = button2(screen, (500, 200), "          BUY WINDMILL         ", "green")
    exit = button2(screen, (500, 300), "                    EXIT                   ", "red")


def buy_menu():
    global buy_land
    buy_land = button2(screen, (500, 250), "                    BUY                   ", "pink")


def menu():
    global buy_factory, buy_cleaning, buy_windturbine, buy_land, counter, exit

    b = [[11, 12, 5], [15, 6, 10], [10, 8, 12], [12, 15, 8]]

    for i in range(3):
        for j in range(3):
            if i == 1:
                b[i][j] = button(screen, ((100 * (j + 1) ), 100), "      ")
            elif i == 2:
                b[i][j] = button(screen, ((100 * (j + 1)), 200), "      ")
            else:
                b[i][j] = button(screen, ((100 * (j + 1)), 300), "      ")

    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b[0][0].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                    counter = 1
                elif b[0][1].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b[0][2].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b[1][0].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b[1][1].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b[1][2].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b[2][0].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b[2][1].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()
                elif b[2][2].collidepoint(mx, my):
                    buy_menu()
                    buildings_menu()

                if buy_factory.collidepoint(mx, my):
                    print("factory")
                if buy_cleaning.collidepoint(mx, my):
                    print("cleaning station")
                if buy_windturbine.collidepoint(mx, my):
                    if counter == 1:
                        pygame.draw.rect(screen, (0, 255, 0), b1)
                if buy_land.collidepoint(mx, my):
                    if counter == 1:
                        pygame.draw.rect(screen, (255, 182, 193), b1)




        pygame.display.update()


menu()
