import matplotlib.pyplot as plt


ele_x=[]
ele_z=[]

oct_x =[]
oct_z = []

str_x =[]
str_z =[]

str_x.append(0.005)
str_x.append(0.01)
str_x.append(0.02)
str_x.append(0.05)

str_z.append(58166)
str_z.append(14519)
str_z.append(3529)
str_z.append(610)

ele_z.append(61127)
ele_z.append(15539)
ele_z.append(4035)
ele_z.append(678)

oct_z.append(182890)
oct_z.append(37776)
oct_z.append(7403)
oct_z.append(1091)

plt.gcf().clear()
fig = plt.figure(1)
ax = fig.add_subplot(111)

ax.plot(str_x, str_z ,color='r',marker='x',label='Stairway mapping 182890')
ax.plot(str_x, ele_z ,color='b',marker='s',label='Elevation mapping',markersize=3)
ax.plot(str_x, oct_z ,color='g',marker='o',label='Octomap')

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5)
text = ax.text(-0.2,1.05, "Pointsize", transform=ax.transAxes)
text2 = ax.text(0.8,-0.1,"Mapping resolution [m]",transform=ax.transAxes)
plt.xlim(0,0.055)
plt.ylim(0,183000)
# ax.set_title("Trigonometry")
ax.grid('on')
fig.savefig('samplefigure', bbox_extra_artists=(lgd,text,text2), bbox_inches='tight')