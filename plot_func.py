
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def my_anima_1d_h_u(fig,axs,x,t,h,u,xy_lim=None):
    # fig: figure 
    # x,t: x-axis annd t-axis
    # u: output[x,t]. dimension: x.size x t.size
    # First set up the figure, the axis, and the plot element we want to animate
    if xy_lim is None:
        axs[0].set_xlim([np.min(x),np.max(x)])
        axs[0].set_ylim([np.min(h),np.max(h)*1.1])
        axs[1].set_xlim([np.min(x),np.max(x)])
        axs[1].set_ylim([np.min(u),np.max(u)*1.1])
    else:
        axs[0].set_xlim([xy_lim[0][0],xy_lim[0][1]])
        axs[0].set_ylim([xy_lim[1][0],xy_lim[1][1]]) # h
        axs[1].set_xlim([xy_lim[0][0],xy_lim[0][1]]) 
        axs[1].set_ylim([xy_lim[2][0],xy_lim[2][1]]) # u
        
    line_h,= axs[0].plot([],[],linewidth=2)
    line_u,= axs[1].plot([],[],linewidth=2)
    
    # animation function. This is called sequentially
    def drawframe(i):
        line_h.set_data(x,h[i])
        line_u.set_data(x,u[i])
        fig.suptitle(f"t={t[i]:4.2f}")
        return line_h,line_u
        
    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, drawframe, frames=t.shape[0], interval=200, blit=True)
    plt.close()
    return anim
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
    def drawframe(i,ax1):
        line1d.set_data(x,u[i])
        fig.suptitle(f"t={t[i]:4.2f}")
        return line1d,
        
    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, drawframe, frames=t.shape[0], interval=200, blit=True)
    plt.close()
    return anim
