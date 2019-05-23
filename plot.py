import numpy as np
import matplotlib.pyplot as plt


#Leapfrog

datos1 = np.loadtxt("datos.dat")


plt.subplot(3,3,3)
plt.plot(datos1[:,1],datos1[:,2])
plt.xlabel("tiempo")
plt.ylabel("y(x)")
plt.title("Leapfrog")
plt.savefig("CardonaCarlos_final_15.pdf")

