import numpy as np
import matplotlib.pyplot as plt
import math as m

N=300
B= 0.0024
A= 0.003
w =(220*m.pi)/3
# Number of turns in the coil
# Area of the coil in square meters (e-g-, 10cm x 10cm)
# Strength of the magnetic field in Tesla (T)
# Angular frequency in radians per second (determines rotation speed)
t = np.linspace(0, 2, 1000)
E_max = (N * A * B * w)
E_ac = (E_max * np.sin(w * t)) * 0.1096 # Efficiency calculated is 10.96%
E_max_printed = E_max * 0.1096 # Adjusted maximum voltage for efficiency

E_dc = np.abs(E_ac) # Rectified DC voltage
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(t, E_dc, color='r', linewidth=2)
ax.set_title( 'Generated Voltage: Rectified Direct Current (DC)')
ax.set_xlabel('Time (t) [seconds]')
ax.set_ylabel('Voltage (E) [Volts]')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
print("Number of turns in the coil (N):", N)
print("Area of the coil (A):", A, "m^2")
print("Strength of the magnetic field (B):", B, "T")
print("Angular frequency (w):", w, "rad/s")
print("Maximum induced voltage (E_max):", E_max_printed, "V")