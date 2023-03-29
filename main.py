import pygame
from pygame.locals import *
from sys import exit


class Game:

    def __init__(self, size_factor_X = 18, size_factor_Y = 12):
        """
        :param size_factor_X: Nombre de tuiles horizontales
        :param size_factor_Y: Nombre de tuiles verticales
        """
        self.size_X, self.size_Y = 64, 64
        self.background_image_filename = "assets/Ground_Tile_01_A_64x64.png"
        self.tank_image_filename = "assets/Hull_02_64x64.png"

        self.size_factor_X, self.size_factor_Y = size_factor_X, size_factor_Y

        pygame.init()
        self.screen = pygame.display.set_mode((self.size_X*self.size_factor_X, self.size_Y*self.size_factor_Y), 0, 32)
        pygame.display.set_caption("BattleTank - Papsdroid tuto")
        self.background = pygame.image.load(self.background_image_filename).convert()
        self.tank_tile = pygame.image.load(self.tank_image_filename).convert_alpha()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.destroy()

            for x in range(0, self.size_X*self.size_factor_X, self.size_X):
                for y in range(0, self.size_Y*self.size_factor_Y, self.size_Y):
                    self.screen.blit(self.background, (x, y))

            x, y = pygame.mouse.get_pos()
            x -= self.tank_tile.get_width() / 2
            y -= self.tank_tile.get_height() / 2
            self.screen.blit(self.tank_tile, (x, y))

            pygame.display.update()

    def destroy(self):

        print("Bye !")
        pygame.quit()
        exit()


if __name__ == "__main__":

    appl = Game()

    try:
        appl.loop()
    except KeyboardInterrupt:
        appl.destroy()
