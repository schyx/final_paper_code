import pywt
import numpy as np
import matplotlib.pyplot as plt

# Create a sample signal
# t_red = np.linspace(0, 5, num=500)
# t_yellow = np.linspace(5, 6, num=100)
# t_green = np.linspace(6, 10, num=400)
# signal = np.sin(np.pi * t_red) + \
#     np.sin(2 * np.pi * t_yellow) + \
#     np.sin(4 * np.pi * t_green)


def signal(t):
    if 0 <= t <= 5:
        return np.sin(np.pi * t)
    elif 5 <= t <= 6:
        return np.sin(2 * np.pi * t)
    else:
        return np.sin(4 * np.pi * t)


x_vals = np.linspace(0, 10, 10000)
y_vals = np.array([signal(t) for t in x_vals])

plt.plot(x_vals, y_vals, label='Piecewise Function', color='blue')
plt.title('Piecewise Function Plot')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

# Perform CWT
# scales = np.arange(1, 128)
# wavelet = 'morl'
# coef, freqs = pywt.cwt(signal, scales, wavelet)
#
# # Plot the CWT
# plt.imshow(coef, extent=[0, 1, 1, 128], cmap='viridis', aspect='auto', interpolation='nearest')
# plt.colorbar(label='CWT Coefficients')
# plt.xlabel('Time')
# plt.ylabel('Scale')
# plt.title('Continuous Wavelet Transform')
# plt.show()
