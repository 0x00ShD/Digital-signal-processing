import numpy as np
import matplotlib.pyplot as plt

# Generate impulse response h[n]
h = np.zeros(99)
for i in range(99):
    h[i] = 0.31752 * np.sin(0.314159 * (i - 49.00001)) / (i - 49.00001)
    h[i] *= (0.54 - 0.46 * np.cos(0.0641114 * i))

# Plot impulse response h[n]
plt.figure(figsize=(10, 5))
plt.plot(h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('Impulse Response')
plt.grid(True)
plt.show()

# Convolution function
def convolution(x, h):
    x_len = len(x)
    h_len = len(h)
    y_len = x_len + h_len - 1
    y = np.zeros(y_len)
    for n in range(y_len):
        for k in range(h_len):
            if n - k >= 0 and n - k < x_len:
                y[n] += x[n - k] * h[k]
    return y

# Test signal x[n]
x = np.zeros(500)
x[0] = 1

# Convolve h[n] with x[n]
y = convolution(x, h)

# Plot the resulting signal y[n]
plt.figure(figsize=(10, 5))
plt.plot(y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Convolution Output')
plt.grid(True)
plt.show()

# Generate more complicated test signal x[n]
x = np.sin(6 * 2 * np.pi * np.arange(500) / 500) + 0.5 * np.sin(44 * 2 * np.pi * np.arange(500) / 500)

# Plot the more complicated test signal x[n]
plt.figure(figsize=(10, 5))
plt.plot(x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('More Complicated Test Signal')
plt.grid(True)
plt.show()

# Convolve h[n] with the more complicated test signal x[n]
y = convolution(x, h)

# Plot the resulting signal after filtering
plt.figure(figsize=(10, 5))
plt.plot(y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Filtered Signal')
plt.grid(True)
plt.show()

# Comment on the results
print("The filter has passed the lower frequency signal, while blocking the higher frequency signal.")
