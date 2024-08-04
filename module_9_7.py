def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res % res or res % 1:
            print(f'Составное')
        else:
            print(f'Простое')
        return res

    return wrapper


@is_prime
def sum_three(*num):
    return sum(num)


result = sum_three(2, 3, 6)
print(result)
