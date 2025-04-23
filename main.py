# Pygame game template

import pygame
import sys
import config # Import the config module
import random
from pygame.locals import *

def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen
   
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    
    # Game variables
    CELL_SIZE = 10
    direction = 1 
    update_snake = 0
    score = 0 

    snake_pos = [[int(config.WINDOW_WIDTH / 2), int(config.WINDOW_HEIGHT / 2)]]
    snake_pos.append([int(config.WINDOW_WIDTH / 2), int(config.WINDOW_HEIGHT / 2) + CELL_SIZE])
    snake_pos.append([int(config.WINDOW_WIDTH / 2), int(config.WINDOW_HEIGHT / 2) + CELL_SIZE * 2])
    snake_pos.append([int(config.WINDOW_WIDTH / 2), int(config.WINDOW_HEIGHT / 2) + CELL_SIZE * 3])

    # Apple pos
    apple_pos = [random.randint(0, config.WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, config.WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

    # Font for score
    pygame.font.init()
    font = pygame.font.SysFont(None, 35)

    # Background Music
    # pygame.mixer.init()
    # pygame.mixer.music.load('')
    # pygame.mixer.music.set_volume(0.5)
    # pygame.mixer.music.play(-1)

    def draw_apple(screen):
        pygame.draw.rect(screen, config.RED, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

    def draw_score(screen):
        score_text = font.render(f'Score: {score}', True, config.BLACK)
        screen.blit(score_text, [10, 10])

    running = True
    while running:
        screen.fill(config.GREEN) 
        draw_apple(screen)
        draw_score(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_UP and direction != 3: # up
                    direction = 1
                elif event.key == pygame.K_RIGT and direction != 4: # right
                    direction = 2
                elif event.key == pygame.K_DOWN and direction != 1: # down
                    direction = 3
                elif event.key == pygame.K_LEFT and direction != 2: #left
                    direction = 4

            # Add timer
        if update_snake > 99:
            update_snake = 0

            # Move the snake
            head_x, head_y = snake_pos[0]
            
            if direction == 1: # up
                head_y -= CELL_SIZE
            elif direction == 2: # right
                head_x += CELL_SIZE
            elif direction == 3: # down
                head_y += CELL_SIZE
            elif direction == 4: #left
                head_x -= CELL_SIZE 
            
            snake_pos.insert(0, [head_x, head_y]) # add new head
            snake_pos.pop() # remove last segment

            # collison with apple
            if snake_pos[0] == apple_pos:
                apple_pos = [random.randint(0, config.WINDOW_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, config.WINDOW_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
                snake_pos.append(snake_pos[-1])
                score += 1
            
            if head_x < 0 or head_x >= config.WINDOW_WIDTH or head_y < 0 or head_y >= config.WINDOW_HEIGHT:
                running = False
        
            for i in range(len(snake_pos)):
                segment = snake_pos[i]
                if i == 0:
                    pygame.draw.rect(screen, (100, 100, 200), (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, config.RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                else: 
                    pygame.draw.rect(screen, (100, 100, 200), (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, (50, 175, 25), (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
                    
        pygame.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate
        update_snake += 1
        
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



