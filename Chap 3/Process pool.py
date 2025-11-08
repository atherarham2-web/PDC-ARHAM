import math
import multiprocessing

# ---------------------------------------------
# Mensuration Functions
# ---------------------------------------------
def perform_mensuration_calculations(_):
    """
    Perform comprehensive mensuration calculations for various 2D and 3D shapes.
    The unused parameter '_' is required because pool.map passes arguments.
    """
    # Shape parameters
    r = 7.5  # radius
    l, b, h = 12, 8, 5  # length, breadth, height
    a = 6  # side
    
    # 2D Shapes
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    area_rect = l * b
    peri_rect = 2 * (l + b)
    area_square = a ** 2
    peri_square = 4 * a
    area_triangle = 0.5 * b * h
    
    # 3D Shapes
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
    
    # Extra computation (CPU load)
    for i in range(100):
        total += math.sqrt(total * i + 1)
    
    return total


def calculate_2d_shapes():
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6
    return {
        'circle_area': math.pi * r ** 2,
        'circle_perimeter': 2 * math.pi * r,
        'rectangle_area': l * b,
        'rectangle_perimeter': 2 * (l + b),
        'square_area': a ** 2,
        'square_perimeter': 4 * a,
        'triangle_area': 0.5 * b * h
    }


def calculate_3d_shapes():
    r = 7.5
    l, b, h = 12, 8, 5
    a = 6
    return {
        'cube_surface_area': 6 * a ** 2,
        'cube_volume': a ** 3,
        'cuboid_surface_area': 2 * (l*b + b*h + h*l),
        'cuboid_volume': l * b * h,
        'cylinder_surface_area': 2 * math.pi * r * (r + h),
        'cylinder_volume': math.pi * r ** 2 * h
    }

# ---------------------------------------------
# Using Process Pool (Chapter 3)
# ---------------------------------------------
if __name__ == '__main__':
    
    # Dummy list to trigger parallel runs
    tasks = list(range(10))  # Run mensuration 10 times in parallel
    
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(perform_mensuration_calculations, tasks)

    pool.close()
    pool.join()

    print("Parallel Mensuration Results:")
    for index, value in enumerate(results):
        print(f"Task {index}: {value}")
