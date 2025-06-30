import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm_y, lpmv, spherical_jn, spherical_yn

mu0 = 1.25 * 1e-6
m = 3.0
omega = 1e6
epsilon = 1e-12
sigma = 0.1
k = np.sqrt(1j * omega * mu0 * (sigma - 1j * omega * epsilon))

q = 5
x = np.linspace(-q, q, 100)
z = np.linspace(-q, q, 100)
X, Z = np.meshgrid(x, z)
r = np.sqrt(X ** 2 + Z ** 2)
theta = np.arctan2(np.abs(X), Z)
phi = np.arctan2(X, Z)
phi = np.mod(phi, 2 * np.pi)

A_inhom = (mu0 * m / (4 * np.pi * r ** 2)) * np.exp(1j * k * r) * (
            (1j * k * r - 1) * (-np.sin(theta) * np.sin(phi) - np.sin(phi)))

l = 1

C = 0.1 * mu0
C2 = epsilon
hl = spherical_jn(l, k * r)
h2l = spherical_yn(l, k * r)
P11 = -lpmv(1, l, np.cos(theta))
Y11 = sph_harm_y(1, l, phi, theta)
A_hom = (C * hl + C2 * h2l) * P11 * np.imag(Y11) * np.exp(1j * m * phi)

A = A_inhom + A_hom

plt.figure(figsize=(8, 6))
plt.imshow(np.abs(A), extent=(-q, q, -q, q), cmap='hot')
plt.colorbar(label='A')
plt.xlabel('x (м)')
plt.ylabel('z (м)')
plt.show()
