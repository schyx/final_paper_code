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
        return np.sin(2 * np.pi * t)
    elif 5 <= t <= 9:
        return np.sin(8 * np.pi * t)
    else:
        return np.sin(4 * np.pi * t)


x_red = np.linspace(0, 5, 5000)
x_green = np.linspace(5, 9, 4000)
x_yellow = np.linspace(9, 10, 1000)
y_red = np.array([signal(t) for t in x_red])
y_green = np.array([signal(t) for t in x_green])
y_yellow = np.array([signal(t) for t in x_yellow])

plt.plot(x_red, y_red, color='red')
plt.plot(x_green, y_green, color='green')
plt.plot(x_yellow, y_yellow, color='yellow')
# plt.axhline(0, color='black', lw=0.5, ls='--')
# plt.axvline(0, color='black', lw=0.5, ls='--')
plt.xticks([])
plt.yticks([])
plt.show()

# # Perform CWT
# scales = np.arange(1, 128)
# wavelet = 'morl'
# coef, freqs = pywt.cwt(y_vals, scales, wavelet)
#
# # Plot the CWT
# plt.imshow(coef, extent=[0, 1, 1, 128], cmap='viridis', aspect='auto', interpolation='nearest')
# plt.colorbar(label='CWT Coefficients')
# plt.xlabel('Time')
# plt.ylabel('Scale')
# plt.title('Continuous Wavelet Transform')
# plt.show()
