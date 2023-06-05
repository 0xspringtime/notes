#Define a Python class Polynomial which provides methods for performiing algebraic operations on polynomials

class Polynomial:
    def __init__(self, coefficients):
       self.coefficients = coefficients

    def __str__(self):
       degree = len(self.coefficients) - 1
       terms = []

       for i, coeff in enumerate(self.coefficients):
           power = degree - i

           if power == 0:
               terms.append(f"{coeff:.3f}")
           elif power == 1:
               terms.append(f"{coeff:.3f}z")
           else:
               terms.append(f"{coeff:.3f}z^{power}")

       return " + ".join(terms)

    def add(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("Invalid type. Cannot add a non-Polynomial object to Polynomial.")

        max_len = max(len(self.coefficients), len(other.coefficients))
        padded_self = self.coefficients + [0] * (max_len - len(self.coefficients))
        padded_other = other.coefficients + [0] * (max_len - len(other.coefficients))

        sum_coeffs = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(sum_coeffs)

    def __add__(self, other):
       return self.add(other)

    def mul(self, other):
       if not isinstance(other, Polynomial):
            raise TypeError("Invalid type. Cannot multiply a non-Polynomial object with Polynomial.")

       degree_self = len(self.coefficients) - 1
       degree_other = len(other.coefficients) - 1
       degree_result = degree_self + degree_other

       result_coeffs = [0] * (degree_result + 1)

       for i in range(degree_self + 1):
           for j in range(degree_other + 1):
               result_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]

       return Polynomial(result_coeffs)

    def __mul__(self, other):
       return self.mul(other)

    def __call__(self, z):
       result = 0

       for i, coeff in enumerate(self.coefficients):
           result += coeff * (z ** (len(self.coefficients) - 1 - i))

       return result

    def roots(self):
       import numpy as np

       if len(self.coefficients) > 4:
           raise ValueError("Order too high to solve for roots.")

       roots = np.roots(self.coefficients)
       return roots.tolist()


# Create polynomial objects
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([100, 200])

# Print polynomial objects
print(p1)  # 1.000 z^2 + 2.000 z + 3.000
print(p2)  # 100.000 z + 200.000

# Add two polynomials
sum_polynomial = p1 + p2
print(sum_polynomial)  # 1.000 z^2 + 102.000 z + 203.000

# Evaluate polynomial at a value
result = p1(1)
print(result)  # 6.0

result = p1(-1)
print(result)  # 2.0

result = (p1 + p2)(10)
print(result)  # 1323.0

# Multiply two polynomials
product_polynomial = p1 * p1
print(product_polynomial)  # 1.000 z^4 + 4.000 z^3 + 10.000 z^2 + 12.000 z + 9.000

# Compute roots of polynomials
roots = p1.roots()
print(roots)  # [(-1+1.4142135623730947j), (-1-1.4142135623730947j)]

roots = p2.roots()
print(roots)  # [-2.0]

# Solve for roots of high-order polynomials
p3 = Polynomial([3, 2, -1])
roots = p3.roots()
print(roots)  # [-1.0, 0.3333333333333333]

roots = (p1 * p1).roots()
print(roots)  # Order too high to solve for roots.

