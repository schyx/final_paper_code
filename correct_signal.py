import pywt
from scipy.fft import fft, fftfreq
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
    if t <= 5:
        return np.sin(2 * np.pi * t)
    elif 5 <= t <= 9:
        return np.sin(8 * np.pi * t)
    else:
        return np.sin(4 * np.pi * t)


# x = np.linspace(0, 10, 10000)
# y = fft([signal(t) for t in x])
# freqs = fftfreq(len(x), x[1] - x[0])
# plt.plot(freqs, np.abs(y), color='blue')
# plt.xlabel("Frequency")
# plt.ylabel("Magnitude")
# plt.xlim(-10, 10)
# plt.show()


# x_red = np.linspace(0, 5, 5000)
# x_green = np.linspace(5, 9, 4000)
# x_yellow = np.linspace(9, 10, 1000)
# y_red = np.array([signal(t) for t in x_red])
# y_green = np.array([signal(t) for t in x_green])
# y_yellow = np.array([signal(t) for t in x_yellow])
#
# plt.plot(x_red, y_red, color='red')
# plt.plot(x_green, y_green, color='green')
# plt.plot(x_yellow, y_yellow, color='yellow')
# # plt.axhline(0, color='black', lw=0.5, ls='--')
# # plt.axvline(0, color='black', lw=0.5, ls='--')
# plt.xticks([])
# plt.yticks([])
# plt.show()

# # Perform CWT
scales = np.arange(1, 128)
x_vals = [signal(t) for t in np.linspace(0, 10, 10000)]
wavelet = 'cmor1.5-1.0'
coef, freqs = pywt.cwt(x_vals, scales, wavelet, sampling_period=10)
coef = np.abs(coef[:-1, :-1])

# Plot the CWT
plt.imshow(coef, extent=[0, 10, 1, 128], cmap='viridis', aspect='auto', interpolation='nearest')
plt.colorbar(label='CWT Coefficients')
plt.xlabel('Time')
plt.ylabel('Scale')
plt.title('Continuous Wavelet Transform')
plt.show()
