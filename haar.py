import numpy as np
import matplotlib.pyplot as plt

def haar_wavelet_corrected(t, j, k):
    scale = 2**j
    t_scaled = t * scale - k
    return np.where((t_scaled >= 0) & (t_scaled < 0.5), np.sqrt(scale),
           np.where((t_scaled >= 0.5) & (t_scaled < 1), -np.sqrt(scale), 0))

t_values = np.linspace(-1, 3, 1000)  # Range of t for visualization

scales_updated = [-1, 0, 1]
k = 0 

fig, axs = plt.subplots(1, len(scales_updated), figsize=(15, 4), sharey=True)

for ax, j in zip(axs, scales_updated):
    wavelet_values_corrected = haar_wavelet_corrected(t_values, j, k)
    ax.plot(t_values, wavelet_values_corrected, color="blue")
    ax.set_title(f"j = {j}, k = {k}")
    ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
    ax.grid(True)
    ax.set_xlabel("t")

fig.suptitle("Haar Wavelet at Different Scales (j = -1, 0, 1) and Translation k = 0")
axs[0].set_ylabel(r"$\psi_{j,k}(t)$")
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.savefig('bryant_figures/harr.png', dpi=150, bbox_inches='tight')  # You can use .png, .jpg, .pdf, etc.
