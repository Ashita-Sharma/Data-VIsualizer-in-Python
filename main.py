import pygame
import random
pygame.init()

class DrawInformation:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BACKGROUND_COLOR = WHITE
    GRADIENTS = [ (128,128,128), (160,160,160), (192,192,192)]
    TOP_PAD = 150
    SIDE_PAD = 100

    FONT = pygame.font.SysFont('comicsans',20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)


    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Algorithm Visualizer")
        self.set_list(lst)
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD)/len(lst))
        self.block_height = (self.height - self.TOP_PAD)//(self.max_val - self.min_val)
        self.start_x = self.SIDE_PAD // 2
def generate_starting_list(n, min_val, max_val):
    lst = []
    for i in range(n):
        lst.append(random.randint(min_val, max_val))
    return lst

def draw(draw_info,algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    title = draw_info.FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLACK)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))
    controls = draw_info.FONT.render("R - Reset | A - Ascending | D - Descending | Space - Start",1,draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 35))
    sorts = draw_info.FONT.render("B - Bubble Sort | I - Insertion Sort | S - Selection Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorts, (draw_info.width / 2 - sorts.get_width() / 2, 65))
    sorts2 = draw_info.FONT.render("Q - Quick Sort | H - Heap Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorts2, (draw_info.width / 2 - sorts2.get_width() / 2, 95))
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg = False):

    lst = draw_info.lst
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    for i, val in enumerate(lst):
        x = draw_info.start_x + (draw_info.block_width * i)
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3 ]
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
    if clear_bg:
        pygame.display.update()


def bubble_sort (draw_info, ascending = True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j:draw_info.GREEN, j+1:draw_info.RED}, True)
                yield True
    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        extreme_idx = i
        for j in range(i + 1, len(lst)):
            draw_list(draw_info, {extreme_idx: draw_info.GREEN, j: draw_info.RED}, True)
            yield True

            if (ascending and lst[j] < lst[extreme_idx]) or (not ascending and lst[j] > lst[extreme_idx]):
                extreme_idx = j
        lst[i], lst[extreme_idx] = lst[extreme_idx], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, extreme_idx: draw_info.RED}, True)
        yield True

    return lst


def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    def heapify(n, root_idx):
        largest = root_idx
        left = 2 * root_idx + 1
        right = 2 * root_idx + 2
        if left < n:
            if (ascending and lst[left] > lst[largest]) or (not ascending and lst[left] < lst[largest]):
                largest = left

        if right < n:
            if (ascending and lst[right] > lst[largest]) or (not ascending and lst[right] < lst[largest]):
                largest = right
        if largest != root_idx:
            lst[root_idx], lst[largest] = lst[largest], lst[root_idx]
            draw_list(draw_info, {root_idx: draw_info.GREEN, largest: draw_info.RED}, True)
            yield True
            yield from heapify(n, largest)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)

    for i in range(n - 1, 0, -1):

        lst[0], lst[i] = lst[i], lst[0]
        draw_list(draw_info, {0: draw_info.GREEN, i: draw_info.RED}, True)
        yield True
        yield from heapify(i, 0)
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1

        while j >= 0:
            ascending_sort = lst[j] > current and ascending
            descending_sort = lst[j] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[j + 1] = lst[j]
            j -= 1  # Move backwards
            draw_list(draw_info, {j + 1: draw_info.GREEN, j + 2: draw_info.RED}, True)
            yield True

        lst[j + 1] = current
    return lst


def quick_sort(draw_info, ascending=True, start=0, end=None):
    lst = draw_info.lst

    if end is None:
        end = len(lst) - 1

    if start < end:
        pivot_idx = yield from partition(draw_info, start, end, ascending)

        yield from quick_sort(draw_info, ascending, start, pivot_idx - 1)
        yield from quick_sort(draw_info, ascending, pivot_idx + 1, end)

    return lst


def partition(draw_info, start, end, ascending):
    lst = draw_info.lst

    pivot = lst[end]
    pivot_idx = start

    for j in range(start, end):
        draw_list(draw_info, {j: draw_info.RED, end: draw_info.GREEN, pivot_idx: draw_info.BLACK}, True)
        yield True

        should_swap = (ascending and lst[j] < pivot) or (not ascending and lst[j] > pivot)

        if should_swap:
            lst[pivot_idx], lst[j] = lst[j], lst[pivot_idx]
            draw_list(draw_info, {pivot_idx: draw_info.GREEN, j: draw_info.RED}, True)
            pivot_idx += 1
            yield True

    lst[pivot_idx], lst[end] = lst[end], lst[pivot_idx]
    draw_list(draw_info, {pivot_idx: draw_info.GREEN, end: draw_info.RED}, True)
    yield True

    return pivot_idx

def main():
    run = True
    n = 50
    min_val = 1
    max_val = 100
    sorting = False
    ascending = True
    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800,600, lst)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info,sorting_algo_name, ascending)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_RETURN and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False #fixed this!
                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble Sort"
                    sorting_algorithm_generator = None
                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"
                    sorting_algorithm_generator = None
                elif event.key == pygame.K_s and not sorting:
                    sorting_algorithm = selection_sort
                    sorting_algo_name = "Selection Sort"
                    sorting_algorithm_generator = None
                elif event.key == pygame.K_h and not sorting:
                    sorting_algorithm = heap_sort
                    sorting_algo_name = "Heap Sort"
                    sorting_algorithm_generator = None
                elif event.key == pygame.K_q and not sorting:
                    sorting_algorithm = quick_sort
                    sorting_algo_name = "Quick Sort"
                    sorting_algorithm_generator = None

    pygame.quit()

if __name__ == "__main__":
    main()
