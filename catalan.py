# Created by Lucas Stoltman
# Program 4
# April 29th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

import sys


def catalan(num: int):
    # base case
    if num == 0 or num == 1:
        return 1
    if num < 0:
        return None

    result = 0
    for i in range(num):
        result += catalan(i) * catalan(num - i - 1)

    return result


argument = int(sys.argv[1])

print(catalan(argument))
