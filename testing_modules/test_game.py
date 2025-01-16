import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Parkour Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
FPS = 60

player_size = 40
player_color = BLUE
player_x, player_y = 100, SCREEN_HEIGHT - player_size - 60
player_speed = 5
player_jump = 12
player_velocity_y = 0
gravity = 0.5
is_jumping = False

platforms = [
    pygame.Rect(50, SCREEN_HEIGHT - 20, SCREEN_WIDTH - 100, 20),
    pygame.Rect(100, 600, 100, 10),
    pygame.Rect(400, 500, 100, 10),
    pygame.Rect(600, 400, 100, 10),
    pygame.Rect(900, 300, 100, 10),
]
traps = [
    pygame.Rect(200, SCREEN_HEIGHT - 60, 50, 10),
    pygame.Rect(500, 450, 50, 10),
    pygame.Rect(800, 350, 50, 10)
]

for trap in traps:
    if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(trap):
        print("You hit a trap! Game over.")
        running = False

for platform in platforms:
    pygame.draw.rect(screen, BLACK, platform)

for trap in traps:
    pygame.draw.rect(screen, RED, trap)



goal = pygame.Rect(1100, 250, 50, 50)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP] and not is_jumping:
        player_velocity_y = -player_jump
        is_jumping = True

    player_velocity_y += gravity
    player_y += player_velocity_y

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_y = platform.top - player_size
            player_velocity_y = 0
            is_jumping = False

    if player_rect.colliderect(goal):
        print("You win!")
        running = False

    if player_y > SCREEN_HEIGHT:
        print("Game Over!")
        running = False

    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

    pygame.draw.rect(screen, GREEN, goal)

    pygame.draw.rect(screen, player_color, player_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
