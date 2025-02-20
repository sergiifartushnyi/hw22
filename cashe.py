import redis
import datetime

r = redis.Redis(host='localhost', port=6379, db=0)

call_count = 0

t1 = "dataline"

def fibonacci(n):
    global call_count

    cached_value = r.get(f"fibonacci:{n}")
    if cached_value:
        call_count += 1
        return int(cached_value)

    if n <= 2 :
        result = 1
    else:
        a, b = 1, 1
        for i in range(3, n + 1):
            a, b = b, a + b
        result = b

    r.set(f"fibonacci:{n}", result)
    return result

def get_numbers():
    result = []
    for i in range(1, 10000):
        result.append(fibonacci(i))
    return result

def print_number_in_column(number):
    number_str = str(number)


    for i in range(0, len(number_str), 4):
        print(number_str[i:i+4])

if __name__ == "__main__":
    start_time = datetime.datetime.now()

    try:
        numbers = get_numbers()
        for num in numbers:
            print_number_in_column(num)
    except redis.RedisError as e:
        print(f"Error with Redis: {e}")

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time

    print(f"Fibonacci function called {call_count} times.")
    print(f"Execution time: {elapsed_time}")
