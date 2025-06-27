import pygame
import datetime
import math
import os

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock center
center = (WIDTH//2, HEIGHT//2)

# Load images (replace with your actual image paths)
try:
    # Try to load images
    mickey_face = pygame.image.load("mickey_face.png").convert_alpha()
    mickey_face = pygame.transform.scale(mickey_face, (WIDTH, HEIGHT))
    
    # Seconds hand (left hand - should point right in the image)
    left_hand = pygame.image.load("left_hand.png").convert_alpha()
    left_hand = pygame.transform.scale(left_hand, (250, 50))  # Adjust size as needed
    
    # Minutes hand (right hand - should point right in the image)
    right_hand = pygame.image.load("right_hand.png").convert_alpha()
    right_hand = pygame.transform.scale(right_hand, (200, 50))  # Adjust size as needed
    
except FileNotFoundError:
    # Fallback if images not found - we'll draw simple shapes instead
    print("Image files not found! Using fallback graphics.")
    
    # Create Mickey face
    mickey_face = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.circle(mickey_face, (200, 200, 200), center, 250)  # Face
    pygame.draw.circle(mickey_face, (200, 200, 200), (center[0]-150, center[1]-150), 80)  # Left ear
    pygame.draw.circle(mickey_face, (200, 200, 200), (center[0]+150, center[1]-150), 80)  # Right ear
    
    # Create hands
    left_hand = pygame.Surface((250, 20), pygame.SRCALPHA)
    pygame.draw.rect(left_hand, RED, (0, 0, 250, 10))  # Red seconds hand
    
    right_hand = pygame.Surface((200, 20), pygame.SRCALPHA)
    pygame.draw.rect(right_hand, BLACK, (0, 0, 200, 15))  # Black minutes hand

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get current time
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute + seconds/60  # Makes minutes hand move smoothly
    
    # Calculate angles (0° at top, clockwise)
    second_angle = -math.radians(seconds * 6) + math.pi/2
    minute_angle = -math.radians(minutes * 6) + math.pi/2
    
    # Rotate hands
    rotated_left = pygame.transform.rotate(left_hand, math.degrees(second_angle))
    rotated_right = pygame.transform.rotate(right_hand, math.degrees(minute_angle))
    
    # Get rects for positioning (account for rotation)
    left_rect = rotated_left.get_rect(center=center)
    right_rect = rotated_right.get_rect(center=center)
    
    # Draw everything
    screen.fill(WHITE)
    screen.blit(mickey_face, (0, 0))
    screen.blit(rotated_left, left_rect)
    screen.blit(rotated_right, right_rect)
    
    # Draw clock center
    pygame.draw.circle(screen, BLACK, center, 10)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
