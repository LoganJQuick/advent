import timeit
import random

def has33(number_list):
    return any(number_list[i] == 3 and number_list[i + 1] == 3 for i in range(len(number_list) - 1))
        
def has33_v2(number_list):
    return '33' in "".join(str(number_list))

rand_lists = [[random.randint(0, 9) for _ in range(20)] for _ in range(10000)]


before = timeit.default_timer()
for rand_list in rand_lists:
    has33(rand_list)
after = timeit.default_timer()
print(after - before) # 0.0299 Seconds 

before = timeit.default_timer()
for rand_list in rand_lists:
    has33_v2(rand_list)
after = timeit.default_timer()
print(after - before) # 0.0517 seconds