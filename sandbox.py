import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP
import math

# Инициализация pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Самолёт и круг")

# Цвета (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Переменные для движущегося круга
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 30
circle_speed_x, circle_speed_y = 5, 3

# Загрузка изображения самолёта
plane_image = pygame.image.load("data/plane.png")  # Убедись, что файл plane.png находится в той же папке
plane_image = pygame.transform.scale(plane_image, (50, 50))  # Масштабирование
plane_width, plane_height = plane_image.get_size()

# Переменные для самолёта
player_x, player_y = WIDTH // 4, HEIGHT // 2
player_speed = 5
player_angle = 0  # Угол поворота самолёта
keys_pressed = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}

# Основной цикл игры
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:  # Обработка нажатий клавиш
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == KEYUP:  # Обработка отпускания клавиш
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    # Логика движения самолёта
    player_dx, player_dy = 0, 0
    if keys_pressed[pygame.K_LEFT]:
        player_dx -= player_speed
    if keys_pressed[pygame.K_RIGHT]:
        player_dx += player_speed
    if keys_pressed[pygame.K_UP]:
        player_dy -= player_speed
    if keys_pressed[pygame.K_DOWN]:
        player_dy += player_speed

    # Угол поворота самолёта
    if player_dx != 0 or player_dy != 0:
        player_angle = math.degrees(math.atan2(-player_dy, player_dx))

    # Обновление позиции самолёта
    player_x += player_dx
    player_y += player_dy

    # Ограничение движения самолёта границами окна
    player_x = max(plane_width // 2, min(WIDTH - plane_width // 2, player_x))
    player_y = max(plane_height // 2, min(HEIGHT - plane_height // 2, player_y))

    # Логика движения круга
    circle_x += circle_speed_x
    circle_y += circle_speed_y

    # Отражение от стен
    if circle_x - circle_radius < 0 or circle_x + circle_radius > WIDTH:
        circle_speed_x = -circle_speed_x
    if circle_y - circle_radius < 0 or circle_y + circle_radius > HEIGHT:
        circle_speed_y = -circle_speed_y

    # Проверка столкновения
    distance = math.sqrt((circle_x - player_x) ** 2 + (circle_y - player_y) ** 2)
    if distance < circle_radius + plane_width // 2:
        dx = circle_x - player_x
        dy = circle_y - player_y
        magnitude = math.sqrt(dx ** 2 + dy ** 2)
        circle_speed_x = (dx / magnitude) * 7
        circle_speed_y = (dy / magnitude) * 7

    # Отрисовка
    screen.fill(WHITE)  # Заливка фона
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)  # Движущийся круг

    # Отрисовка самолёта
    rotated_plane = pygame.transform.rotate(plane_image, -player_angle)  # Поворот самолёта
    plane_rect = rotated_plane.get_rect(center=(player_x, player_y))  # Центровка
    screen.blit(rotated_plane, plane_rect.topleft)

    pygame.display.flip()  # Обновление экрана

    # Ограничение FPS
    clock.tick(60)

# Завершение работы pygame
pygame.quit()
