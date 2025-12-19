def isCorrectRect(rect):
    (x1, y1), (x2, y2) = rect
    return x1 < x2 and y1 < y2

class RectCorrectError(Exception):
    pass

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некорректный")

    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2

    return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)

def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise ValueError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise ValueError("2й прямоугольник некорректный")

    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2

    x_left = max(x1, x3)
    x_right = min(x2, x4)
    y_bottom = max(y1, y3)
    y_top = min(y2, y4)

    if x_right <= x_left or y_top <= y_bottom:
        return 0.0

    return (x_right - x_left) * (y_top - y_bottom)

def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0.0

    for rect in rectangles:
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Прямоугольник {rect} некорректный")

    common_x_left = max(rect[0][0] for rect in rectangles)
    common_x_right = min(rect[1][0] for rect in rectangles)
    common_y_bottom = max(rect[0][1] for rect in rectangles)
    common_y_top = min(rect[1][1] for rect in rectangles)

    if common_x_right <= common_x_left or common_y_top <= common_y_bottom:
        return 0.0

    return (common_x_right - common_x_left) * (common_y_top - common_y_bottom)
 
