from collision import (
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect,
    RectCorrectError,
)

def get_rect_from_user(prompt):
    print(prompt)
    try:
        x1 = float(input("Введите x1: "))
        y1 = float(input("Введите y1: "))
        x2 = float(input("Введите x2: "))
        y2 = float(input("Введите y2: "))
        return [(x1, y1), (x2, y2)]
    except ValueError:
        print("Ошибка: введите числовые значения.")
        return get_rect_from_user(prompt)
    
def main():
    print("=== Проверка корректности прямоугольника ===")
    rect = get_rect_from_user("Введите координаты прямоугольника:")
    print(f"Прямоугольник корректен: {isCorrectRect(rect)}")

    print("\n=== Проверка пересечения двух прямоугольников ===")
    rect1 = get_rect_from_user("Введите координаты первого прямоугольника:")
    rect2 = get_rect_from_user("Введите координаты второго прямоугольника:")
    try:
        print(f"Прямоугольники пересекаются: {isCollisionRect(rect1, rect2)}")
    except RectCorrectError as e:
        print(f"Ошибка: {e}")

    print("\n=== Площадь пересечения двух прямоугольников ===")
    try:
        area = intersectionAreaRect(rect1, rect2)
        print(f"Площадь пересечения: {area}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n=== Уникальная площадь пересечения нескольких прямоугольников ===")
    rectangles = []
    n = int(input("Сколько прямоугольников вы хотите ввести? "))
    for i in range(n):
        rect = get_rect_from_user(f"Введите координаты {i+1}-го прямоугольника:")
        rectangles.append(rect)
    try:
        area = intersectionAreaMultiRect(rectangles)
        print(f"Уникальная площадь пересечения: {area}")
    except RectCorrectError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()    