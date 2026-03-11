import numpy as np
import matplotlib.pyplot as plt
import time

def calculate_objective(x, num):
    g_x = (1/2) * (x - np.log(num + x))**2
    return g_x

def compute_gradient(x, num):
    grad_x = (x - np.log(num + x)) * (1 + 1/(num + x))
    return grad_x

def gradient_descent(max_iterations, x0, num):
    f_x = []
    x = []
    x_k = x0

    L = calculate_L_step(0, 2.1, num)
    for i in range(max_iterations):
        x.append(x_k)
        f_x.append(calculate_objective(x_k, num).copy())
        gradient = compute_gradient(x_k, num)

        x_k = x_k - (1/L) * gradient

        if np.isinf(f_x[i]) or f_x[i] > 1e10:
            print(f"Diverged at step {i} (Values too large)")
            print(f_x[i])
            return np.array(f_x)

    print(f"Diverged at step {len(f_x)}")
    return np.array(f_x)

def calculate_L_step(x0, x_max, num):
    grad_x = []
    for i in np.arange(x0, x_max, 0.01):
        grad_x.append(compute_gradient(i, num).copy())

    L = np.max(grad_x)
    print(f"L = {L}")

    return L

def main():
    cords_x = np.arange(0, 2.1, 0.1)
    y_x = np.array([x for x in cords_x])
    y_ln_1 = np.array([np.log(1 + x) for x in cords_x])
    y_ln_2 = np.array([np.log(2 + x) for x in cords_x])

    fig, ax = plt.subplots()
    ax.plot(cords_x, y_x)
    ax.plot(cords_x, y_ln_1)
    ax.plot(cords_x, y_ln_2)
    plt.show()

    max_iterations = 100
    times = []

    x0 = 2

    fig, ax = plt.subplots()
    for i in range(0, 2):
        start_time = time.time()
        f_x = gradient_descent(max_iterations, x0, i + 1)
        end_time = time.time()
        times.append(end_time - start_time)

        ax.plot([i for i in range(0, len(f_x), 10)], f_x[::10])
        ax.set_yscale('log')

    plt.show()

    print("Time: ")
    print(times)


main()