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

str_z.append(0.00270779)
str_z.append(0.00323069)
str_z.append(0.00314846)
str_z.append(0.0032696)

ele_z.append(0.00819196)
ele_z.append(0.00881029)
ele_z.append(0.00992813)
ele_z.append(0.0123339)

oct_z.append(0.0178142)
oct_z.append(0.0306776)
oct_z.append(0.0293774)
oct_z.append(0.0390261)

plt.gcf().clear()
fig = plt.figure(1)
ax = fig.add_subplot(111)

ax.plot(str_x, str_z ,color='r',marker='x',label='Stairway mapping')
ax.plot(str_x, ele_z ,color='b',marker='s',label='Elevation mapping')
ax.plot(str_x, oct_z ,color='g',marker='o',label='Octomap')

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5)
text = ax.text(-0.2,1.05, "Mapping error [m]", transform=ax.transAxes)
text2 = ax.text(0.8,-0.1,"Mapping resolution [m]",transform=ax.transAxes)
plt.xlim(0,0.055)
# ax.set_title("Trigonometry")
ax.grid('on')
fig.savefig('samplefigure1', bbox_extra_artists=(lgd,text,text2), bbox_inches='tight')