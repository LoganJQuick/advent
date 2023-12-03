import timeit
import random
import numpy

def has33(number_list):
    return any(number_list[i] == 3 and number_list[i + 1] == 3 for i in range(len(number_list) - 1))
        
def has33_v2(number_list):
    return '33' in "".join(str(number_list))

rand_lists = [random.randint(0, 9) for _ in range(10000000)]
# rand_lists = numpy.array(rand_lists)


before = timeit.default_timer()
has33(rand_lists)
after = timeit.default_timer()
print(f"Logan's Method: {after - before}") # 2.930e-05 seconds

before = timeit.default_timer()
has33_v2(rand_lists)
after = timeit.default_timer()
print(f"Randy's Method: {after - before}" ) # 1.948 seconds