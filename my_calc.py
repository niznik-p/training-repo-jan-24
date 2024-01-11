import numpy as np

x_len = int(input('How many arrays of 100? '))  # Not the best error handling!
y_len = 100
a = np.random.randint(1, 100, [x_len, y_len])

for i in range(0, x_len):
    print(a[i].mean())
