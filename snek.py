import pygame


class Snek:
    def __init__(self, color: tuple[int, int, int], step: int, width: int, height: int):
        self.size = 9  # segment takes up 90% of the tile (not really but yea)
        self.segments = [pygame.Rect(  # find field center
            width // 2,   # x
            height // 2,  # y
            step,         # w
            step          # h
        )] * 2
        self.color = color
        self.step = step
    
    def move(self, direction: int):
        segment = self.segments.pop()
        match direction:
            case 0: segment = self.segments[0].move(self.step, 0)  # move right
            case 1: segment = self.segments[0].move(-self.step, 0)  # move left
            case 2: segment = self.segments[0].move(0, -self.step)  # move up
            case 3: segment = self.segments[0].move(0, self.step)  # move down
        
        self.segments.insert(0, segment)  # add back to body
        
    def grow(self):
        self.segments.append(self.segments[-1].copy())
        
    def draw(self, screen: pygame.display):
        for segment in self.segments:
            pygame.draw.rect(screen, self.color, segment.scale_by(self.size/self.step, self.size/self.step))
            

class SnekSeg:
    def __init__(self, rect: pygame.Rect):
        self.rect = rect
