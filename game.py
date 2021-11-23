import pygame
import pytmx
import pyscroll


class Game:
    def __init__(self):
        # create the window of the game
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Pygamon adventure')

        # load the map (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)


    def run(self):
        # loop of the game
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
