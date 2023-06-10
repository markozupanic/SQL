#Funkcije iz prethodnog zadatka prikažite na dva odvojena grafa.
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 10, 0.1)

sin_values = np.sin(x)
cos_values = np.cos(x)

fig,axes=plt.subplots(2)
fig.suptitle("Dva prikaza")

axes[0].set_title("Sinus")
axes[0].plot(sin_values)
axes[0].set(xlabel="x",ylabel="y")

axes[1].set_title("Cosinus")
axes[1].plot(cos_values)
axes[1].set(xlabel="x",ylabel="y")

plt.legend()
plt.show()

