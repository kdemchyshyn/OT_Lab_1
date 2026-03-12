import numpy as np
import matplotlib.pyplot as plt
import time

A = np.array([[1, 0], [0, 2]])
b = np.array([1, 1])

def calculate_objective(x):
    f_x =(1/(2*len(b))) * np.linalg.norm((A @ x-b), 2)**2
    return f_x

def compute_gradient(x):
    grad_x= (1/(2*len(b))) * (np.transpose(A) @ (A @ x - b))

    return grad_x

def gradient_descent(max_iterations, step_size, x0):
    f_x = []
    x = []
    x_k = x0.astype(float)

    for i in range(max_iterations):
        x.append(x_k)
        f_x.append(calculate_objective(x_k))
        gradient = compute_gradient(x_k)

        x_k = x_k - step_size * gradient

    print(f"Diverged at step {len(f_x)}")
    return np.array(f_x)

def calculate_step(A):
    Q = (np.transpose(A) @ A)
    B = (1/(len(b))) * np.linalg.norm(Q, 2)

    return (1/B)

def calculate_L_step(bound):
    Q_norm = np.linalg.norm((np.transpose(A) @ A), 2)
    Ab_norm = np.linalg.norm((A @ b), 2)

    L = (1/(len(b))) * (Q_norm * bound + Ab_norm)

    return (1/L)

def main():
    max_iterations = 50
    steps = [0.1, calculate_step(A), calculate_L_step(20)]
    times = []

    x0 = np.array([-2, 2])
    x0 = np.transpose(x0)

    fig, ax = plt.subplots()
    for step in steps:
        start_time = time.time()
        f_x = gradient_descent(max_iterations, step, x0)
        end_time = time.time()
        times.append(end_time - start_time)


        ax.plot([i for i in range(0, len(f_x))], f_x)

    plt.show()

    print("Time: ")
    print(times)


main()