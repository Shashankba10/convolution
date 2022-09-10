#linear convolution
import numpy as np
import matplotlib.pyplot as plt

xn=eval(input("enter the x(n) sequence:"))   #x(n) input

# ploting  of x
plt.subplot(2,2,1)
n=np.arange(0,len(xn),1)
plt.stem(n,xn,"r")
plt.show
plt.grid()
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("x(n) sequence")


hn=eval(input("enter the h(n) sequence"))

# ploting  of y
plt.subplot(2,2,2)
n=np.arange(0,len(hn),1)
plt.stem(n,hn,"b")
plt.show
plt.grid()
plt.xlabel("n")
plt.ylabel("h(n)")
plt.title("h(n) sequence")


y=np.convolve(xn,hn)
plt.subplot(2,2,3)
n=np.arange(0,len(y),1)
plt.stem(n,y,"g")
plt.show
plt.grid()
plt.xlabel("n")
plt.ylabel("y")
plt.title("convilution sequence")
print("linear convolution of x(n) and h(n) is:",y)
