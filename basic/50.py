# #map
# def cube(x):
#     return x*x*x
# l=[1,3,46,78,99,6]
# # new = []
# # for item in l:
# #     new.append(cube(item))
# new=list(map(cube,l))    
# print(new)
# # filter
# def filter_function(a):
#     return a>2
# new=list(filter(filter_function,l))
# print(new)
from functools import reduce
l=[1,3,46,78,99,6]
new=reduce(lambda x,y:x+y,l)
print(new)