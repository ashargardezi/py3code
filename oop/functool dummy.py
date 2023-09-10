import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*2
print(fx(6))
print(fx(5))
print(fx(2))
print(fx(2))
print(fx(3))
print(fx(2))
print(fx(5))
print(fx(6))
print(fx(2))
print(fx(3))