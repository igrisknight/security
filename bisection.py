# Bisection Method Algorithm Implementation

# Define the function for which we want to find the root
def f(x):
    return x**2 - 3  # The function we want to find the root of

# Bisection method function
def bisection(a, b, tol):
    # Check if f(a) and f(b) have opposite signs
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) should have opposite signs.")
        return None

    while (b - a) / 2 > tol:  # Repeat until the interval is smaller than tolerance
        t = (a + b) / 2  # Find the midpoint
        print(f"Interval: [{a}, {b}], Midpoint: {t}, f(t): {f(t)}")

        if f(t) == 0:  # Exact root found
            return t
        elif f(t) * f(a) < 0:  # Root is between a and t
            b = t
        else:  # Root is between t and b
            a = t

    return (a + b) / 2  # Return the midpoint as the root

# Example usage
a = 1  # Lower bound of the interval
b = 2  # Upper bound of the interval
tolerance = 1e-6  # Tolerance level

root = bisection(a, b, tolerance)
if root is not None:
    print(f"The root of the function is: {root:.6f}")
