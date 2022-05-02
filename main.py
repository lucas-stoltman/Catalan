# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

from catalan import catalan

print("-------Testing-------")
for i in range(10):
    print(f"n({i}) : {catalan(i)}")

print("\n-------Negative-------")
for i in range(-9, 0):
    print(f"n({i}) : {catalan(i)}")
