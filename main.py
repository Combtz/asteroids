import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    clock = pygame.time.Clock()

    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        pygame.display.flip()
        
        #Framerate limiter
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()