# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0
import timeit
from catalan import catalan

print("-------Testing-------")
for i in range(10):
    print(f"n({i}) : {catalan(i)}")

print("\n-------Negative-------")
for i in range(-9, 0):
    print(f"n({i}) : {catalan(i)}")

# TODO floats
# print("\n-------Floats-------")


print("\n-------Efficiency-------")
n = 10
print(f"n({n})")
t = timeit.Timer(f"catalan({n})", "from catalan import catalan")
duration = t.timeit(1000)
print("Time:", duration, "ms")
