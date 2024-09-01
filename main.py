import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    clock = pygame.time.Clock()

    dt = 0
    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroid_field = AsteroidField()    

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for thing in updatable:
            thing.update(dt)
        pygame.Surface.fill(screen, (0,0,0))
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        #Framerate limiter
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()