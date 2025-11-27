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

    TOP_PAD = 150
    SIDE_PAD = 100
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Algorithm Visualizer")
        self.set_list(lst)
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(list)
        self.max_val = max(list)

        self.block_width = round((self.width - self.SIDE_PAD)/len(lst))
        self.block_height = round((self.height - self.TOP_PAD)/(self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
def generate_starting_list(n, min_val, max_val):
    lst = []
    for i in range(n):
        lst.append(random.randint(min_val, max_val))
    return lst

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)