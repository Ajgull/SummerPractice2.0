import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lpmv, spherical_jn, spherical_yn, sph_harm_y

mu0 = 1.25e-6
m = 3.0
omega = 1e6
epsilon = 1e-12
sigma = 0.1
k = np.sqrt(1j * omega * mu0 * (sigma - 1j * omega * epsilon))

q = 5
N = 100
x = np.linspace(-q, q, N)
z = np.linspace(-q, q, N)
X, Z = np.meshgrid(x, z)
r = np.sqrt(X ** 2 + Z ** 2)
theta = np.arctan2(np.abs(X), Z)
phi = np.arctan2(X, Z)
phi = np.mod(phi, 2 * np.pi)

l = 1
C = 0.1 * mu0
C2 = epsilon
hl = spherical_jn(l, k * r)
h2l = spherical_yn(l, k * r)
P11 = lpmv(1, l, np.cos(theta))
Y11 = sph_harm_y(1, l, phi, theta)
A_hom = (C * hl + C2 * h2l) * P11 * np.real(Y11) * np.exp(1j * m * phi)

A_r = 0
A_theta = mu0 * m / (4 * np.pi * r ** 2) * np.exp(1j * k * r) * (1j * k * r - 1) * (-np.sin(phi) * np.sin(theta))
A_phi = mu0 * m / (4 * np.pi * r ** 2) * np.exp(1j * k * r) * (1j * k * r - 1) * (-np.sin(phi) * np.cos(theta))

A_theta += A_hom.real
A_phi += 0

phi = 0
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)
sin_phi = np.sin(phi)
cos_phi = np.cos(phi)

A_x = A_r * sin_theta * cos_phi + A_theta * cos_theta * cos_phi - A_phi * sin_phi
A_y = A_r * sin_theta * sin_phi + A_theta * cos_theta * sin_phi + A_phi * cos_phi
A_z = A_r * cos_theta - A_theta * sin_theta

E_x = 1j * omega * A_x
E_y = 1j * omega * A_y
E_z = 1j * omega * A_z

Ex = np.real(E_x)
Ez = np.real(E_z)
magnitude_E = np.sqrt(Ex ** 2 + Ez ** 2) + 1e-20
Ex_norm = Ex / magnitude_E
Ez_norm = Ez / magnitude_E

magnitude_A = np.sqrt(np.abs(A_x) ** 2 + np.abs(A_y) ** 2 + np.abs(A_z) ** 2)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.imshow(magnitude_A, extent=(-q, q, -q, q), origin='lower', cmap='hot')
plt.colorbar(label='|A| (Вб/м)')
plt.xlabel('x (м)')
plt.ylabel('z (м)')
plt.title('Модуль векторного потенциала A')

plt.subplot(1, 2, 2)
plt.quiver(X, Z, Ex_norm, Ez_norm, magnitude_E, cmap='inferno', scale=50)
plt.xlabel('x (м)')
plt.ylabel('z (м)')
plt.title('Векторное поле E')
plt.colorbar(label='E В/м')
plt.axis('equal')

plt.tight_layout()
plt.show()
