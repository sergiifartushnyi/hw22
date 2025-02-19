from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def get_numbers():

    result = [fibonacci(18), fibonacci(19), fibonacci(20), 9999]
    return result

if __name__ == "__main__":
    numbers = get_numbers()
    for num in numbers:
        print(num)
