#!/usr/bin/env python3


def print_fibonacci(length):
    counter = length - 2
    fibonacci_list = list([0, 1])
    if counter < 0:
        for i in range(abs(counter)):
            fibonacci_list.pop()
    while counter > 0:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
        counter -= 1
    print(fibonacci_list)


print_fibonacci(9)
