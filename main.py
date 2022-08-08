import time

import pygame
import sys

pygame.init()
WINDOW_SIZE = WIDTH, HEIGHT = 602, 602
BG_COLOR = (93, 244, 221)
BOX_COLOR = (123, 187, 229)
(BOX_WIDTH, BOX_HEIGHT) = (WIDTH / 3, HEIGHT / 3)

window = pygame.display.set_mode(WINDOW_SIZE)


class Box:
    def __init__(self, row, col):
        self.x = col * BOX_WIDTH
        self.y = row * BOX_HEIGHT
        self.clicked = False
        self.isX = None
        self.image = None

    def setImage(self, isX):
        self.isX = isX
        if isX:
            self.image = pygame.image.load("x.png")
        else:
            self.image = pygame.image.load("o.png")

    def draw(self):
        if self.image is None:
            window.fill(BOX_COLOR, (self.x, self.y, BOX_WIDTH - 2, BOX_HEIGHT - 2))
        else:
            window.blit(self.image, (self.x, self.y, BOX_WIDTH - 5, BOX_HEIGHT - 5))


if __name__ == '__main__':
    grid = [[Box(i, j) for i in range(3)] for j in range(3)]
    is_x_round = True
    playing = True
    winner = None

    while playing:
        playing = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i, j = x // BOX_HEIGHT, y // BOX_WIDTH
                i, j = int(i), int(j)
                print(i, end=' ')
                print(j)
                currentBox = grid[i][j]

                if not currentBox.clicked:
                    currentBox.clicked = True
                    currentBox.setImage(is_x_round)
                    is_x_round = not is_x_round

        window.fill(BG_COLOR)
        for rows in grid:
            for box in rows:
                if box.clicked is False:
                    playing = True
                box.draw()
        row = None
        if grid[0][0].isX == grid[0][1].isX == grid[0][2].isX and grid[0][0].isX is not None:
            row = 0
        elif grid[1][0].isX == grid[1][1].isX == grid[1][2].isX and grid[1][0].isX is not None:
            row = 1
        elif grid[2][0].isX == grid[2][1].isX == grid[2][2].isX and grid[2][0].isX is not None:
            row = 2

        if row is not None:
            playing = False
            if grid[row][0].isX:
                winner = 'X'
            else:
                winner = 'O'
            break

        col = None
        if grid[0][0].isX == grid[1][0].isX == grid[2][0].isX and grid[0][0].isX is not None:
            col = 0
        elif grid[0][1].isX == grid[1][1].isX == grid[2][1].isX and grid[0][1].isX is not None:
            col = 1
        elif grid[0][2].isX == grid[1][2].isX == grid[2][2].isX and grid[0][2].isX is not None:
            col = 2

        if col is not None:
            playing = False
            if grid[0][col].isX:
                winner = 'X'
            else:
                winner = 'O'
            break

        if (grid[0][0].isX == grid[1][1].isX == grid[2][2].isX or grid[0][2].isX == grid[1][1].isX == grid[2][0].isX) \
                and grid[1][1].isX is not None:
            playing = False
            if grid[1][1].isX:
                winner = 'X'
            else:
                winner = 'O'
            break

        pygame.display.update()

    start = time.time()
    end = time.time()
    font = pygame.font.Font('freesansbold.ttf', 32)

    message = ""
    if winner is None:
        message = "TIE"
    else:
        if winner == 'X':
            message = "\"X\" WON THE GAME"
        else:
            message = "\"O\" WON THE GAME"

    text = font.render(message, True, (0, 150, 100))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)

    while end - start < 10:
        clock = font.render(str(int(10-(end-start))), True, (200, 0, 0))
        clockRect = clock.get_rect()

        window.fill((255, 255, 150))
        window.blit(text, textRect)
        window.blit(clock, clockRect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        end = time.time()

    sys.exit()
