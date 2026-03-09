import sys
import os
import matplotlib.pyplot as plt 

sys.path.append(os.path.abspath("./src"))

from astro_transit_lib.logic import get_kepler_data, plot_frame

def main():
    print("--- Запуск астрономічного проекту ---")
    
    target = "KIC 6922244"
    print(f"Крок 1: Завантаження даних для зірки {target}...")
    
    try:
        # 3. Викликаємо завантаження
        data = get_kepler_data(target, q=4)
        
        print("Крок 2: Побудова графіка кадру №42...")
        # 4. Викликаємо малювання
        plot_frame(data, frame_number=42)
        
        # 5. Тримаємо вікно з графіком відкритим
        print("Готово! Графік має з'явитися в окремому вікні.")
        plt.show() 
        
    except Exception as e:
        print(f"Ой, виникла помилка: {e}")

if __name__ == "__main__":
    main()