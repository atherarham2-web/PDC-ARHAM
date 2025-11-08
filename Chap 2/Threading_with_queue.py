
import math
from threading import Thread
from queue import Queue
import time


# =======================
# Mensuration Calculations
# =======================
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


# =======================
# Producer - Consumer Code
# =======================
class Producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):
            result = mensuration_calculations()
            self.queue.put(result)
            print(f"Producer notify: Mensuration result {result:.2f} added to queue by {self.name}")
            time.sleep(1)


class Consumer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            result = self.queue.get()
            print(f"Consumer notify: Result {result:.2f} processed by {self.name}")
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue()

    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
