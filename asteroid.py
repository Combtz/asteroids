import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)

        child_velocity1 = self.velocity.rotate(random_angle) * 1.2

        child_velocity2 = self.velocity.rotate(-random_angle) * 1.2

        child_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        child_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        child_asteroid1.velocity = child_velocity1
        child_asteroid2.velocity = child_velocity2