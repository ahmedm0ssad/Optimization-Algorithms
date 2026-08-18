# 1D and Multidimensional Optimization Algorithms

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white)](https://scipy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)

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

---

## Author

**Ahmed Mossad** — Data Science & AI, Zewail City

- GitHub: [@ahmedm0ssad](https://github.com/ahmedm0ssad)
- LinkedIn: [Ahmed Mossad](https://linkedin.com/in/ahmed-mossad-4528202b2)