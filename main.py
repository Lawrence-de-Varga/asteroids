import pygame
import constants as cn
from player import Player

pygame.init()
screen = pygame.display.set_mode((cn.SCREEN_WIDTH, cn.SCREEN_HEIGHT))

# Clock
clock = pygame.time.Clock()


def main():
    player = Player(cn.SCREEN_WIDTH / 2, cn.SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
