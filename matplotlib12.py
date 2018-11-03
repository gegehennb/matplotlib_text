import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec

# plt.figure()

# plt.subplot(2,1,1)
# plt.plot([0,1],[0,1])

# plt.subplot(2,3,4)
# plt.plot([0,1],[0,2])

# plt.subplot(2,3,5)
# plt.plot([0,1],[0,3])

# plt.subplot(2,3,6)
# plt.plot([0,1],[0,4])

#method 1 : subplot2grid 
# plt.figure()
# ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# ax1.plot([1,2],[1,2])
# ax1.set_title("ax1_title")

# ax2=plt.subplot2grid((3,3),(1,0),colspan=2)
# ax3=plt.subplot2grid((3,3),(1,2),rowspan=2)
# ax4=plt.subplot2grid((3,3),(2,0))
# ax4=plt.subplot2grid((3,3),(2,1))

#method 1 : gridspec
# plt.figure()
# gs=gridspec.GridSpec(3,3)
# ax1=plt.subplot(gs[0,:])
# ax2=plt.subplot(gs[1,:2])
# ax3=plt.subplot(gs[1:,2])
# ax4=plt.subplot(gs[-1,0])
# ax5=plt.subplot(gs[-1,-2])

#method3:easy to define structure

f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])

plt.show()