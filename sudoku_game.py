import pygame

width = 800
play_width = 550
background_color = (255, 255, 255)

top_left_x = (width - play_width) // 2
top_left_y = (width - play_width)


def main():
    pygame.init()
    win = pygame.display.set_mode((play_width, play_width))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    pygame.font.init()
    font = pygame.font.SysFont('arial', 40, bold=True)
    game_label = font.render('SUDOKU', 1, (0, 0, 0))

    win.blit(game_label, (width / 3 - game_label.get_width() / 2 + 9, 4))

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
