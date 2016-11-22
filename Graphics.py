import matplotlib
import pylab
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation
import numpy as np

N = 100

f = open('text.txt', 'r')
with open("text.txt") as file:
    array = [row.strip() for row in file]
f.close()


cmas=np.random.sample((2, 30))

fig = plt.figure()   # list object Figure
print (fig.axes)   
print (type(fig))

circle1 = matplotlib.patches.Circle((0, 0), radius=1)
pylab.show()

class graphs:
      x=np.arange(-10, 10.01, 0.01)
      t=np.arange(-10,10,100)
      #plt.plot(x,np.cos(x),x,-x)
#subplot 1
      plt.subplot(221)     
      z = np.random.gamma(2., 1., N)
      c = np.array([[1, 0.2, 3], [4, 5, 6]])
      y=z.reshape(10,10)
      cf=plt.contourf(c)
      plt.colorbar(cf)
      plt.grid(True)
      plt.title(r'$\cos(x)$')
      fig.get_size_inches()
      fig.get_dpi() 
      plt.savefig('plot16.pdf')
#subplot 2
      
      plt.subplot(223)
      plt.plot(x,np.sin(x),color='green', linewidth=4.0)
      plt.grid(True)
      plt.title(r'$\sin(x)$')
      plt.xlabel(r'$x$')
      plt.ylabel(r'$f(x)$')

#subplot 3
      plt.subplot(222)
      plt.plot(x,np.exp(x)*np.sin(x),color='red', linewidth=4.0)
      plt.grid(True)
      plt.title(r'$\sin(x)$')
      plt.xlabel(r'$x$')
      plt.ylabel(r'$f(x)$')

#subplot 4
    
      #plt.show()

def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, np.cos(2*np.pi*t) * np.exp(-t/10.)


def init():
    plt.subplot(224)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()
