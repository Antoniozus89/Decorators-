def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            if all(result % i != 0 for i in range(2, int(result ** 0.5) + 1)):
                print("Простое")
            else:
                print("Составное")
        else:
            print("Не является числом")
    return wrapper

@is_prime
def sum_three(a, b, c):
    print(a + b + c)
    return a + b + c
sum_three(7,3,6)

