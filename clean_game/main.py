import pygame
import random
import asyncio
import math
import os

# Configure pygbag environment
os.environ["PYGBAG_POOL_SIZE"] = "256MB"
os.environ["PYGBAG_DEBUG"] = "0"  # Reduce verbose logging

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 255
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    SMALL_FONT = pygame.font.SysFont('comicsans', 15)
    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 30)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    # Controls
    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start | A - Ascending | D - Descending",
        1, draw_info.BLACK
    )
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

    # Algorithms
    sorting = draw_info.FONT.render(
        "B - Bubble | I - Insertion | M - Merge | Q - Quick",
        1, draw_info.BLACK
    )
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 70))

    # Title
    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        1, draw_info.BLUE
    )
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    # Speed
    time = draw_info.SMALL_FONT.render(
        "SPEED: UP - Faster | DOWN - Slower",
        1, draw_info.BLACK
    )
    draw_info.window.blit(time, (draw_info.width / 2 - time.get_width() / 2, 95))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_PAD // 2,
            draw_info.TOP_PAD,
            draw_info.width - draw_info.SIDE_PAD,
            draw_info.height - draw_info.TOP_PAD
        )
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(
            draw_info.window,
            color,
            (x, y, draw_info.block_width, draw_info.height)
        )

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]


async def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if (lst[j] > lst[j + 1] and ascending) or (lst[j] < lst[j + 1] and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                if j % 5 == 0:  # Only draw every 5 steps for performance
                    draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                    await asyncio.sleep(0.03)
    return lst


async def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1

        while j >= 0 and ((lst[j] > current and ascending) or (lst[j] < current and not ascending)):
            lst[j + 1] = lst[j]
            if j % 3 == 0:  # Reduced drawing frequency
                draw_list(draw_info, {j: draw_info.RED, j + 1: draw_info.GREEN}, True)
                await asyncio.sleep(0.02)
            j -= 1

        lst[j + 1] = current
        draw_list(draw_info, {j + 1: draw_info.GREEN}, True)
        await asyncio.sleep(0.02)
    return lst


async def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst

    async def merge(start, mid, end):
        left = lst[start:mid + 1]
        right = lst[mid + 1:end + 1]
        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if (left[i] <= right[j] and ascending) or (left[i] >= right[j] and not ascending):
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1

            if k % 10 == 0:  # Reduced drawing frequency
                draw_list(draw_info, {k: draw_info.GREEN}, True)
                await asyncio.sleep(0.02)
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

        draw_list(draw_info, {}, True)
        await asyncio.sleep(0.05)

    async def merge_sort_rec(start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        await merge_sort_rec(start, mid)
        await merge_sort_rec(mid + 1, end)
        await merge(start, mid, end)

    await merge_sort_rec(0, len(lst) - 1)
    return lst


async def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst

    async def partition(low, high):
        pivot = lst[high]
        i = low - 1

        for j in range(low, high):
            if (lst[j] <= pivot and ascending) or (lst[j] >= pivot and not ascending):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

                if j % 5 == 0:  # Reduced drawing frequency
                    colors = {high: draw_info.RED, i: draw_info.GREEN, j: draw_info.BLUE}
                    draw_list(draw_info, colors, True)
                    await asyncio.sleep(0.03)

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        draw_list(draw_info, {i + 1: draw_info.GREEN}, True)
        await asyncio.sleep(0.03)
        return i + 1

    async def quick_sort_rec(low, high):
        if low < high:
            pi = await partition(low, high)
            await quick_sort_rec(low, pi - 1)
            await quick_sort_rec(pi + 1, high)

    await quick_sort_rec(0, len(lst) - 1)
    return lst


async def main():
    try:
        pygame.display.init()
        pygame.font.init()
    except:
        pass

    run = True
    clock = pygame.time.Clock()

    # Reduced size for web performance
    n = 100
    min_val, max_val = 0, 100
    speed = 60

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    sorting = False
    ascending = True
    sorting_algorithm = None
    sorting_algo_name = "Choose Algorithm"
    sorting_task = None

    while run:
        clock.tick(speed)

        if sorting and sorting_task and sorting_task.done():
            sorting = False
            speed = 60

        if not sorting:
            draw(draw_info, sorting_algo_name, ascending)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    if sorting and sorting_task:
                        sorting_task.cancel()
                    sorting = False
                    speed = 60

                elif event.key == pygame.K_SPACE and not sorting:
                    if sorting_algorithm:
                        sorting = True
                        sorting_task = asyncio.create_task(sorting_algorithm(draw_info, ascending))

                elif event.key == pygame.K_a and not sorting:
                    ascending = True

                elif event.key == pygame.K_d and not sorting:
                    ascending = False

                elif event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble Sort"

                elif event.key == pygame.K_i and not sorting:
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"

                elif event.key == pygame.K_m and not sorting:
                    sorting_algorithm = merge_sort
                    sorting_algo_name = "Merge Sort"

                elif event.key == pygame.K_q and not sorting:
                    sorting_algorithm = quick_sort
                    sorting_algo_name = "Quick Sort"

                elif event.key == pygame.K_UP:
                    speed = min(speed + 10, 120)

                elif event.key == pygame.K_DOWN:
                    speed = max(speed - 10, 10)

        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {e}")
        pygame.quit()