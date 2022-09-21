import difffunctions as df

# f(x) = sin(5x) - x^2
f = df.sin(df.x * 5) + -df.x**2

import matplotlib.pyplot as plt

domain = [x/100 for x in range(-200, 200)]
plt.plot(domain, [f(x) for x in domain])


point = 1
grad = f.d(point)
plt.plot([point-1, point+1], [f(point)-grad, f(point) + grad])

plt.show()