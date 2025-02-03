import pygame

pygame.init()

window = pygame.display.set_mode((1440, 900))
pygame.display.set_caption("Coordinate Finder")
font = pygame.font.Font(None, 36)

platform_width = 100
platform_height = 10

def save_points_to_file(points, base_name="point"):
    index = 1
    while True:
        filename = f"{base_name}{index}.txt"
        try:
            with open(filename, "x") as f:
                for point in points:
                    f.write(f"{point[0]},{point[1]}\n")
            break
        except FileExistsError:
            index += 1

def load_points_from_file():
    print("Enter the filename:")
    filename = input()
    try:
        with open(filename, "r") as f:
            points = [(int(x), int(y)) for x, y in [line.split(",") for line in f.readlines()]]
        print("Points loaded.")
        return points
    except FileNotFoundError:
        print("File not found.")
        return None

print("Would you like to load a file? (y/n)")
load_file = input().lower() == "y"

points = []
if load_file:
    points = load_points_from_file()
    if points is not None:
        window.fill((255, 255, 255))
        for i, point in enumerate(points, start=1):
            pygame.draw.rect(window, (0, 0, 0), (x, y, platform_width, platform_height)),
            text = font.render(str(i), True, (0, 0, 0))
            window.blit(text, (point[0] + 10, point[1] - 10))
        pygame.display.flip()
else:
    label = 1
    window.fill((255, 255, 255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                pygame.draw.rect(window, (0, 0, 0), (x, y, platform_width, platform_height)),
                text = font.render(str(label), True, (0, 0, 0))
                window.blit(text, (x + 10, y - 10))
                points.append((x, y))
                print(f"pygame.Rect({x}, {y}, platform_width, platform_height)")
                label += 1
        pygame.display.flip()

    save_points_to_file(points)

pygame.quit()


