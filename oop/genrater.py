def my_genrater():
    for i in range(50000):
        yield i
x=my_genrater()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
for i in x:
    print(i)