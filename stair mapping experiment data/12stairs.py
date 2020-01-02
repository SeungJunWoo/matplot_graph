
import numpy as np
import matplotlib.pyplot as plt

objects = ('0','1', '2', '3', '4', '5','6','7','8','9','10','11','12')
y_pos = np.arange(len(objects))
height = []

#### measurement
mmd_0 = 0.646806
mmd_1 = 0.470697
mmd_2 = 0.296156
mmd_3 = 0.120918
mmd_4 = -0.0573376
mmd_5 = -0.239803
mmd_6 = -0.40261
mmd_7 = -0.588489
mmd_8 = -0.759553
mmd_9 = -0.951465
mmd_10 = -1.13551
mmd_11 = -1.29849
mmd_12 = -1.48371

# height.append(mmd_0 - mmd_1)
# height.append(mmd_1 - mmd_2)
# height.append(mmd_2 - mmd_3)
# height.append(mmd_3 - mmd_4)
# height.append(mmd_4 - mmd_5)
# height.append(mmd_5 - mmd_6)
# height.append(mmd_6 - mmd_7)
# height.append(mmd_7 - mmd_8)
# height.append(mmd_8 - mmd_9)
# height.append(mmd_9 - mmd_10)
# height.append(mmd_10 - mmd_11)
# height.append(mmd_11 - mmd_12)

#### measurement estimate
md_0 = 0.646806
md_1 = 0.470697
md_2 = 0.296156
md_3 = 0.120216
md_4 = -0.0555041
md_5 = -0.236515
md_6 = -0.408019
md_7 = -0.585539
md_8 = -0.760989
md_9 = -0.946181
md_10 = -1.13352
md_11 = -1.30524
md_12 = -1.47831

# height.append(0.646806-0.646806)
# height.append(0.646806-0.470697)
# height.append(0.646806-0.296156)
# height.append(0.646806-0.120216)
# height.append(0.646806+0.0555041)
# height.append(0.646806+0.236515)
# height.append(0.646806+0.408019)
# height.append(0.646806+0.585539)
# height.append(0.646806+0.760989)
# height.append(0.646806+0.946181)
# height.append(0.646806+1.13352)
# height.append(0.646806+1.30524)
# height.append(0.646806+1.47831)

# height.append(md_0 - md_1)
# height.append(md_1 - md_2)
# height.append(md_2 - md_3)
# height.append(md_3 - md_4)
# height.append(md_4 - md_5)
# height.append(md_5 - md_6)
# height.append(md_6 - md_7)
# height.append(md_7 - md_8)
# height.append(md_8 - md_9)
# height.append(md_9 - md_10)
# height.append(md_10 - md_11)
# height.append(md_11 - md_12)


#### key estimate
kd_0 = 0.646867
kd_1 = 0.470892
kd_2 = 0.296128
kd_3 = 0.120762
kd_4 = -0.0546716
kd_5 = -0.23016
kd_6 = -0.405549
kd_7 = -0.581007
kd_8 = -0.756451
kd_9 = -0.931929
kd_10 = -1.10742
kd_11 = -1.28281
kd_12 = -1.45826

height.append(0.646867-0.646867)
height.append(0.646867-0.470892)
height.append(0.646867-0.296128)
height.append(0.646867-0.120762)
height.append(0.646867+0.0546716)
height.append(0.646867+0.23016)
height.append(0.646867+0.405549)
height.append(0.646867+0.581007)
height.append(0.646867+0.756451)
height.append(0.646867+0.931929)
height.append(0.646867+1.10742)
height.append(0.646867+1.28281)
height.append(0.646867+1.45826)

# height.append(kd_0 - kd_1)
# height.append(kd_1 - kd_2)
# height.append(kd_2 - kd_3)
# height.append(kd_3 - kd_4)
# height.append(kd_4 - kd_5)
# height.append(kd_5 - kd_6)
# height.append(kd_6 - kd_7)
# height.append(kd_7 - kd_8)
# height.append(kd_8 - kd_9)
# height.append(kd_9 - kd_10)
# height.append(kd_10 - kd_11)
# height.append(kd_11 - kd_12)


#################



plt.gcf().clear()
fig = plt.figure(1)
ax = fig.add_subplot(111)

ax.bar(y_pos, height, alpha=0.5,width=0.5,align='center')
plt.xticks(y_pos, objects)

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5)
text = ax.text(-0.2,1.05, "Height from the ground [m]", transform=ax.transAxes)
# text = ax.text(-0.2,1.05, "The difference between two consecutive d [m]", transform=ax.transAxes)
text2 = ax.text(0.8,-0.1,"Stair number",transform=ax.transAxes)
ax.grid('on',axis='y')
# ax.set_yticks([0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20])
plt.xlim(-1,13)
plt.ylim(0,2.2)
fig.savefig('samplefigure', bbox_extra_artists=(lgd,text,text2), bbox_inches='tight')
# fig.savefig('samplefigure', bbox_extra_artists=(lgd,text2), bbox_inches='tight')
