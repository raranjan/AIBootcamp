import math
import sys
import numpy as np


def generate(n):
    """
    Generate data based on function -- f(X) = sin(2*pi*x)
    @param n: number of data to be generated
    @return: list of numbers
    """
    return [math.sin(2*math.pi*i) - np.random.randn() for i in range(n)]

if __name__ == '__main__':
    count = 10
    if len(sys.argv) > 1:
        count = sys.argv[1]

    numbers = generate(count)
    print('Generated Data for {} numbers: {}'.format(count, numbers))