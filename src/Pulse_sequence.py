import numpy as np
import matplotlib.pyplot as plt

# Constants
gamma_hydrogen = 42.57747892e6  # Gyromagnetic ratio for hydrogen-1 in rad/s/T
B0 = 1  # Magnetic field strength in Tesla
pulse_width = 18e-6  # Pulse width in seconds
pulse_separation = 1e-3  # Pulse separation in seconds

# Function to apply a pi/2 pulse
def apply_pi_2_pulse(M):
    # Rotation matrix for pi/2 pulse around y-axis
    R_y_pi_2 = np.array([[np.cos(np.pi/2), 0, np.sin(np.pi/2)],
                         [0, 1, 0],
                         [-np.sin(np.pi/2), 0, np.cos(np.pi/2)]])
    return np.dot(R_y_pi_2, M)

# Initial magnetization aligned along z-axis
M0 = np.array([0, 0, 1])

# Apply pi/2 pulse
M_after_pulse = apply_pi_2_pulse(M0)

# Visualize the effect of the pi/2 pulse
plt.figure(figsize=(10, 6))
plt.quiver(0, 0, M0[0], M0[2], angles='xy', scale_units='xy', scale=1, color='r', label='Before Pulse')
plt.quiver(0, 0, M_after_pulse[0], M_after_pulse[2], angles='xy', scale_units='xy', scale=1, color='g', label='After Pulse')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel('Mx')
plt.ylabel('Mz')
plt.title('Effect of a π/2 Pulse on Magnetization')
plt.legend()
plt.grid(True)
plt.show()
