import pygame
import random
pygame.init()

class DrawInformation:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GRAY = (128, 128, 128)
    BACKGROUND_COLOR = WHITE

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Algorithm Visualizer")
        self.set_list(lst)
    def set_list(self, lst):
        pass
    
