import numpy as np
import matplotlib.pyplot as plt

# Constants
gamma_hydrogen = 42.57747892e6  # Gyromagnetic ratio for hydrogen-1 in rad/s/T
B0 = 1  # Magnetic field strength in Tesla (example value)

# Calculate the Larmor frequency
omega_L = gamma_hydrogen * B0

print(f"Larmor Frequency: {omega_L} rad/s")

# Simulation parameters
time = np.linspace(0, 1, 1000)  # Time array from 0 to 1 second, 1000 points

# Simulate Larmor precession
# Assuming the initial magnetization is aligned along the z-axis (M0 = [0, 0, 1])
M0 = np.array([0, 0, 1])
# Rotation matrix around y-axis to simulate the effect of B0
theta = omega_L * time
Mx = M0[0] * np.cos(theta) - M0[2] * np.sin(theta)
Mz = M0[0] * np.sin(theta) + M0[2] * np.cos(theta)



plt.figure(figsize=(10, 6))
plt.plot(time, Mx, label='Mx(t)')
plt.plot(time, Mz, label='Mz(t)')
plt.xlabel('Time (s)')
plt.ylabel('Magnetization')
plt.title('Larmor Precession of Hydrogen-1 Nuclei')
plt.legend()
plt.grid(True)
plt.show()
