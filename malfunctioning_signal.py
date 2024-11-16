import pywt
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 10, 10000)

def signal(t):
    if 0 <= t <= 5:
        return np.sin(2 * np.pi * t)
    elif 5 <= t <= 6:
        return np.sin(4 * np.pi * t)
    else:
        return np.sin(8 * np.pi * t)


# x = np.linspace(0, 10, 10000)
# y = fft([signal(t) for t in x])
# freqs = fftfreq(len(x), x[1] - x[0])
# plt.plot(freqs, np.abs(y), color='red')
# plt.xlabel("Frequency")
# plt.ylabel("Magnitude")
# plt.xlim(-10, 10)
# plt.show()

# x_red = np.linspace(0, 5, 5000)
# x_yellow = np.linspace(5, 6, 4000)
# x_green = np.linspace(6, 10, 1000)
# y_red = np.array([signal(t) for t in x_red])
# y_yellow = np.array([signal(t) for t in x_yellow])
# y_green = np.array([signal(t) for t in x_green])
#
# plt.plot(x_red, y_red, color='red')
# plt.plot(x_green, y_green, color='green')
# plt.plot(x_yellow, y_yellow, color='yellow')
# plt.xticks([])
# plt.yticks([])
# plt.show()

# # Perform CWT
scales = np.geomspace(128, 1536, num=100)
x_vals = [signal(t) for t in time]
wavelet = 'cmor1.5-1.0'
sampling_period = np.diff(time).mean()
coef, freqs = pywt.cwt(x_vals, scales, wavelet, sampling_period=sampling_period)
coef = np.abs(coef[:-1, :-1])

# Plot the CWT
fig, axs = plt.subplots(1, 1)
pcm = axs.pcolormesh(time, freqs, coef)
axs.set_yscale("log", base=2)
axs.set_xlabel("Time (s)")
axs.set_ylabel("Frequency (Hz)")
axs.set_title("Wavelet Transform of Malfunctioning Signal")
fig.colorbar(pcm, ax=axs)
plt.show()
