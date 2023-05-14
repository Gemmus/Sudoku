import pygame
import requests

########################
#   Global Variables   #
########################

width = 800
play_width = 550
background_color = (255, 255, 255)

#######################
#   Calling the API   #
#######################

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=medium")
# Available difficulties: easy, medium, hard, random
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


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

    pygame.font.init()
    font = pygame.font.SysFont('arial', 40, bold=True)
    game_label = font.render('SUDOKU', 1, (0, 0, 0))

    win.blit(game_label, (width / 2 - game_label.get_width() / 2 + 26, 12))

    ##########################
    #   Creating the Grids   #
    ##########################

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    ##########################################
    #   Placing the Numbers into the Grids   #
    ##########################################

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
