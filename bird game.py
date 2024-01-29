import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1250, 600
FPS = 30
GRAVITY = 0
BIRD_SPEED = 5
JUMP_HEIGHT = 10
BOX_SIZE = 30
SCORE_FONT_SIZE = 36
highest_score=0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game states
RUNNING = "running"
GAME_OVER = "game_over"

# Initialize Pygame mixer
pygame.mixer.init()
start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks() - start_time

# Load sound effects
jump_sound = pygame.mixer.Sound(r"point-101soundboards.mp3")
score_sound = pygame.mixer.Sound(r"die-101soundboards.mp3")
collision_sound = pygame.mixer.Sound(r"flappy-bird-hit-sound-101soundboards.mp3")
background_image = pygame.image.load(r"C:\Users\Akshay\OneDrive\Desktop\python\R (1).jpeg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Box class
class Box(pygame.sprite.Sprite):
    def __init__(self, color, position):
        super().__init__()
        self.image = pygame.Surface((BOX_SIZE, BOX_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird with Boxes")
clock = pygame.time.Clock()

# Create sprites
all_sprites = pygame.sprite.Group()
boxes = pygame.sprite.Group()
bird = Box(WHITE, (100, HEIGHT // 2))
all_sprites.add(bird)

# Game variables
score = 0
score_displayed = False
game_state = RUNNING

# Font setup
font = pygame.font.Font(None, SCORE_FONT_SIZE)

def reset_game():
    all_sprites.empty()
    boxes.empty()
    bird.rect.topleft = (100, HEIGHT // 2)
    all_sprites.add(bird)
    return 0

# Game loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION and game_state == RUNNING:
            bird.rect.y = event.pos[1]
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_state == GAME_OVER:
            game_state = RUNNING
            score = reset_game()
            score_displayed = False
            jump_sound.play()

    if game_state == RUNNING and current_time%9==0 :
        # Spawn green boxes (points) and red boxes (game over)
        if random.randint(0,1):  # 50% chance for a green box
            green_box = Box(GREEN, (WIDTH, random.randint(50, HEIGHT - 200)))
            all_sprites.add(green_box)
            boxes.add(green_box)
        else:  # 50% chance for a red box
            red_box = Box(RED, (WIDTH, random.randint(50, HEIGHT - 200)))
            all_sprites.add(red_box)
            boxes.add(red_box)

    if game_state == RUNNING:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and bird.rect.y > 0:
            bird.rect.y -= JUMP_HEIGHT
        elif keys[pygame.K_DOWN] and bird.rect.y < HEIGHT - BOX_SIZE:
            bird.rect.y += JUMP_HEIGHT

        all_sprites.update()

        # Update box positions and maintain a gap of 5 pixels between them
        for box in boxes:
            box.rect.x -= BIRD_SPEED  # Adjust this value based on your game's speed

        # Check for collisions with boxes
        hits = pygame.sprite.spritecollide(bird, boxes, True)
        for hit in hits:
            if hit.image.get_at((0, 0)) == GREEN:
                score += 1
                score_sound.play()  # Play score sound
            elif hit.image.get_at((0, 0)) == RED:
                game_state = GAME_OVER
                score_displayed = True
                collision_sound.play()  # Play collision sound

        # Check if bird touches the ground
        if bird.rect.bottom >= HEIGHT:
            game_state = GAME_OVER
            score_displayed = True
            collision_sound.play()  # Play collision sound

        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        current_time = pygame.time.get_ticks() - start_time
        seconds = (current_time // 1000) % 60  # Get the remaining seconds after minutes
        minutes = current_time // (1000 * 60)
        
        timer_text = font.render(f"Time: {minutes:02}:{seconds:02}", True, WHITE)
        screen.blit(timer_text, (WIDTH - 200, 10))

        # Display the highest score on the screen

        highscore_text = font.render(f"Highest Score: {highest_score}", True, WHITE)
        screen.blit(highscore_text, (WIDTH/2 - 150 ,10))

        # Update the highest score
        if score > highest_score:
            highest_score = score
            # Save the new highest score and total time
        
    elif game_state == GAME_OVER:
        game_over_text = font.render("Game Over", True, WHITE)
        replay_text = font.render("Press SPACE to replay", True, WHITE)

        screen.fill(BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - 40, HEIGHT // 2))
        screen.blit(replay_text, (WIDTH // 2 - 110, HEIGHT // 2 + 50))

    pygame.display.flip()
    clock.tick(FPS)
