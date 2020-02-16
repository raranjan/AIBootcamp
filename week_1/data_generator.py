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

def generate_with_np(n=10):
    # Get equally spaced numbers using numpy
    numbers = np.linspace(0, 1, n)

    # Generate data based on formula
    data = formula(numbers)

    # Add noise to the data
    data = data + noise(n)

    return data

def formula(X):
    return np.sin(2*np.pi*X)

def noise(n):
    return np.random.normal(0, 1, n)

def main():
    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument("--n")

    count = 10
    args = parser.parse_args()
    if args.n:
        count = int(args.n)
    numbers = generate_with_np(count)
    print('Generated Data for {} numbers: {}'.format(count, numbers))
    
    generate_with_np()

if __name__ == '__main__':
    main()