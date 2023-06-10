#Prikažite sinus i kosinus vrijednosti u rasponu [0, 10]. Dodjelite odgovarajuće nazive
#koordinatnim osima, te odgovarajući naslov grafa. Prikažite legendu. Obje funkcije prikažite na
#istom grafu.



import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 10, 0.1)

sin_values = np.sin(x)
cos_values = np.cos(x)

plt.plot(x, sin_values, label='sin(x)')
plt.plot(x, cos_values, label='cos(x)')


plt.xlabel('x-os')
plt.ylabel('y-os')
plt.title('Sinus i kosinus funkcije')

plt.legend()

plt.show()


































