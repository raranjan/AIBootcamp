import random
import math

"""
To approximate sqrt of i, lets assume i = x^2 and we need to find x as close to actual as possible
therefore, x^2 - i = f(x) = y
As per newton menthod, new_x = x - f(x)/f'(x)
Which simplifies to: new_x = x - (x^2 - 1)/(2*x)
"""

def approx_sqrt(num):
    epoch = 10
    x = random.randint(1, num)

    for i in range(epoch):
        x_new = x - (x**2 - num)/(2*x)

        print("Square root for {} --> {}".format(num, x_new))
        difference = math.fabs(x_new - x)
        print("Difference from previous --> {}".format(difference))

        x = x_new


if __name__ == '__main__':
    approx_sqrt(3)