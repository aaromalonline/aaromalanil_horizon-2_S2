import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #initialize screen
pygame.display.set_caption("Pygame Circle Drawer")


circles = []
path_length = 0.0
running = True
click_start_time = None


def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def draw_path():
    global path_length
    path_length = 0.0
    if len(circles) > 1:
        for i in range(1, len(circles)):
            pygame.draw.line(screen, BLACK, circles[i - 1]["pos"], circles[i]["pos"], 2)
            path_length += calculate_distance(circles[i - 1]["pos"], circles[i]["pos"])

def save_drawing():
    pygame.image.save(screen, "drawing.png")

# Main event loop
while running:
    screen.fill(WHITE)

    # Draw circles
    for circle in circles:
        pygame.draw.circle(screen, circle["color"], circle["pos"], circle["radius"])

    # Draw path
    draw_path()

    # Display path length
    font = pygame.font.Font(None, 36)
    text = font.render(f"Path Length: {path_length:.2f}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                click_start_time = time.time()
            elif event.button == 3:  # Right click
                if circles:
                    circles.pop()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and click_start_time is not None:  # Left click release
                click_duration = time.time() - click_start_time
                radius = max(5, int(click_duration * 50))
                pos = event.pos
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                circles.append({"pos": pos, "radius": radius, "color": color})
                click_start_time = None

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Clear canvas
                circles.clear()
            elif event.key == pygame.K_s:  # Save drawing
                save_drawing()

pygame.quit()