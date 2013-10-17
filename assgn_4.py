import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import urllib

def Colormap(name):
    
    url = 'http://geography.uoregon.edu/datagraphics/color/'+name
    
    red = []
    green = []
    blue  =[]
    
    f = urllib.urlopen(url)
    
    for line in f.readlines()[2:]:
        colortable = line.split()
        red.append(float(colortable[0]))
        green.append(float(colortable[1]))
        blue.append(float(colortable[2]))
        
    length = len(red)
    
    '''red0 = [(float(n)/ (length -1),red[n],red[n]) for n in range (length)]
    green0 = [(float(n)/(length-1),green[n],green[n]) for n in range (length)]
    blue0 = [(float(n)/(length -1),blue[n],blue[n]) for n in range (length)]'''
    red0 = [(float(n)/ (length -1),red[n-1],red[n]) for n in range (length)]
    green0 = [(float(n)/(length-1),green[n-1],green[n]) for n in range (length)]
    blue0 = [(float(n)/(length -1),blue[n-1],blue[n]) for n in range (length)]  
    
    cdict ={'red':red0,'green':green0,'blue':blue0}
    
    return matplotlib.colors.LinearSegmentedColormap('my_cmap',cdict,256)
    
if __name__ == '__main__':
    import matplotlib.pyplot
    cmap= Colormap('StepSeq_25.txt')
    plt.pcolor(np.random.rand(10,10),cmap= cmap)
    plt.colorbar()
    plt.show()
    plt.savefig('my_color_map.pdf')
        
    
    
    
    