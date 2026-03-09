import sys
import os

sys.path.append(os.path.abspath("./src"))

from astro_transit_lib.logic import fibonacci_with_timeout

print("--- Запуск демонстрации библиотеки ---")
timeout = 0.5
for num in fibonacci_with_timeout(timeout):
    print(f"Найдено число: {num}")
    if num > 1000: 
        break