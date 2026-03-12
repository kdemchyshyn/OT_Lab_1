## **Task 1**
Objective function:
$$
f(x) = 100(x_2 - (x_1 ^ 2)) ^ 2 + (1 - x_1) ^ 2
$$

Gradient:
$$
\nabla f = \left( 400x_1^3 - 400x_1x_2 + 2x_1 - 2, -200x_1^2 + 200x_2 \right)
$$

Convergence:
1. Step: 0.1

    After very first iteration, function value have become too large. This means that the step size is too big, and function is divergent.   

2. Step: 0.01

    Similar to step 0.1, after second iteration function value becomes too large, so function is divergent.
    Step size is too big. 

3. Step: 0.001

    Algorithm successfully completes 10,000 iterations. It's final values are near real global minimum (x* = [1, 1]).
    Function convergence rate is sublinear -> if we look at the plot function value drops significantly in the beginning and then stays on the plato, but never reaches expected error.
    For linear or superlinear convergence it was suppose to reach it within 1-2 iterations.

---
## **Task 2**

Objective function:
$$
f(x) = \frac{1}{2m} ||Ax-b||^2
$$

Gradient:
$$
\nabla f = \frac{1}{m} A^T(Ax - b)
$$

Convergence:
1. Step: 0.1

    Convergence rate for this step size is linear. The plot goes down - not too slow or fast.

2. Step: $\frac{1}{\beta}$

     Convergence rate is superlinear. Plot line goes down really fast with each iteration.

3. Step: $\frac{1}{L}$

     Convergence rate is sublinear because graph goes down really slow.


---
## **Task 3**

Original functions:
$$
f(x)_1 = ln(1 + x)
$$
$$
f(x)_2 = ln(2 + x)
$$

Objective functions:
$$
g(x)_1 = \frac{1}{2} (x - ln(1 + x))^2
$$
$$
g(x)_2 = \frac{1}{2} (x - ln(2 + x))^2
$$

Derivatives:
$$
g(x)_1' = (x - ln(1 + x)) * (1 - \frac{1}{1 + x})
$$
$$
g(x)_2' = (x - ln(2 + x)) * (1 - \frac{1}{2 + x})
$$

Convergence:
1. Step: $\frac{1}{L_1}$

    Convergence is linear (from the plot). The function converges slowly but steady.

2. Step: $\frac{1}{L_2}$

     From the plot, we can see that convergence is superlinear and drops down rapidly (up to $10^{10}$ per iteration).

