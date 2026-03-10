import numpy as np
import matplotlib.pyplot as plt
import time

def calculate_objective(x):
    x1 = x[0]
    x2 = x[1]

    f_x = 100 * (x2 - (x1 ** 2)) ** 2 + (1 - x1) ** 2
    return f_x

def compute_gradient(x):
    x1 = x[0]
    x2 = x[1]

    grad_x1 = 400 * np.power(x1, 3) - 400 * x1 * x2 + 2 * x1 - 2
    grad_x2 = -200 * np.power(x1, 2) + 200 * x2

    return np.array([grad_x1, grad_x2])

def gradient_descent(max_iterations, step_size, x0):
    error = 1e-4

    f_x = []
    x = []
    x_k = x0

    for i in range(max_iterations):
        x.append(x_k.copy())
        f_x.append(calculate_objective(x_k).copy())
        gradient = compute_gradient(x_k)

        if (np.linalg.norm(gradient) < error):
            return np.array(f_x)

        x_k = x_k - step_size * gradient

        if np.isinf(f_x[i]) or f_x[i] > 1e10:
            print(f"Diverged at step {i} (Values too large)")
            print(f"x: {x_k}, {f_x[i]}")
            return np.array(f_x)

    print(f"Diverged at step {len(f_x)}")
    print(f"x: {x_k}, f(x): {f_x[i]}")
    return np.array(f_x)

def main():
    max_iterations = 10000
    steps = [0.1, 0.01, 0.001]
    times = []

    x0 = np.array([-2, 2])
    for step in steps:
        start_time = time.time()
        f_x = gradient_descent(max_iterations, step, x0)
        end_time = time.time()
        times.append(end_time - start_time)

        fig, ax = plt.subplots()
        ax.plot([i for i in range(0, len(f_x))], f_x)
        plt.show()

    print("Time: ")
    print(times)

main()