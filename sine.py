import numpy as np
import matplotlib.pyplot as plt
 
x = np.arange(-3, 3, 0.1)
y = np.sin(x)*2
  
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Title')
plt.show()