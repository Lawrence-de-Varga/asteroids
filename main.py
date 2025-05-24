import pygame
import constants as cn
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((cn.SCREEN_WIDTH, cn.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(cn.SCREEN_WIDTH / 2, cn.SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)
        
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
