
import math
import multiprocessing

# ------------------- Mensuration Functions -------------------

def perform_mensuration_calculations():
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

    for i in range(100):
        total += math.sqrt(total * i + 1)

    return total

# ------------------- Multiprocessing Section -------------------

def send_mensuration_result(pipe):
    output_pipe, _ = pipe
    result = perform_mensuration_calculations()
    output_pipe.send(result)
    output_pipe.close()

def square_received_value(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        value = input_pipe.recv()
        output_pipe.send(value * value)
    except EOFError:
        pass
    output_pipe.close()

if __name__ == '__main__':

    # First Pipe: Send mensuration result
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(
        target=send_mensuration_result, args=(pipe_1,))
    process_pipe_1.start()

    # Second Pipe: Squares the received result
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(
        target=square_received_value, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print("Final Output:", pipe_2[1].recv())
    except EOFError:
        print("End")
