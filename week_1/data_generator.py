import math
import sys
import numpy as np
import argparse

def generate(n):
    """
    Generate data based on function -- f(X) = sin(2*pi*x)
    @param n: number of data to be generated
    @return: list of numbers
    """
    initial_data = np.random.random(n) # Generate random data between 0 and 1
    return [math.sin(2*math.pi*i) + np.random.randn() for i in initial_data]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument("--n")

    count = 10
    args = parser.parse_args()
    if args.n:
        count = int(args.n)
    numbers = generate(count)
    print('Generated Data for {} numbers: {}'.format(count, numbers))