import pygame
from bullet import Shot
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS 
from constants import PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta

    def update(self, delta):
        if self.shot_timer < 0:
            self.shot_timer = 0
        else:
            self.shot_timer -= delta
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta)

        if keys[pygame.K_d]:
            self.rotate(delta)

        if keys[pygame.K_w]:
            self.move(delta)

        if keys[pygame.K_s]:
            self.move(-delta)

        if keys[pygame.K_SPACE] and not self.shot_timer > 0:
            self.shot_timer += PLAYER_SHOT_COOLDOWN
            self.shoot()


    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        bullet.velocity *= PLAYER_SHOT_SPEED
