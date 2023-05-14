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

url = "https://sudoku-generator1.p.rapidapi.com/sudoku/generate"
api_key = ""

# querystring = {"seed":"1337"}
# querystring = {"seed":"1337", "difficulty":"easy}
# querystring = {"seed":"1337", "difficulty":"medium"}
querystring = {"seed":"1337", "difficulty":"hard"}

headers = {"X-RapidAPI-Key": api_key,
           "X-RapidAPI-Host": "sudoku-generator1.p.rapidapi.com"}

# response = requests.get(url, headers=headers, params=querystring)

# grid = response.json()['puzzle']
grid = "...46.....8.2..73.9....7...6....2.4..15...2.9.4...8........6..17....49.3..9...5.."
print(grid)

# grid_original = [[0 for x in range(9)] for y in range(9)]
# for i in range(0, 9):
#     for j in range(0, 9):
#         if grid[9*i+j].isdigit():
#             grid_original[i][j] = int(grid[9*i+j])
#         else:
#             grid_original[i][j] = 0

grid_original = [[0, 0, 0, 4, 6, 0, 0, 0, 0], [0, 8, 0, 2, 0, 0, 7, 3, 0], [9, 0, 0, 0, 0, 7, 0, 0, 0], [6, 0, 0, 0, 0, 2, 0, 4, 0], [0, 1, 5, 0, 0, 0, 2, 0, 9], [0, 4, 0, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 6, 0, 0, 1], [7, 0, 0, 0, 0, 4, 9, 0, 3], [0, 0, 9, 0, 0, 0, 5, 0, 0]]

print(grid_original)


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

    my_font = pygame.font.SysFont('arial', 35)

    for i in range(9):
        for ii in range(9):
            if 0 < grid_original[i][ii] < 10:
                value = my_font.render(str(grid[9*i+ii]), 1, (0, 0, 0))
                win.blit(value, ((ii + 1) * 50 + 15, (i + 1) * 50 + 15))

    pygame.display.update()

    ########################
    #   Quiting the game   #
    ########################

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
