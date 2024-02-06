import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Рисование фигур")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Координаты и размеры фигур
circle_x, circle_y = 100, 100
circle_radius = 50

square_x, square_y = 200, 200
square_size = 100

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очищаем экран
    screen.fill(white)

    # Рисуем круг
    pygame.draw.circle(screen, black, (circle_x, circle_y), circle_radius)

    # Рисуем квадрат
    pygame.draw.rect(screen, black, (square_x, square_y, square_size, square_size))

    # Обновляем экран
    pygame.display.flip()

    # Задержка для управления скоростью анимации
    pygame.time.delay(100)
