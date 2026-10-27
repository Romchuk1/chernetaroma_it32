import math
import sys

print("Roman Cherneta, IT-32")

# Розміри кімнати в метрах — заміни на свої вимірювання
LENGTH = 4.2
WIDTH = 3.5
HEIGHT = 2.7

# Розміри дверей і вікна
DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.0
WINDOW_WIDTH = 1.4
WINDOW_HEIGHT = 1.5

# Розміри плитки в метрах
TILE_LENGTH = 0.3
TILE_WIDTH = 0.3
TILE_PRICE = 42.30

if min(LENGTH, WIDTH, HEIGHT, TILE_LENGTH, TILE_WIDTH) <= 0:
    print("Помилка: розміри мають бути більшими за нуль.", file=sys.stderr)
    sys.exit(1)

floor_area = LENGTH * WIDTH
wall_area = 2 * (LENGTH * HEIGHT + WIDTH * HEIGHT)
wall_area -= DOOR_WIDTH * DOOR_HEIGHT
wall_area -= WINDOW_WIDTH * WINDOW_HEIGHT

floor_diagonal = math.hypot(LENGTH, WIDTH)
room_diagonal = math.dist(
    (0, 0, 0),
    (LENGTH, WIDTH, HEIGHT)
)

tile_area = TILE_LENGTH * TILE_WIDTH
tiles_exact = floor_area / tile_area

print(f"room:          {LENGTH} x {WIDTH} x {HEIGHT} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2")
print(f"floor diag:    {floor_diagonal:.2f} m")
print(f"room diag:     {room_diagonal:.2f} m")

print(f"\ntiles exact:   {tiles_exact:.2f}")
print(f"  round:       {round(tiles_exact)}")
print(f"  floor:       {math.floor(tiles_exact)}")
print(f"  ceil:        {math.ceil(tiles_exact)}")

tiles_to_buy = math.ceil(tiles_exact * 1.10)
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")

paint_liters = wall_area / 10 * 2
paint_cans = math.ceil(paint_liters / 2.5)

print(f"paint:         {paint_liters:.2f} l")
print(f"paint cans:    {paint_cans} cans of 2.5 l")

cost_mul = tiles_to_buy * TILE_PRICE

cost_sum = 0
for _ in range(tiles_to_buy):
    cost_sum += TILE_PRICE

print(f"\ntiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul):.15f}")