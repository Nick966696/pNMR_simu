import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Constants
T1_initial_guess = 1e-3  # Initial guess for T1 in seconds

# Time points for observing relaxation after the π pulse
time_points = np.linspace(0, 0.1, 1000)  # 100 ms, 1000 points

# Relaxation model for T1 (Mz recovery)
def mz_recovery(t, T1):
    return 1 - 2*np.exp(-t/T1)

# Simulated Mz(t) data using the initial guess for T1
mz_data = mz_recovery(time_points, T1_initial_guess)

# Fit the simulated data to the relaxation model to estimate T1
popt, pcov = curve_fit(mz_recovery, time_points, mz_data, p0=[T1_initial_guess])
T1_estimated = popt[0]

print(f"Estimated T1: {T1_estimated} s")

# Plotting the recovery of Mz over time
plt.figure(figsize=(10, 6))
plt.plot(time_points, mz_data, 'b-', label='Simulated Mz(t)')
plt.plot(time_points, mz_recovery(time_points, T1_estimated), 'r--', label='Fitted Recovery Curve')
plt.xlabel('Time (s)')
plt.ylabel('Mz(t)')
plt.title('T1 Relaxation Process and Fitting')
plt.legend()
plt.grid(True)
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
#
# # Constants and Parameters
# T1_initial_guess = 1e-3  # Initial guess for T1 in seconds, for demonstration
# T2_initial_guess = 100e-3  # Initial guess for T2 in seconds, for demonstration
# time_points = np.linspace(0, 0.2, 1000)  # Observation period: 200 ms, 1000 points
#
# # Model for magnetization recovery and decay
# def magnetization_model(t, T1, T2):
#     Mz_recovery = 1 - 2 * np.exp(-t/T1)  # Simplified recovery along z-axis
#     Mxy_decay = np.exp(-t/T2)  # Decay in the xy-plane
#     return Mz_recovery, Mxy_decay
#
# # Generate simulated data based on initial guesses
# Mz_simulated, Mxy_simulated = magnetization_model(time_points, T1_initial_guess, T2_initial_guess)
#
# # Visualization of relaxation processes
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.plot(time_points, Mz_simulated, 'r-', label='Mz Recovery')
# plt.title('Longitudinal Relaxation (T1)')
# plt.xlabel('Time (s)')
# plt.ylabel('Mz(t)')
# plt.grid(True)
# plt.legend()
#
# plt.subplot(1, 2, 2)
# plt.plot(time_points, Mxy_simulated, 'b-', label='Mxy Decay')
# plt.title('Transverse Relaxation (T2)')
# plt.xlabel('Time (s)')
# plt.ylabel('Mxy(t)')
# plt.grid(True)
# plt.legend()
#
# plt.tight_layout()
# plt.show()
