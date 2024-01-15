import matplotlib.pyplot as plt
import numpy as np

sine1 = 0.63
sine2 = 0.17
sine3 = 0.10
sine4 = 0.03
sine5 = 0.04
sine7 = 0.04

sine_x = np.linspace(0, 2 * np.pi, 2048)

sine1_y = sine1 * np.sin(sine_x)
sine2_y = sine2 * np.sin(2 * sine_x)
sine3_y = sine3 * np.sin(3 * sine_x)
sine4_y = sine4 * np.sin(4 * sine_x)
sine5_y = sine5 * np.sin(5 * sine_x)
sine7_y = sine7 * np.sin(7 * sine_x)

sine_y = sine1_y + sine2_y + sine3_y + sine4_y + sine5_y + sine7_y

sine_y = np.round(sine_y * (127 / max(sine_y)))

plt.plot(sine_x, sine_y)
plt.show()