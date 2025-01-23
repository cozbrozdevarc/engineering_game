import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1440, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Parkour Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
FPS = 60

# Player attributes
player_size = 20
player_color = BLUE
player_x, player_y = 79, 800
player_speed = 4
player_jump = 8
player_velocity_y = 0
gravity = 0.4
is_jumping = False

# Camera offset (start at 0)
camera_offset_x = 0

# Platform attributes
platform_width = 100
platform_height = 10

platforms = [
    pygame.Rect(79, 820, platform_width, platform_height),
    pygame.Rect(185, 747, platform_width, platform_height),
    pygame.Rect(322, 667, platform_width, platform_height),
    pygame.Rect(174, 609, platform_width, platform_height),
    pygame.Rect(332, 549, platform_width, platform_height),
    pygame.Rect(510, 532, platform_width, platform_height),
    pygame.Rect(663, 455, platform_width, platform_height),
    pygame.Rect(734, 572, platform_width, platform_height),
    pygame.Rect(893, 473, platform_width, platform_height),
    pygame.Rect(1002, 375, platform_width, platform_height),
    pygame.Rect(1186, 346, platform_width, platform_height),
    pygame.Rect(1088, 546, platform_width, platform_height),
    pygame.Rect(972, 531, platform_width, platform_height),
    pygame.Rect(794, 369, platform_width, platform_height),
    pygame.Rect(715, 307, platform_width, platform_height),
    pygame.Rect(625, 237, platform_width, platform_height),
    pygame.Rect(783, 172, platform_width, platform_height),
    pygame.Rect(906, 129, platform_width, platform_height),
    pygame.Rect(1061, 86, platform_width, platform_height),
]

traps = []

start_time = pygame.time.get_ticks()

goal = pygame.Rect(1200, 50, 50, 50)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP] and not is_jumping:
        player_velocity_y = -player_jump
        is_jumping = True

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Collision with platforms
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_y = platform.top - player_size
            player_velocity_y = 0
            is_jumping = False

    # Check for goal collision
    if player_rect.colliderect(goal):
        end_time = pygame.time.get_ticks()
        time_diff = end_time - start_time
        milliseconds = time_diff % 1000
        seconds = (time_diff // 1000) % 60
        minutes = time_diff // 60000
        print(f"Your time: {minutes}:{seconds:02d}.{milliseconds:03d}")
        running = False

    # Check for traps
    for trap in traps:
        if player_rect.colliderect(trap):
            print("You hit a trap! Game over.")
            running = False

    # Check if player falls off the screen
    if player_y > SCREEN_HEIGHT:
        print("Game Over!")
        running = False

    # Update camera offset based on player position
    # Center the player horizontally on the screen
    camera_offset_x = player_x - SCREEN_WIDTH // 2

    # Draw platforms
    for platform in platforms:
        platform_rect = pygame.Rect(
            platform.x - camera_offset_x, platform.y, platform.width, platform.height
        )
        pygame.draw.rect(screen, WHITE, platform_rect)

    # Draw traps
    for trap in traps:
        trap_rect = pygame.Rect(
            trap.x - camera_offset_x, trap.y, trap.width, trap.height
        )
        pygame.draw.rect(screen, RED, trap_rect)

    # Draw goal
    goal_rect = pygame.Rect(goal.x - camera_offset_x, goal.y, goal.width, goal.height)
    pygame.draw.rect(screen, GREEN, goal_rect)

    # Draw player
    player_screen_rect = pygame.Rect(
        SCREEN_WIDTH // 2, player_y, player_size, player_size
    )
    pygame.draw.rect(screen, player_color, player_screen_rect)

    # Display timer
    current_time = pygame.time.get_ticks()
    time_diff = current_time - start_time
    milliseconds = time_diff % 1000
    seconds = (time_diff // 1000) % 60
    minutes = time_diff // 60000
    time_str = f"{minutes}:{seconds:02d}.{milliseconds:03d}"
    font = pygame.font.Font(None, 36)
    text = font.render(time_str, True, WHITE)
    screen.blit(text, (SCREEN_WIDTH - 150, 20))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
