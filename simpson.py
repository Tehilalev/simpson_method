def simpsons_method(function, a, b, n):
    h = (b - a) / n

    x_ = list()  # List for values of x
    fx = list()  # List for values of f(x)

    i = 0
    while i <= n:
        x_.append(a + i * h)
        fx.append(function(x_[i]))
        i += 1

    # Calculating result
    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
        i += 1
    return res * (h / 3)


def calculate_error_range(value, a, b, n):
    h = (b - a) / n
    return (1 / 180) * h ** 4 * (b - a) * value


def calculate_amount_of_sections(value, a, b, error):
    return (b - a) / ((180 * error) / ((b - a) * value) ** 0.25)
