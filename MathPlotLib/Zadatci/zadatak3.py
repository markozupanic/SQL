#Generirajte 100 slučajnih cjelobrojnih brojeva u rasponu [1, 10]. Prikažite histogram generiranih
#brojeva.
#Za generiranje cjelobrojnih brojeva možete koristiti Numpy funkciju np.random.randint().
import numpy as np
import matplotlib.pyplot as plt

random_brojevi=np.random.randint(1,11,size=100)

plt.hist(random_brojevi,bins=10,range=(1,11))
plt.title("Histogram random brojeva")
plt.show()
































