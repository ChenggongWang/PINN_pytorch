
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
# function for animation
def anima_1d(fig,x,t,u,xy_lim=None):
    # fig: figure 
    # x,t: x-axis annd t-axis
    # u: output[x,t]. dimension: x.size x t.size
    # First set up the figure, the axis, and the plot element we want to animate
    ax1 = fig.add_subplot(111,facecolor=(1.0, 1.0, 1.0))
    if xy_lim is None:
        ax1.set_xlim([np.min(x),np.max(x)])
        ax1.set_ylim([np.min(u),np.max(u)])
    else:
        ax1.set_xlim([xy_lim[1][0],xy_lim[1][1]])
        ax1.set_ylim([xy_lim[0][0],xy_lim[0][1]])
        
    line1d,= ax1.plot([np.min(x),np.max(x)],[0,0],linewidth=0.2)
    
    def init_f():
        line1d.set_data(x,u[0])
        return line1d,
    # animation function. This is called sequentially
    def animate(i,ax1,x,t,u):
        line1d.set_data(x,u[i])
        fig.suptitle(f"t={t[i]:4.2f}")
        return line1d,
        
    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate,fargs=(ax1,x,t,u),init_func=init_f,
                                   frames=t.shape[0], interval=200, blit=True)
    plt.close()
    return anim
