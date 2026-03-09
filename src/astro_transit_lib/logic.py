import time

def fibonacci_with_timeout(timeout_sec):
    a, b = 0, 1
    start_time = time.time()
    while True:
        yield a
        if (time.time() - start_time) > timeout_sec:
            break
        a, b = b, a + b