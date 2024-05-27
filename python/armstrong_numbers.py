def is_armstrong_number(number):
    acc = 0
    num_digits = len(str(number))
    for d in range(num_digits):
        res = int(str(number)[d]) ** num_digits
        acc += res

    return acc == number

print(is_armstrong_number(154))
