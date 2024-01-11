import numpy as np

x_len = 5
y_len = 100
a = np.random.randint(1, 100, [x_len, y_len])

for i in range(0, 5):
    print(a[i].mean())
