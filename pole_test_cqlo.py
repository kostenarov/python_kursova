import pygame
from buildings import Factory
from buildings import Windturbine
from buildings import Cleaning_station

pygame.init()

screen = pygame.display.set_mode((800, 600))
bgcolor = (0, 0, 0)
screen.fill(bgcolor)
clock = pygame.time.Clock()
counter = 0
income = 0


def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (144, 238, 144), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (144, 238, 144), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (128, 128, 128), (x, y, w, h))
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
    global buy_factory, buy_cleaning, buy_windturbine, upgrade
    buy_factory = button2(screen, (500, 100), "     BUY FACTORY: 1000   ", "red")
    buy_cleaning = button2(screen, (500, 150), " BUY CL. STATION: 3500  ", "blue")
    buy_windturbine = button2(screen, (500, 200), "     BUY WINDMILL: 2000  ", "green")
    upgrade = button2(screen, (500, 300), "       UPGRADE: 10000       ", "red")


def buy_menu():
    global buy_land
    buy_land = button2(screen, (500, 250), "               BUY: 1500             ", "pink")


def menu():
    global buy_factory, buy_cleaning, buy_windturbine, buy_land, counter, upgrade, clock, income
    factory = Factory(1000, 0.03, 0, 1.5)
    windturbine = Windturbine(2000, 0, 0, 0.5)
    cleaning_station = Cleaning_station(3500, 0.055, 0, 0)
    color = (0, 0, 0)
    money = 70000
    counter_factory = 0
    counter_windturbine = 0
    counter_cleaning_station = 0
    counter_factory_upgrade = 0
    counter_cleaning_station_upgrade = 0
    counter_windturbine_upgrade = 0
    polution = 0
    b = [[11, 12, 5, 2], [15, 6, 10, 3], [10, 8, 12, 6], [12, 15, 8, 69], [12, 15, 8, 69]]
    bought = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def display_text():
        font = pygame.font.SysFont("Stencil", 40)

        BarColor = (119, 136, 153)
        pygame.draw.rect(screen, color, pygame.Rect(610, 35, 170, 45))
        pygame.display.flip()
        Score_display = font.render(f"MONEY : {money}", 1, (5, 50, 32))
        screen.blit(Score_display, (450, 35))
        pygame.draw.rect(screen, BarColor, [80, 30, polution * 3, 30])

        pygame.display.update()

    for i in range(4):
        for j in range(4):
            if i == 1:
                b[i][j] = button(screen, ((90 * (j + 1)), 100), "      ")
            elif i == 2:
                b[i][j] = button(screen, ((90 * (j + 1)), 200), "      ")
            elif i == 3:
                b[i][j] = button(screen, ((90 * (j + 1)), 300), "      ")
            else:
                b[i][j] = button(screen, ((90 * (j + 1)), 400), "      ")
    running = 0
    while running == 0:
        mx, my = pygame.mouse.get_pos()
        money += income
        if counter_cleaning_station > 0 or counter_cleaning_station_upgrade > 0:
            polution = polution + factory.polution * (counter_factory + counter_factory_upgrade) - (cleaning_station.polution * counter_cleaning_station + 3 * cleaning_station.polution * counter_cleaning_station_upgrade)
            polution = round(polution, 2)
        else:
            polution = polution + factory.polution * (counter_factory + counter_factory_upgrade)

        display_text()

        if polution > 100:
            income = 0
            money = 0
            running = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, 4):
                    for j in range(0, 4):
                        if b[i][j].collidepoint(mx, my):
                            buy_menu()
                            buildings_menu()
                            save_i = i
                            save_j = j
                            pass

                if buy_land.collidepoint(mx, my) and money >= 1500 and bought[save_i][save_j] == 0:
                    pygame.draw.rect(screen, (255, 182, 193), b[save_i][save_j])
                    money = money - 1500
                    bought[save_i][save_j] = 10
                if buy_factory.collidepoint(mx, my) and money >= factory.cost and bought[save_i][save_j] == 10 and \
                        bought[save_i][save_j] != 11 and bought[save_i][save_j] != 12 and bought[save_i][save_j] != 13 and bought[save_i][save_j] != 21 and bought[save_i][save_j] != 22 and bought[save_i][save_j] != 23:
                    pygame.draw.rect(screen, (255, 0, 0), b[save_i][save_j])
                    money = money - factory.cost
                    counter_factory = counter_factory + 1
                    bought[save_i][save_j] = 11
                if buy_cleaning.collidepoint(mx, my) and money >= cleaning_station.cost and bought[save_i][
                    save_j] == 10 and bought[save_i][save_j] != 11 and bought[save_i][save_j] != 12 and bought[save_i][
                    save_j] != 13 and bought[save_i][save_j] != 21 and bought[save_i][save_j] != 22 and bought[save_i][save_j] != 23:
                    pygame.draw.rect(screen, (173,216,230), b[save_i][save_j])
                    money = money - cleaning_station.cost
                    counter_cleaning_station = counter_cleaning_station + 1
                    bought[save_i][save_j] = 12
                if buy_windturbine.collidepoint(mx, my) and money >= windturbine.cost and bought[save_i][
                    save_j] == 10 and bought[save_i][save_j] != 11 and bought[save_i][save_j] != 12 and bought[save_i][
                    save_j] != 13 and bought[save_i][save_j] != 21 and bought[save_i][save_j] != 22 and bought[save_i][save_j] != 23:
                    pygame.draw.rect(screen, (0, 255, 0), b[save_i][save_j])
                    money = money - windturbine.cost
                    counter_windturbine = counter_windturbine + 1
                    bought[save_i][save_j] = 13
                if upgrade.collidepoint(mx, my) and money >= 10000 and bought[save_i][save_j] == 11:
                    pygame.draw.rect(screen, (139,0,0), b[save_i][save_j])
                    money = money - 10000
                    counter_factory_upgrade = counter_factory_upgrade + 1
                    counter_factory = counter_factory - 1
                    bought[save_i][save_j] = 21
                if upgrade.collidepoint(mx, my) and money >= 10000 and bought[save_i][save_j] == 12:
                    pygame.draw.rect(screen, (0, 0, 255), b[save_i][save_j])
                    money = money - 10000
                    counter_cleaning_station_upgrade = counter_cleaning_station_upgrade + 1
                    counter_cleaning_station = counter_cleaning_station - 1
                    bought[save_i][save_j] = 22
                if upgrade.collidepoint(mx, my) and money >= 10000 and bought[save_i][save_j] == 13:
                    pygame.draw.rect(screen, (149,255,128), b[save_i][save_j])
                    money = money - 10000
                    counter_windturbine_upgrade = counter_windturbine_upgrade + 1
                    counter_windturbine = counter_windturbine - 1
                    bought[save_i][save_j] = 23
                else:
                    pass

        income = factory.income * counter_factory + windturbine.income * counter_windturbine + 1.5 * counter_factory_upgrade * factory.income + 1.5 * counter_windturbine_upgrade * windturbine.income
        money = round(money, 0)
        clock.tick(60)


menu()