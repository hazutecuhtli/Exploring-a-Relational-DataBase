#************************************************************************************************
#Importing libraries
#************************************************************************************************
import numpy as np
import matplotlib.pyplot as plt
#************************************************************************************************
#Functions
#************************************************************************************************

def PlottingResults(labels,titles,vals1,vals2=0,vals3=0,ax2p=0,ax3p=0,legends='',w=.35,fsize=(10,6),rot=0):

    '''
    Function to visualize query results for the dvdrental database

    Inputs:
    labels --> List of labels defining the xtick labels
    titles --> List composed by strings that define the title, ylabel and secondary ylabel titles
    vals1 --> List of first values related to the query results to plot
    vals2 --> List of second values related to the query results to plot
    vals3 --> List of third values related to the query results to plot
    ax2p --> Flag to display the y values of the vals2 values in the secondary axis
    ax3p --> Flag to display the y values of the vals3 values in the secondary axis
    legends --> List composed by strings  that define the legends for the plotted values
    w --> Width for the bars to plot
    fsize --> tupple that defines the figure size for plotting the query results
    rot --> rotation for the x labels (xticks labels)
    '''
        
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    c1 = 'royalblue'
    c2 = 'darkorange'
    c3 = 'lightsteelblue'
    
    fig, ax = plt.subplots(figsize=fsize)
    bars1 = ax.bar(x - width, vals1, width, color=c1, label=legends[0])
    
    if vals2 != 0:
        if ax2p != 0:
            ax2 = ax.twinx()
        else:
            ax2=ax
        bars2 = ax2.bar(x, vals2, width, color=c2, label=legends[1])

    if vals3 != 0:
        if ax3p != 0:
            ax2 = ax.twinx()
        else:
            ax2=ax
        bars3 = ax2.bar(x + width-.1, vals3, width, color=c3, label=legends[2])
                           
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(titles[1], fontsize=14)
    if (ax2p!=0 or ax3p !=0):
        ax2.set_ylabel(titles[2], fontsize=14)
    ax.set_title(titles[0], fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.tick_params(axis ='x', rotation = rot) 
    ax.legend(loc= 'upper center')
    ax2.legend()

    plt.grid(False)
    
#************************************************************************************************
#Fin
#************************************************************************************************