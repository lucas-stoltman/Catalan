# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

def catalan(num: int):
    # base case
    if num <= 1:
        return 1

    # memoization to save time
    memory = [0 for i in range(num + 1)]

    # set the first two values from the base case
    memory[0] = memory[1] = 1

    for i in range(2, num + 1):
        memory[i] = 0
        for j in range(i):
            memory[i] += memory[j] * memory[i - j - 1]

    return memory[num]
