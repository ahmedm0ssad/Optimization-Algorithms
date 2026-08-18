import numpy as np

def fibonacci_method(f, a, b, tol=1e-5, max_iter=100):
    """
    Perform Fibonacci search to find the minimum of a unimodal function within a specified interval.
    """
    # Generate Fibonacci numbers
    fib = [1, 1]
    while fib[-1] < (b - a) / tol:
        fib.append(fib[-1] + fib[-2])
    
    n = len(fib) - 1
    k = 0
    x1 = a + (fib[n-2] / fib[n]) * (b - a)
    x2 = a + (fib[n-1] / fib[n]) * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    iterations = 0

    while k < n - 2 and iterations < max_iter:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (fib[n-k-1] / fib[n-k]) * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (fib[n-k-2] / fib[n-k]) * (b - a)
            f1 = f(x1)
        k += 1
        iterations += 1

    if f1 < f2:
        return x1, iterations
    else:
        return x2, iterations

def golden_section_method(f, a, b, tol=1e-5, max_iter=100):
    """
    Perform Golden Section search to find the minimum of a unimodal function within a specified interval.
    """
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    iterations = 0

    while abs(b - a) > tol and iterations < max_iter:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + resphi * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - resphi * (b - a)
            f2 = f(x2)
        iterations += 1

    if f1 < f2:
        return x1, iterations
    else:
        return x2, iterations

def newtons_method(f, df, ddf, x0, tol=1e-5, max_iter=100):
    """
    Perform Newton's method to find the minimum of a function.
    """
    x = x0
    iterations = 0

    for _ in range(max_iter):
        dfx = df(x)
        ddfx = ddf(x)
        if abs(dfx) < tol:
            break
        x = x - dfx / ddfx
        iterations += 1

    return x, iterations

def quasi_newton_method(f, df, x0, tol=1e-5, max_iter=100):
    """
    Perform the Quasi-Newton method to find the minimum of a function.
    """
    x = x0
    H = 1.0  # Initial Hessian approximation (scalar for 1D)
    iterations = 0

    for _ in range(max_iter):
        dfx = df(x)
        if abs(dfx) < tol:
            break
        p = -H * dfx
        alpha = 1.0  # Line search can be implemented here
        x_new = x + alpha * p
        s = x_new - x
        y = df(x_new) - dfx
        rho = 1.0 / (y * s)
        H = (1 - rho * y * s) * H + rho * s * s
        x = x_new
        iterations += 1

    return x, iterations

def secant_method(f, df, x0, x1, tol=1e-5, max_iter=100):
    """
    Perform the Secant method to find the minimum of a function.
    """
    iterations = 0

    for _ in range(max_iter):
        dfx0 = df(x0)
        dfx1 = df(x1)
        if abs(dfx1) < tol:
            break
        x2 = x1 - dfx1 * (x1 - x0) / (dfx1 - dfx0)
        x0, x1 = x1, x2
        iterations += 1

    return x1, iterations
