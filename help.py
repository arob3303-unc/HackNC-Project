import pygame
pygame.init()

# Set up screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up your object (e.g., a rectangle)
object_width, object_height = 50, 50
object_x, object_y = screen_width // 2 - object_width // 2, screen_height // 2 - object_height // 2
object_speed = 5

# Initialize the camera position
camera_x, camera_y = 0, 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_x -= object_speed
    if keys[pygame.K_RIGHT]:
        object_x += object_speed
    if keys[pygame.K_UP]:
        object_y -= object_speed
    if keys[pygame.K_DOWN]:
        object_y += object_speed

    # Calculate the camera offset to keep the object centered on the screen
    screen_center_x, screen_center_y = screen_width // 2, screen_height // 2
    camera_x, camera_y = object_x - screen_center_x, object_y - screen_center_y
    
    # Clear the screen
    screen.fill((0, 0, 0))
    print(keys)
    # Draw the object on the screen
    pygame.draw.rect(screen, (255, 0, 0), (object_x - camera_x, object_y - camera_y, object_width, object_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()