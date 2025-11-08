
import math
import threading
import time

# ============================
# Mensuration Function
# ============================
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

# ============================
# Thread Functions
# ============================
def function_A():
    print(threading.currentThread().getName() + " --> starting\n")
    result = mensuration_calculations()
    print(threading.currentThread().getName() + f" --> Result: {result}\n")
    print(threading.currentThread().getName() + " --> exiting\n")

def function_B():
    print(threading.currentThread().getName() + " --> starting\n")
    result = mensuration_calculations()
    print(threading.currentThread().getName() + f" --> Result: {result}\n")
    print(threading.currentThread().getName() + " --> exiting\n")

def function_C():
    print(threading.currentThread().getName() + " --> starting\n")
    result = mensuration_calculations()
    print(threading.currentThread().getName() + f" --> Result: {result}\n")
    print(threading.currentThread().getName() + " --> exiting\n")

# ============================
# Main
# ============================
if __name__ == "__main__":
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
