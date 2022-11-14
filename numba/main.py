#!/bin/python3

from numba import njit


@njit
def calc(max_number: int):
    x = max_number
    while True:
        i = 2
        while i <= max_number:
            if x % i: break
            i += 1
        else:
            # x was not divisible by 2...20
            break
        x += 1
    return x


def main():
    from datetime import datetime
    start_time = datetime.now()
    x = calc(20)
    print(f"Answer: {x}")
    print(f"Time taken: {(datetime.now() - start_time).total_seconds():.5f} seconds")


if __name__ == '__main__':
    main()
