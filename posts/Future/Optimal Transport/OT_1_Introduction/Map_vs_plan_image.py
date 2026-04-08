import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Parameters
n_points = 500
x_range = np.linspace(-3, 3, 200)
y_range = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x_range, y_range)

# 1. Independent Product Plan: gamma = mu x nu
# mu = N(0, 1), nu = N(0, 1)
pos = np.dstack((X, Y))
rv = multivariate_normal([0, 0], [[1, 0], [0, 1]])
Z_indep = rv.pdf(pos)

# 2. Monge Map Plan: T(x) = -x
# The measure is concentrated on the graph (x, -x)
# To visualize this, we approximate the Dirac delta with a narrow ridge
epsilon = 0.05  # thickness of the ridge
Z_map = np.exp(-(Y + X)**2 / (2 * epsilon**2)) / (np.sqrt(2 * np.pi) * epsilon)
# Multiply by marginal density to keep it localized
Z_map *= np.exp(-X**2 / 2) / np.sqrt(2 * np.pi)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot Independent Product
im1 = ax1.contourf(X, Y, Z_indep, levels=20, cmap='Blues')
ax1.set_title(r'Kantorovich Plan: Independent Product $\mu \otimes \nu$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.axhline(0, color='black', lw=1, alpha=0.3)
ax1.axvline(0, color='black', lw=1, alpha=0.3)

# Plot Monge Map
im2 = ax2.contourf(X, Y, Z_map, levels=20, cmap='Reds')
ax2.set_title(r'Monge Map: $\gamma = (Id, T)_\# \mu$ with $T(x)=-x$')
ax2.set_xlabel('$x$')
ax2.set_ylabel('$y$')
ax2.axhline(0, color='black', lw=1, alpha=0.3)
ax2.axvline(0, color='black', lw=1, alpha=0.3)

plt.tight_layout()
plt.show()