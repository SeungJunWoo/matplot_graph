
import numpy as np
import matplotlib.pyplot as plt

objects = ('0', '1', '2', '3', '4', '5','6','7','8','9','10','11','12')
y_pos = np.arange(len(objects))
height = []
height.append(35)
height.append(212)
height.append(291)
height.append(284)
height.append(276)
height.append(345)
height.append(322)
height.append(299)
height.append(297)
height.append(292)
height.append(271)
height.append(283)
height.append(318)

plt.gcf().clear()
fig = plt.figure(1)
ax = fig.add_subplot(111)

ax.bar(y_pos, height, align='center', alpha=0.5,width=0.5)
plt.xticks(y_pos, objects)

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5)
text = ax.text(-0.2,1.05, "Number of classified planes", transform=ax.transAxes)
text2 = ax.text(0.8,-0.1,"Stair number",transform=ax.transAxes)
# ax.grid('on')
fig.savefig('samplefigure', bbox_extra_artists=(lgd,text,text2), bbox_inches='tight')
