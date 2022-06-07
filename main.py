import math
import sympy as sp
from sympy import solve
from sympy.utilities.lambdify import lambdify
import simpson


x0 = 0
x1 = math.pi
num_sections = 4
x_ = sp.symbols('x')
func = sp.sin(x_)
func = lambdify(x_, func)
print(f'Value of integral is {simpson.simpsons_method(func, x0, x1, num_sections):.4f}\n')

# Error calculation
x, y = sp.symbols('x y')
func_ = sp.sin(x)
f_prime1 = func_.diff(x)
f_prime2 = f_prime1.diff(x)
func_ = lambdify(x, func_)
# f_prime1 = lambdify(x, f_prime1)
roots = solve(f_prime1, x)
f_prime3 = f_prime2.diff(x)
f_prime4 = f_prime3.diff(x)
f_prime2 = lambdify(x, f_prime2)
f_prime3 = lambdify(x, f_prime3)
f_prime4 = lambdify(x, f_prime4)


array_max = []
for i in roots:
    if f_prime2(i) < 0:
        array_max.append(i)

max_ = array_max[0]
for j in array_max:
    if func_(j) > max_:
        max_ = j

error = 0.00558
print(f'Error with {num_sections} sections: '
      f'{simpson.calculate_error_range(f_prime4(func_(max_)), x0, x1, num_sections)}:.4f\n')

# sections calculations
print(f'Amount of sections with error {error}: '
      f'{simpson.calculate_amount_of_sections(f_prime4(func_(max_)), x0, x1, error):.0f} sections')
