# 1D and Multidimensional Optimization Algorithms

Implementations of classical line-search and multidimensional optimization algorithms, tested against benchmark functions and compared with `scipy.optimize` references.

## Algorithms

**1D (line search):**
- Fibonacci Search
- Golden Section Search
- Newton's Method
- Secant Method

**Multidimensional:**
- Quasi-Newton (BFGS)
- Fletcher-Reeves Conjugate Gradient
- Marquardt (Levenberg-Marquardt)

## Benchmark Functions

- **Rosenbrock's function** — classic non-convex valley benchmark.
- **Powell's function** — quadratic with correlated variables.

Each implementation is compared against the corresponding `scipy.optimize` reference.

## Structure

```
├── notebooks/
│   └── optimization_algorithms.ipynb
├── src/
│   └── 1d_minimization.py
└── README.md
```

## Requirements

- `numpy`
- `scipy.optimize`