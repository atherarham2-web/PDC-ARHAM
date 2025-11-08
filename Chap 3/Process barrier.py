
import math
import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

# -----------------------------------------
# MENSURATION CALCULATION FUNCTIONS
# -----------------------------------------
def perform_mensuration_calculations():
    """
    Perform comprehensive mensuration calculations for various 2D and 3D shapes
    Returns the total computed value
    """
    # Shape parameters
    r = 7.5  # radius
    l, b, h = 12, 8, 5  # length, breadth, height
    a = 6  # side
    
    # 2D Shape Calculations
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    area_rect = l * b
    peri_rect = 2 * (l + b)
    area_square = a ** 2
    peri_square = 4 * a
    area_triangle = 0.5 * b * h
    
    # 3D Shape Calculations
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
    
    # Additional computation to increase CPU effort
    for i in range(100):
        total += math.sqrt(total * i + 1)
    
    return total


def calculate_2d_shapes():
    """Calculate only 2D shapes areas and perimeters"""
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6
    
    calculations = {
        'circle_area': math.pi * r ** 2,
        'circle_perimeter': 2 * math.pi * r,
        'rectangle_area': l * b,
        'rectangle_perimeter': 2 * (l + b),
        'square_area': a ** 2,
        'square_perimeter': 4 * a,
        'triangle_area': 0.5 * b * h
    }
    
    return calculations


def calculate_3d_shapes():
    """Calculate only 3D shapes surface areas and volumes"""
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6
    
    calculations = {
        'cube_surface_area': 6 * a ** 2,
        'cube_volume': a ** 3,
        'cuboid_surface_area': 2 * (l*b + b*h + h*l),
        'cuboid_volume': l * b * h,
        'cylinder_surface_area': 2 * math.pi * r * (r + h),
        'cylinder_volume': math.pi * r ** 2 * h
    }
    
    return calculations


# -----------------------------------------
# MULTIPROCESSING SECTION
# -----------------------------------------
def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    
    # Run mensuration calculations
    result = perform_mensuration_calculations()
    
    now = time()
    with serializer:
        print(f"{name} --> {datetime.fromtimestamp(now)} | Calculated Total = {result:.2f}")


def test_without_barrier():
    name = multiprocessing.current_process().name
    
    # Run mensuration calculations
    result = perform_mensuration_calculations()
    
    now = time()
    print(f"{name} --> {datetime.fromtimestamp(now)} | Calculated Total = {result:.2f}")


# -----------------------------------------
# MAIN PROCESS CONTROL
# -----------------------------------------
if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()

    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
