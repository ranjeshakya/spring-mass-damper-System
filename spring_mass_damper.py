import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step, bode,  impulse

###### parameters  #########



m = 1.0  # mass in kg
b = 2.0   # dmaping coefficint  in N/m/sec
k = 5.0 # spring const (N/m)

##### transfer function 1/(ms^2+bs+k)

num2 = [1]
den2 = [m ,b ,k]

H = TransferFunction(num2,den2)

### time vector in simulatiom  ######


t = np.linspace(0,10,1000)
t_step, x_step = step(H, T=t)

# Impulse response
t_impulse, x_impulse = impulse(H, T=t)


# Bode plot
w, mag, phase = bode(H)

# Plotting
plt.figure(figsize=(12, 10))

# Step Response
plt.subplot(3, 1, 1)
plt.plot(t_step, x_step, label='Step Response', color='blue')
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)


# Impulse Response
plt.subplot(3, 1, 2)
plt.plot(t_impulse, x_impulse, label='Impulse Response', color='green')
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)

# Bode Plot
plt.subplot(3, 2, 5)
plt.semilogx(w, mag, label='Magnitude')
plt.title('Bode Plot - Magnitude')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(3, 2, 6)
plt.semilogx(w, phase, label='Phase', color='orange')
plt.title('Bode Plot - Phase')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.grid(True)

plt.tight_layout()
plt.show()