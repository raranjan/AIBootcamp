import math
import sys
import numpy as np

def generate(n):
    return [math.sin(2*math.pi*i) - np.random.randn() for i in range(n)]

if __name__ == '__main__':
    count = 10
    if len(sys.argv) > 1:
        count = sys.argv[1]

    numbers = generate(count)
    print('Generated Data for {} numbers: {}'.format(count, numbers))