#Define a Python class V2, which represents two-dimensional vectors and
#supports the following operations:
#• Create a new vector out of two real numbers: v = V2(1.1, 2.2)
#• Convert a vector to a string (with the __str__ method)
#• Access the components (with the getX and getY methods)
#• Add two V2s to get a new V2 (with add and __add__ methods)
#• Multiply a V2 by a scalar (real or int) and return a new V2 (with the mul
#and __mul__ methods)

class V2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
       return f"({self.x}, {self.y})"

    def add(self, other):
       if not isinstance(other, V2):
            raise TypeError("Invalid type. Cannot add a non-V2 object to V2.")

       new_x = self.x + other.x
       new_y = self.y + other.y
       return V2(new_x, new_y)

    def __add__(self, other):
       return self.add(other)

    def mul(self, scalar):
        if not (isinstance(scalar, int) or isinstance(scalar, float)):
            raise TypeError("Invalid type. Cannot multiply V2 by non-scalar.")

        new_x = self.x * scalar
        new_y = self.y * scalar
        return V2(new_x, new_y)

    def __mul__(self, scalar):
       return self.mul(scalar)

# Create a new vector
v = V2(1.1, 2.2)

# Access components
x = v.getX()
y = v.getY()
print(f"x-component: {x}")
print(f"y-component: {y}")

# Convert to string
vector_str = str(v)
print(f"Vector: {vector_str}")

# Add two vectors
v1 = V2(1.5, 2.5)
v2 = V2(0.5, 1.0)
sum_vector = v1 + v2
print(f"Sum of vectors: {sum_vector}")

# Multiply a vector by a scalar
scalar = 2.5
scaled_vector = v * scalar
print(f"Scaled vector: {scaled_vector}")

