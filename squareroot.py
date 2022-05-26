def square_root():
    a = 60
    upperBound = 8
    lowerBound = 7
    guess = (upperBound + lowerBound)/(2.0)
    eps = 1e-10
    while abs(a - guess**2) > eps:
        if guess**2 > a:
            upperBound = guess
        elif guess**2 < a:
            lowerBound = guess
        else:
            return guess
        guess = (upperBound + lowerBound)/(2.0)
    return guess

print(square_root())
