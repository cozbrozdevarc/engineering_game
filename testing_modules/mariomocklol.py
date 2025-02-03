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

player_size = 20
player_color = BLUE
player_x, player_y = 79, SCREEN_HEIGHT - player_size - 100
player_speed = 4
player_jump = 6
player_velocity_y = 0
gravity = 0.2
is_jumping = False

floor_height = 100  
floor_y = SCREEN_HEIGHT - floor_height

goal_x, goal_y = 1101, 301  
goal = pygame.Rect(goal_x, goal_y, 50, 50)  

platform_width = 100
platform_height = 10

platforms = [
    pygame.Rect(378, 645, platform_width, platform_height),
    pygame.Rect(599, 587, platform_width, platform_height),
    pygame.Rect(287, 759, platform_width, platform_height),
    pygame.Rect(994, 595, platform_width, platform_height),
    pygame.Rect(907, 515, platform_width, platform_height),
    pygame.Rect(1054, 436, platform_width, platform_height),
    pygame.Rect(959, 370, platform_width, platform_height),
    pygame.Rect(1101, 301, platform_width, platform_height),
    pygame.Rect(1338, 299, platform_width, platform_height)
]

start_time = pygame.time.get_ticks()
running = True

camera_offset_x = 0

font = pygame.font.Font(None, 36)

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    
    
    player_velocity_y += gravity
    next_y = player_y + player_velocity_y
    
    
    next_player_rect = pygame.Rect(player_x, next_y, player_size, player_size)
    
    
    collision_detected = False
    for platform in platforms:
        if next_player_rect.colliderect(platform):
            
            if player_velocity_y > 0:
                player_y = platform.y - player_size
                player_velocity_y = 0
                is_jumping = False
                collision_detected = True
                break
    
    
    if not collision_detected:
        player_y = next_y

    
    if player_y + player_size >= floor_y:
        player_y = floor_y - player_size
        player_velocity_y = 0
        is_jumping = False

    
    if keys[pygame.K_UP] and not is_jumping:
        player_velocity_y = -player_jump
        is_jumping = True

    
    camera_offset_x = player_x - SCREEN_WIDTH // 2

    
    floor_rect = pygame.Rect(-camera_offset_x, floor_y, 5000, floor_height)  
    pygame.draw.rect(screen, WHITE, floor_rect)

    
    goal_rect = pygame.Rect(goal_x - camera_offset_x, goal_y, goal.width, goal.height)
    pygame.draw.rect(screen, GREEN, goal_rect)

    
    player_screen_x = SCREEN_WIDTH // 2
    player_rect = pygame.Rect(player_screen_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, player_color, player_rect)

    
    for platform in platforms:
        platform_rect = pygame.Rect(
            platform.x - camera_offset_x, platform.y, platform.width, platform_height
        )
        pygame.draw.rect(screen, WHITE, platform_rect)

    
    player_world_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    if player_world_rect.colliderect(goal):
        end_time = pygame.time.get_ticks()
        time_diff = end_time - start_time
        milliseconds = time_diff % 1000
        seconds = (time_diff // 1000) % 60
        minutes = time_diff // 60000
        print(f"Your time: {minutes}:{seconds:02d}.{milliseconds:03d}")
        running = False

    
    if player_y > SCREEN_HEIGHT:
        print("Game Over!")
        running = False

    
    current_time = pygame.time.get_ticks()
    time_diff = current_time - start_time
    milliseconds = time_diff % 1000
    seconds = (time_diff // 1000) % 60
    minutes = time_diff // 60000
    time_str = f"{minutes}:{seconds:02d}.{milliseconds:03d}"
    text = font.render(time_str, True, WHITE)
    screen.blit(text, (SCREEN_WIDTH - 150, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()