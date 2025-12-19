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

