import pygame
import requests

########################
#   Global Variables   #
########################

width = 800
play_width = 550
background_color = (255, 255, 255)
x_tuning = 3.5
y_tuning = 4

#######################
#   Calling the API   #
#######################

url = "https://sudoku-generator1.p.rapidapi.com/sudoku/generate"
api_key = ""  # add own

querystring = {"difficulty":"hard"}  # examples: {"seed":"1337", "difficulty":"medium"}, difficulties: easy, medium, hard

headers = {"X-RapidAPI-Key": api_key,
           "X-RapidAPI-Host": "sudoku-generator1.p.rapidapi.com"}

response = requests.get(url, headers=headers, params=querystring)

grid = response.json()['puzzle']

grid_original = [[0 for x in range(9)] for y in range(9)]
for i in range(0, 9):
    for j in range(0, 9):
        if grid[9*i+j].isdigit():
            grid_original[i][j] = int(grid[9*i+j])
        else:
            grid_original[i][j] = 0


######################################
#   Function for drawing the title   #
######################################

def draw_title(win):
    pygame.font.init()
    title_font = pygame.font.SysFont('arial', 40, bold=False)
    game_label = title_font.render('SUDOKU', 1, (0, 0, 0))

    win.blit(game_label, (width / 2 - game_label.get_width() / 2 + 26, 12))


#######################################
#   Function for creating the grids   #
#######################################

def draw_grid(win):
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()


#######################################################
#   Function for placing the Numbers into the Grids   #
#######################################################

def place_numbers(win):
    font = pygame.font.SysFont('arial', 35)

    for i in range(9):
        for ii in range(9):
            if 0 < grid_original[i][ii] < 10:
                value = font.render(str(grid[9*i+ii]), 1, (0, 0, 0))
                win.blit(value, ((ii + 1) * 50 + 18, (i + 1) * 50 + 8))

    pygame.display.update()


################################
#   Function for click event   #
################################

def insert(win, position):
    x, y = position[0]//50, position[1]//50
    font = pygame.font.SysFont('arial', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if 0 < x < 10 and 0 < y < 10:
                    if grid_original[y-1][x-1] != 0:
                        return
                    else:
                        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(1), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(2), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(3), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(4), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(5), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(6), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(7), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(8), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            value = font.render(str(9), 1, (125, 36, 69))
                            win.blit(value, (x * 50 + 18, y * 50 + 8))
                            pygame.display.update()
                            return
                        if event.key == pygame.K_0 or event.key == pygame.K_KP_0:
                            pygame.draw.rect(win, (255, 255, 255), (x * 54 - (x - 1) * x_tuning, y * 54 - (y - 1) * y_tuning, 40, 40))
                            pygame.display.update()
                            return
            return


def main():
    ###########################
    #   Setting up the Game   #
    ###########################

    pygame.init()
    win = pygame.display.set_mode((play_width, play_width))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    #########################
    #   Drawing the Title   #
    #########################

    draw_title(win)

    ##########################
    #   Creating the Grids   #
    ##########################

    draw_grid(win)

    ##########################################
    #   Placing the Numbers into the Grids   #
    ##########################################

    place_numbers(win)

    ########################
    #   Quiting the game   #
    ########################

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, pos)
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
