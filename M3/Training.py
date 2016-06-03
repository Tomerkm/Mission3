import matplotlib.transforms as mtransforms
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.parasite_axes import SubplotHost


#fig = plt.figure()
#
#ax_kms = SubplotHost(fig, 1, 1, 1, aspect=1.)
#
#fig.add_subplot(ax_kms)
#
#
#
#
#ax_kms.set_xlim(0, 3000)
#ax_kms.set_ylim(0, 3000)
## xlim and ylim of ax_pms will be automatically adjusted.
#
#plt.grid(True)
#plt.draw()
#plt.show()

import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image

fig, ax = plt.subplots()

image = np.random.uniform(size=(1000, 1000))


img_artist=ax.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax.set_title('dropped spines')

# Move left and bottom spines outward by 10 points
ax.spines['left'].set_position(('outward', 20))
ax.spines['bottom'].set_position(('outward', 20))
# Hide the right and top spines
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
# Only show ticks on the left and bottom spines

ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

image[5][5]=1

plt.plot(5,5,'rx', markeredgewidth=3, markersize=10)


print img_artist.cmap(img_artist.norm(image))
       



# get the color at pixel 5,5 (use normalization and colormap)
#print img_artist.cmap(img_artist.norm(image[5,5]))


print "END"

plt.axis('image')
plt.show()


#i=0
#while i<1000:
#    j=0
#    while j<1000:
#        
#        if 100*img_artist.cmap(img_artist.norm(image[i][j]))[0]==255:
#            print True
#        j+=1
#    i+=1


#i=0
#while i<1000:
#
#    plt.scatter(i,999,s=500,color="Black",linewidth='0') 
#    plt.scatter(999,i,s=500,color="Black",linewidth='0') 
#    plt.scatter(i,0,s=500,color="Black",linewidth='0') 
#    plt.scatter(0,i,s=500,color="Black",linewidth='0') 
#    count=random.randint(1,10)
#    Color="white"
#    if count>2 and count<6 :
#        Color="grey"
#    elif count>=1 and count<=2:
#        Color="black"
#      
#    plt.scatter(i, i,s=300,color=Color,linewidth='0')     
#     
#    
#    i+=1




plt.grid(True)
plt.show()



