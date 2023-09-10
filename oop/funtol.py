import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*2
x=fx(n)
print(x(6))
print(x(5))
print(x(2))
print(x(2))
print(x(3))
print(x(2))
print(x(5))
print(x(6))
print(x(2))
print(x(3))