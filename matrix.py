import pygame
import random
import sys

pygame.init()

# -----------------------------
# DISPLAY
# -----------------------------
screen = pygame.display.set_mode(
    (0, 0),
    pygame.FULLSCREEN
)

pygame.display.set_caption("Matrix Rain")

WIDTH, HEIGHT = screen.get_size()

# -----------------------------
# COLORS
# -----------------------------
BLACK = (0, 0, 0)
GREEN = (0, 150, 45)
BRIGHT_GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# -----------------------------
# FONT
# -----------------------------
FONT_SIZE = 25
font = pygame.font.SysFont("Menlo", FONT_SIZE)

# -----------------------------
# MATRIX SETTINGS
# -----------------------------
CHARACTERS = "01"

COLUMN_WIDTH = FONT_SIZE
ROW_HEIGHT = FONT_SIZE

columns = WIDTH // COLUMN_WIDTH

drops = []
speeds = []
lengths = []
characters = []

for _ in range(columns):

    drops.append(random.randint(-75, 0))

    # Slower falling speed
    speeds.append(random.uniform(3, 7.5))

    length = random.randint(8, 28)
    lengths.append(length)

    # Remember each character
    characters.append([
        random.choice(CHARACTERS)
        for _ in range(length)
    ])

# -----------------------------
# CLOCK
# -----------------------------
clock = pygame.time.Clock()

running = True

while running:

    # -------------------------
    # EVENTS
    # -------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

    # -------------------------
    # BACKGROUND
    # -------------------------
    screen.fill(BLACK)

    # -------------------------
    # MATRIX RAIN
    # -------------------------
    for column in range(columns):

        x = column * COLUMN_WIDTH
        head_y = int(drops[column] * ROW_HEIGHT)

        for trail in range(lengths[column]):

            y = head_y - trail * ROW_HEIGHT

            if y < -ROW_HEIGHT or y > HEIGHT:
                continue

            # Slow 0/1 switching
            if random.random() < 0.15:
                characters[column][trail] = random.choice(CHARACTERS)

            character = characters[column][trail]

            # Very rare white characters
            if random.random() < 0.010:
                color = WHITE

            # Bright head
            elif trail == 0:
                color = BRIGHT_GREEN

            # Dark green trail
            else:
                color = GREEN

            text = font.render(
                character,
                True,
                color
            )

            screen.blit(
                text,
                (x, y)
            )

        # -------------------------
        # MOVE RAIN
        # -------------------------
        drops[column] += speeds[column] / 10

        # -------------------------
        # RESET DROP
        # -------------------------
        if head_y > HEIGHT + 500:

            drops[column] = random.randint(-75, -1)

            speeds[column] = random.uniform(3, 7.5)

            length = random.randint(8, 28)
            lengths[column] = length

            characters[column] = [
                random.choice(CHARACTERS)
                for _ in range(length)
            ]

    # -------------------------
    # UPDATE SCREEN
    # -------------------------
    pygame.display.flip()

    clock.tick(30)

# -----------------------------
# CLEAN EXIT
# -----------------------------
pygame.quit()
sys.exit()
