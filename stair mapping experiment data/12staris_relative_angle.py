
import numpy as np
import matplotlib.pyplot as plt
import math

objects = ('0', '1', '2', '3', '4', '5','6','7','8','9','10','11','12')
y_pos = np.arange(len(objects))
height = []
me0 =[0.00172761,-0.004054,0.999968,0.646806]
me1 =[-0.0108176,-0.00632869,0.999872,0.470697]
me2 =[-0.021758,-0.0103747,0.999692,0.296156]
me3 =[-0.0120888,-0.00993091,0.999809,0.120216]
me4 =[-0.0114274,-0.0108986,0.999827,-0.0555041]
me5 =[-0.0102506,-0.0131645,0.999822,-0.236515]
me6 =[-0.0124626,-0.0149231,0.999782,-0.408019]
me7 =[-0.00790024,-0.0182877,0.999786,-0.585539]
me8 =[-0.010464,-0.0208511,0.999727,-0.760989]
me9 =[-0.00650024,-0.0223198,0.999729,-0.946181]
me10 =[-0.00380707,-0.0231819,0.999727,-1.13352]
me11 =[-0.0112,-0.0234509,0.999666,-1.30524]
me12 =[-0.00326538,-0.0257492,0.999672,-1.47831]

m0 =[0.00172761,-0.004054,0.999968,0.646806]
m1 =[-0.0108176,-0.00632869,0.999872,0.470697]
m2 =[-0.021758,-0.0103747,0.999692,0.296156]
m3 =[-0.0153108,-0.0111327,0.999808,0.120918]
m4 =[-0.00795517,-0.0157148,0.999839,-0.0573376]
m5 =[-0.0058338,-0.01709,0.99983,-0.239803]
m6 =[-0.0134496,-0.0187966,0.999726,-0.40261]
m7 =[-0.00437542,-0.0224262,0.999734,-0.588489]
m8 =[-0.00969106,-0.0235488,0.999674,-0.759553]
m9 =[-0.00255967,-0.0250657,0.999679,-0.951465]
m10 =[0.000126329,-0.0253436,0.999676,-1.13551]
m11 =[-0.0149994,-0.0240252,0.999595,-1.29849]
m12 =[0.00161549,-0.0278331,0.999608,-1.48371]

ke0 =[0.00178683,-0.00412497,0.999971,0.646867]
ke1 =[-0.0114098,-0.00643174,0.999859,0.470892]
ke2 =[-0.0218434,-0.0108218,0.999684,0.296128]
ke3 =[-0.0134888,-0.00825119,0.999807,0.120762]
ke4 =[-0.0118014,-0.00994396,0.99982,-0.0546716]
ke5 =[-0.0113632,-0.0124722,0.999811,-0.23016]
ke6 =[-0.0137634,-0.0143929,0.99977,-0.405549]
ke7 =[-0.007761,-0.0185776,0.999783,-0.581007]
ke8 =[-0.0112534,-0.0207253,0.999721,-0.756451]
ke9 =[-0.00649452,-0.0222855,0.99973,-0.931929]
ke10 =[-0.00402069,-0.0229378,0.99973,-1.10742]
ke11 =[-0.0120773,-0.0226154,0.999671,-1.28281]
ke12 =[-0.00350952,-0.0255241,0.999676,-1.45826]


def angle(baseplane,newplane):
    dot= baseplane[0]*newplane[0]+baseplane[1]*newplane[1]+baseplane[2]*newplane[2]
    basemag = math.sqrt(baseplane[0]*baseplane[0]+baseplane[1]*baseplane[1]+baseplane[2]*baseplane[2])
    newmag =  math.sqrt(newplane[0]*newplane[0]+newplane[1]*newplane[1]+newplane[2]*newplane[2])
    planeangle = math.acos(dot/(basemag*newmag))*180.0/math.pi
    return planeangle

# height.append(angle(me0,me0))
# height.append(angle(me0,me1))
# height.append(angle(me0,me2))
# height.append(angle(me0,me3))
# height.append(angle(me0,me4))
# height.append(angle(me0,me5))
# height.append(angle(me0,me6))
# height.append(angle(me0,me7))
# height.append(angle(me0,me8))
# height.append(angle(me0,me9))
# height.append(angle(me0,me10))
# height.append(angle(me0,me11))
# height.append(angle(me0,me12))

# height.append(angle(m0,m0))
# height.append(angle(m0,m1))
# height.append(angle(m0,m2))
# height.append(angle(m0,m3))
# height.append(angle(m0,m4))
# height.append(angle(m0,m5))
# height.append(angle(m0,m6))
# height.append(angle(m0,m7))
# height.append(angle(m0,m8))
# height.append(angle(m0,m9))
# height.append(angle(m0,m10))
# height.append(angle(m0,m11))
# height.append(angle(m0,m12))

height.append(angle(ke0,ke0))
height.append(angle(ke0,ke1))
height.append(angle(ke0,ke2))
height.append(angle(ke0,ke3))
height.append(angle(ke0,ke4))
height.append(angle(ke0,ke5))
height.append(angle(ke0,ke6))
height.append(angle(ke0,ke7))
height.append(angle(ke0,ke8))
height.append(angle(ke0,ke9))
height.append(angle(ke0,ke10))
height.append(angle(ke0,ke11))
height.append(angle(m12,ke12))

plt.gcf().clear()
fig = plt.figure(1)
ax = fig.add_subplot(111)

ax.bar(y_pos, height, align='center', alpha=0.5,width=0.5)
plt.xticks(y_pos, objects)

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5)
text = ax.text(-0.2,1.05, "Angle [degrees]", transform=ax.transAxes)
text2 = ax.text(0.8,-0.1,"Stair number",transform=ax.transAxes)
# ax.grid('on')
plt.xlim(-1,13)
plt.ylim(0,1.5)
fig.savefig('samplefigure', bbox_extra_artists=(lgd,text,text2), bbox_inches='tight')
