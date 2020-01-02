import matplotlib.pyplot as plt


ele_f = open("elevation_res_0.01.txt", "r")
ele_x=[]
ele_z=[]

oct_f = open("octomap_res_0.01_cutview2.txt", "r")
oct_x =[]
oct_z = []

str_f = open("stair_res_0.01_cutview2.txt", "r")
str_x =[]
str_z =[]

mdl_f = open("model_res_0.005_cutview2.txt","r")
mdl_x=[]
mdl_z=[]

for line in ele_f:
    xz = line.strip("\n")
    xz2 =xz.split(",")
    ele_x.append(float(xz2[0]))
    ele_z.append(float(xz2[1]))
    # print(xz2)
ele_f.close() 

for line in str_f:
    xz = line.strip("\n")
    xz2 =xz.split(",")
    str_x.append(float(xz2[0]))
    str_z.append(float(xz2[1]))
    # print(xz2)
str_f.close() 

for line in mdl_f:
    xz = line.strip("\n")
    xz2 =xz.split(",")
    mdl_x.append(float(xz2[0]))
    mdl_z.append(float(xz2[1]))
    # print(xz2)
mdl_f.close() 

for line in oct_f:
    xz = line.strip("\n")
    xz2 =xz.split(",")
    oct_x.append(float(xz2[0]))
    oct_z.append(float(xz2[1]))
    # print(xz2)
oct_f.close() 




# plt.figure(figsize=(18, 5))
# plt.plot(mdl_x,mdl_z,"k-",linewidth =4,label="True terrain")

# plt.plot(ele_x,ele_z,"b-",linewidth=2,label="Elevation mapping")
# plt.scatter(oct_x,oct_z,3,color= "g",marker="o",label="Octomap")
# plt.scatter(str_x,str_z,linewidth=2.4,color="r",marker="x",label="Stair mapping")
# plt.xlim(0,0.055)
# plt.xlabel("distance[m]")
# plt.ylabel("z[m]")
# leg = plt.legend(loc=8)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),ncol=5)
# leg.get_frame().set_linewidth(0.0)
# plt.show()

plt.gcf().clear()
fig = plt.figure(figsize=(18, 4))
ax = fig.add_subplot(111)

ax.plot(mdl_x,mdl_z,color='k',label="True terrain")
ax.plot(ele_x,ele_z ,color='b',label='Elevation mapping')
ax.scatter(oct_x,oct_z ,3,color='g',marker='o',label='Octomap')
ax.scatter(str_x,str_z ,color='r',marker='x',label='Stairway mapping')


handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(loc=8)
text = ax.text(-0.02,1.05, "z [m]", transform=ax.transAxes)
text2 = ax.text(0.9,-0.1,"distance [m]",transform=ax.transAxes)
plt.xlim(0.55,2.45)
plt.ylim(0.1,0.6)
# ax.set_title("Trigonometry")
fig.savefig('samplefigure1', bbox_extra_artists=(lgd,text,text2), bbox_inches='tight')