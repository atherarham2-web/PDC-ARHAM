
import math
from threading import Thread
import time

def mensuration_calculations():
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6

    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    area_rect = l * b
    peri_rect = 2 * (l + b)
    area_square = a ** 2
    peri_square = 4 * a
    area_triangle = 0.5 * b * h

    sa_cube = 6 * a ** 2
    vol_cube = a ** 3
    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h
    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h

    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )

    return total


class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        result = mensuration_calculations()
        print(f"{self.name} → Mensuration Total = {result}")


def main():
    # Creating threads
    thread1 = MyThreadClass("Thread #1")
    thread2 = MyThreadClass("Thread #2")

    # Starting threads
    thread1.start()
    thread2.start()

    # Waiting for threads to finish
    thread1.join()
    thread2.join()

    print("End")


if __name__ == "__main__":
    main()
