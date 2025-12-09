# 1-mashq
even_squares = tuple(i*i for i in range(2, 21, 2))
print("1)", even_squares)

# 2-mashq
mult_of_3 = tuple(i for i in range(1, 51) if i % 3 == 0)
print("2)", mult_of_3)

# 3-mashq
sample_strings = ["salom", "dunyo", "python", "tuple comprehensions"]
lengths = tuple(len(s) for s in sample_strings)
print("3)", lengths)

# 4-mashq
def digit_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

even_digit_sum = tuple(i for i in range(1, 101) if digit_sum(i) % 2 == 0)
print("4)", even_digit_sum)

# 5-mashq
words = ["python", "tuple", "set", "loop"]
first_letters = tuple(w[0] for w in words)
print("5)", first_letters)
