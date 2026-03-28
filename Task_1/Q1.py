#Nilai minimum suatu fungsi .
from scipy.optimize import minimize
def func(x) :
    return x**2 - 4*x

x0 = [0]
min_val = minimize(func, x0)

xmin = int(min_val.x[0])
ymin = int(func(xmin))

print(f"Min x-value: {xmin}")
print(f"Min y-value: {ymin}")
print(f"The minimum point is {xmin, ymin}")
