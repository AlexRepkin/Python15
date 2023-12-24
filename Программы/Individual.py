#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func_show(func):
    """Декоратор, выводящий «Площадь прямоугольника:<значение>»"""

    def wrapper(width, height):
        print("Rectangle's square: ", func(width, height))

    return wrapper


@ func_show
def get_sq(width, height):
    """Вычисление площади прямоугольника."""

    return width * height


if __name__ == "__main__":
    height = float(input("Good day, user! Please, enter height: "))
    width = float(input("Great, now we need width: "))
    get_sq(width, height)
