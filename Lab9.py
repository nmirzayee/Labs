import pygame
import random
import sys

def play_racer():
    # Initialize Pygame
    pygame.init()
    win_w, win_h = 400, 600
    win = pygame.display.set_mode((win_w, win_h))
    pygame.display.set_caption("Racer Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (200, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)

    # Player Car
    car = pygame.Rect(175, 500, 50, 70)
    car_speed = 5

    # Enemy Car
    enemy = pygame.Rect(random.randint(0, win_w - 50), 0, 50, 70)
    enemy_speed = 5

    # Coins
    coins = []
    coin_spawn_delay = 30
    coin_timer = 0
    coin_values = [1, 2, 3]
    score = 0

    running = True
    while running:
        win.fill(BLACK)

        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car.left > 0:
            car.x -= car_speed
        if keys[pygame.K_RIGHT] and car.right < win_w:
            car.x += car_speed

        # Move enemy
        enemy.y += enemy_speed
        if enemy.top > win_h:
            enemy.y = 0
            enemy.x = random.randint(0, win_w - enemy.width)

        # Coin spawning
        coin_timer += 1
        if coin_timer >= coin_spawn_delay:
            coin_timer = 0
            cx = random.randint(0, win_w - 20)
            cy = 0
            val = random.choice(coin_values)
            coin_rect = pygame.Rect(cx, cy, 20, 20)
            coins.append({"rect": coin_rect, "val": val})

        # Draw enemy and player
        pygame.draw.rect(win, GREEN, car)
        pygame.draw.rect(win, RED, enemy)

        # Move and draw coins
        for coin in coins[:]:
            coin["rect"].y += 4
            pygame.draw.circle(win, YELLOW, coin["rect"].center, 10)
            if car.colliderect(coin["rect"]):
                score += coin["val"]
                coins.remove(coin)
            elif coin["rect"].top > win_h:
                coins.remove(coin)

        # Collision with enemy
        if car.colliderect(enemy):
            game_over_text = font.render("Game Over!", True, WHITE)
            win.blit(game_over_text, (130, 280))
            pygame.display.update()
            pygame.time.delay(2000)
            running = False
            continue

        # Show score
        score_text = font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

# Run the game
if __name__ == "__main__":
    play_racer()

#second

import pygame
import random
import sys

def play_snake():
    pygame.init()
    grid_w, grid_h = 600, 600
    cell = 20
    snake_win = pygame.display.set_mode((grid_w, grid_h))
    pygame.display.set_caption("Snake Game")
    snake_clock = pygame.time.Clock()
    snake_font = pygame.font.SysFont("Arial", 20)

    color_bg = (0, 0, 0)
    color_snake = (0, 255, 0)
    color_food = (255, 255, 0)
    color_text = (255, 255, 255)

    snake_body = [(100, 100)]
    move_dir = (cell, 0)
    food_list = []
    food_vals = [1, 2, 3]
    food_life = 50
    snake_score = 0

    def add_food():
        while True:
            fx = random.randint(0, (grid_w - cell) // cell) * cell
            fy = random.randint(0, (grid_h - cell) // cell) * cell
            fval = random.choice(food_vals)
            food_pos = (fx, fy)
            if food_pos not in snake_body:
                food_list.append({"pos": food_pos, "val": fval, "life": food_life})
                break

    add_food()

    playing = True
    while playing:
        snake_win.fill(color_bg)
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and move_dir != (0, cell):
            move_dir = (0, -cell)
        if keys[pygame.K_DOWN] and move_dir != (0, -cell):
            move_dir = (0, cell)
        if keys[pygame.K_LEFT] and move_dir != (cell, 0):
            move_dir = (-cell, 0)
        if keys[pygame.K_RIGHT] and move_dir != (-cell, 0):
            move_dir = (cell, 0)

        # Move snake
        hx, hy = snake_body[0]
        new_head = (hx + move_dir[0], hy + move_dir[1])
        snake_body.insert(0, new_head)

        # Check wall or self collision
        if not (0 <= new_head[0] < grid_w and 0 <= new_head[1] < grid_h):
            playing = False
            break
        if new_head in snake_body[1:]:
            playing = False
            break

        # Eat food if on same position
        ate = False
        for food in food_list[:]:
            if new_head == food["pos"]:
                snake_score += food["val"]
                food_list.remove(food)
                add_food()
                ate = True
                break

        if not ate:
            snake_body.pop()

        # Update and draw food
        for food in food_list[:]:
            pygame.draw.rect(snake_win, color_food, (*food["pos"], cell, cell))
            food["life"] -= 1
            if food["life"] <= 0:
                food_list.remove(food)
                add_food()

        # Draw snake
        for part in snake_body:
            pygame.draw.rect(snake_win, color_snake, (*part, cell, cell))

        # Display score
        score_disp = snake_font.render("Score: " + str(snake_score), True, color_text)
        snake_win.blit(score_disp, (10, 10))

        pygame.display.flip()
        snake_clock.tick(10)

# Run snake game
if __name__ == "__main__":
    play_snake()

#third
import pygame
import math

def play_paint():
    pygame.init()
    paint_w, paint_h = 800, 600
    paint_win = pygame.display.set_mode((paint_w, paint_h))
    pygame.display.set_caption("Paint App")
    paint_clock = pygame.time.Clock()
    paint_font = pygame.font.SysFont("Arial", 20)

    bg_col = (255, 255, 255)
    shape_col = (100, 100, 255)

    is_drawing = False
    start_pt = None
    draw_shape = "square"
    paint_win.fill(bg_col)

    # Draw square with equal sides
    def draw_sq(surf, pt1, pt2):
        sz = max(abs(pt2[0] - pt1[0]), abs(pt2[1] - pt1[1]))
        rect = pygame.Rect(pt1[0], pt1[1], sz, sz)
        rect.normalize()
        pygame.draw.rect(surf, shape_col, rect, 2)

    # Draw right triangle
    def draw_right_tri(surf, pt1, pt2):
        points = [pt1, (pt1[0], pt2[1]), pt2]
        pygame.draw.polygon(surf, shape_col, points, 2)

    # Draw equilateral triangle
    def draw_eq_tri(surf, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        sz = math.dist(pt1, pt2)
        angle = math.radians(60)
        dx, dy = x2 - x1, y2 - y1
        x3 = x1 + dx * math.cos(angle) - dy * math.sin(angle)
        y3 = y1 + dx * math.sin(angle) + dy * math.cos(angle)
        points = [pt1, pt2, (int(x3), int(y3))]
        pygame.draw.polygon(surf, shape_col, points, 2)

    running = True
    while running:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                running = False

            elif evt.type == pygame.MOUSEBUTTONDOWN:
                is_drawing = True
                start_pt = evt.pos

            elif evt.type == pygame.MOUSEBUTTONUP:
                if is_drawing:
                    end_pt = evt.pos
                    if draw_shape == "square":
                        draw_sq(paint_win, start_pt, end_pt)
                    elif draw_shape == "right_triangle":
                        draw_right_tri(paint_win, start_pt, end_pt)
                    elif draw_shape == "equilateral_triangle":
                        draw_eq_tri(paint_win, start_pt, end_pt)
                    is_drawing = False

            elif evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_1:
                    draw_shape = "square"
                elif evt.key == pygame.K_2:
                    draw_shape = "right_triangle"
                elif evt.key == pygame.K_3:
                    draw_shape = "equilateral_triangle"
                elif evt.key == pygame.K_c:
                    paint_win.fill(bg_col)  # Clear screen

        pygame.display.flip()
        paint_clock.tick(60)

# Run the app
if __name__ == "__main__":
    play_paint()
