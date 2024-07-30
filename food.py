import random
import pygame


class Food:
    def __init__(self, x: int, y: int, step: int, color: tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, step, step)
        self.color = color
        
    @staticmethod
    def random(width: int, height: int, step: int, color: tuple[int, int, int]):
        return Food(
            (random.randint(0, width - step) // step) * step,
            (random.randint(0, height - step) // step) * step,
            step,
            color
        )
    
    def draw(self, screen: pygame.display):
        pygame.draw.rect(screen, self.color, self.rect)
    