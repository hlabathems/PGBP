import numpy as np
import sys

def f(x):
    return x - 6 + np.sin(x)

left = 6
right = 7

epsilon = 0.1

iter = 1

while True:
    
    if f(left) * f(right) < 0:
        
        interval = np.array([left, right])
        mid = np.average(interval)
        max_error = 0.5 * np.diff(interval)[0]
        
        if max_error > epsilon:
            if f(mid) * f(right) < 0:
                left = mid
            else:
                if f(left) * f(mid) < 0:
                    right = mid
        else:
            print(mid, max_error, iter)
            sys.exit()
        
        iter += 1

    else:
        sys.exit('Sorry, you can\'t use bisection method')
