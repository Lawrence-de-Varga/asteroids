import pygame
import constants as cn

pygame.init()
screen = pygame.display.set_mode((cn.SCREEN_WIDTH, cn.SCREEN_HEIGHT))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
