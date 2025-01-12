#!/usr/bin/env python3

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    # ========== INIT ==========
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    aster_field = AsteroidField()

    clock = pygame.time.Clock()
    dt  = 0
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return

        # ============== Input/update ==================
        for obj in updatable:
            obj.update(dt)

        # =================== Render ============
        screen.fill(0)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    
    
if __name__ == "__main__":
    main()