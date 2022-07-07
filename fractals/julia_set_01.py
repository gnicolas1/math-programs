# Julia Set 
# f(z) = z^2 + c
# if |f(z)| > 2, then z diverges

import matplotlib.pyplot as plt
import numpy as np

max = 500

xx = np.linspace(-2, 2, 1000)

x, y = np.meshgrid(xx, xx)
z = x + y*1j
c = np.complex(0.2359, -0.8871)
# (0.2359, -0.8871)
# (-0.023, 0.72112)
#(-0.63108, 0.1132)
i = 0
while i < max:
    z = np.where(abs(pow(z, 2) + c) < 2, pow(z, 2) + c, z)  
    i += 1

plt.figure()
plt.contourf(x, y, abs(z), 255, cmap='hot')
plt.colorbar()
plt.show()
