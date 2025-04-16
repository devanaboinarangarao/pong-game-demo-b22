import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Define ball properties
ball_pos = [width//2, height//2]
ball_radius = 15
ball_speed = [3, 3]

# Define paddle properties
paddle_width, paddle_height = 10, 100
paddle_speed = 5
left_paddle_pos = [50, height//2 - paddle_height//2]
right_paddle_pos = [width - 50 - paddle_width, height//2 - paddle_height//2]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= paddle_speed
    if keys[pygame.K_s] and left_paddle_pos[1] < height - paddle_height:
        left_paddle_pos[1] += paddle_speed
    if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
        right_paddle_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_pos[1] < height - paddle_height:
        right_paddle_pos[1] += paddle_speed

    # Move ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with top and bottom
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if (ball_pos[0] - ball_radius < left_paddle_pos[0] + paddle_width and
        left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + paddle_height) or
       (ball_pos[0] + ball_radius > right_paddle_pos[0] and
        right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]

    # Ball out of bounds
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_pos = [width//2, height//2]

    # Fill background
    window.fill(black)

    # Draw paddles
    pygame.draw.rect(window, white, (left_paddle_pos[0], left_paddle_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(window, white, (right_paddle_pos[0], right_paddle_pos[1], paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(window, white, ball_pos, ball_radius)

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()