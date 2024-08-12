import numpy as np
import matplotlib.pyplot as plt

# Generate impulse response h[n]
h = np.zeros(99)
for i in range(99):
    h[i] = 0.31752 * np.sin(0.314159 * (i - 49.00001)) / (i - 49.00001)
    h[i] *= 0.54 - 0.46 * np.cos(0.0641114 * i)

# Plot impulse response h[n]
plt.figure()
plt.stem(h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('Impulse Response')
plt.grid(True)
plt.show()

# Convolution function
def convolution(x, h):
    N = len(x) + len(h) - 1
    y = np.convolve(x, h)[:N]
    return y

# Test signal x[n] = 1 for n = 0, x[n] = 0 otherwise
x = np.zeros(500)
x[0] = 1

# Convolve h[n] with x[n]
y = convolution(x, h)

# Print and explain the output
print("Output of convolution:", y)
print("The output of the convolution should be a filtered version of the input signal x[n]. Since the impulse response h[n] acts as a low-pass filter, it passes sinusoids with fewer than 25 cycles in 500 samples and blocks higher-frequency sinusoids. Since x[n] is an impulse, which is a high-frequency signal, the output should be a filtered version of the impulse response h[n] that suppresses high-frequency components.")

# Generate more complicated test signal x[n]
n = np.arange(500)
x = np.sin(6 * 2 * np.pi * n / 500) + 0.5 * np.sin(44 * 2 * np.pi * n / 500)

# Plot test signal x[n]
plt.figure()
plt.plot(n, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Test Signal')
plt.grid(True)
plt.show()

# Convolve h[n] with x[n]
y = convolution(x, h)

# Plot filtered signal y[n]
plt.figure()
plt.plot(y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Filtered Signal')
plt.grid(True)
plt.show()

# Comment on the results
print("The filter has passed the lower frequency sinusoid while blocking the higher frequency sinusoid. This is evident in the filtered signal y[n] where the low-frequency component is preserved, but the high-frequency component is significantly attenuated. The filter successfully separates the different frequency components present in the input signal x[n].")
