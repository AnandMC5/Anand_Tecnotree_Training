import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.5f} seconds to execute.")
        return result
    return wrapper

@measure_time
def example_function():
    time.sleep(2)
    return "Done!"

result = example_function()
print(result)
