import random

def get_divisors(n: int) -> list[int]:
        divisors = []
        for i in range(1, abs(n) + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors

def quadratic_formula(a: float, b: float, c: float) -> list[float]:
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero.")
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # No hay raíces reales
    elif discriminant == 0:
        return [-b / (2*a), -b / (2*a)]  # Una raíz doble
    else:
        return [(-b + discriminant**0.5) / (2*a), (-b - discriminant**0.5) / (2*a)]
    
def gaussian_factorization(polynomial: list[float]) -> list[float]:
    # Implementación del algoritmo de factorización de Gauss
    # Divisores del coeficiente ppal
    main_coefficient_divisors = get_divisors(polynomial[0])
    # Divisores del término independiente
    independente_term_divisors = get_divisors(polynomial[-1])
    # Candidatos a raíces
    root_candidates = []
    for i in main_coefficient_divisors:
        for j in independente_term_divisors:
            root_candidates.append(i / j)
    quotient = polynomial[:]
    roots = []
    while len(quotient) > 3 and len(root_candidates) > 0:
        new_root = root_candidates.pop(0)
        # Teorema del resto
        remainder = sum(coef * (new_root ** exp) for exp, coef in enumerate(reversed(quotient)))
        while remainder == 0:
            roots.append(new_root)
            # División sintética
            for i in range(1,len(quotient) - 1):
                quotient[i] = quotient[i - 1] * new_root + quotient[i]
            quotient.pop()
            remainder = sum(coef * (new_root ** exp) for exp, coef in enumerate(reversed(quotient)))
    # Single root remaining
    if len(quotient) == 2:
        print(quotient)
        roots.append(-quotient[1] / quotient[0])
    # Quadratic remaining
    if len(quotient) == 3:
        return roots + quadratic_formula(quotient[0], quotient[1], quotient[2])
    else:
        return roots
    
def scramble_roots(polynomial : list[float]) -> list[float]:
    random.shuffle(polynomial)
    return polynomial

def factorize_polynomial(polynomial : list[float]) -> list[float]:
    roots = []
    for coefficient in polynomial:
        if not isinstance(coefficient, (int, float)):
            raise TypeError("Los coeficientes del polinomio deben ser números")
    # Recortar 0s iniciales
    while len(polynomial) > 0 and polynomial[0] == 0:
        polynomial.pop(0)
    if len(polynomial) <= 1:
        raise ValueError("El polinomio debe ser al menos de grado 2")
    elif len(polynomial) == 2:
        # La raíz de una función lineal es -b/a
        roots = [-polynomial[1] / polynomial[0]]
    elif len(polynomial) == 3:
        roots =  quadratic_formula(polynomial[0], polynomial[1], polynomial[2])
    else:
        roots = gaussian_factorization(polynomial)
    return scramble_roots(roots)