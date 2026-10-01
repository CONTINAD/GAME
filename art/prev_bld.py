from bld import *
from chars import char, LOOKS
items=[bank(125,100),saloon(120,110),sheriff(95,90),telegraph(75,80),stables(115,85),church(85,115),annex_closed(52,70),annex_closed(52,70,True)]
Wt=sum(i.w for i in items)+10*len(items); Ht=max(i.h for i in items)+10
out=Image.new('RGBA',(Wt,Ht),(214,176,118,255)); x=5
for i in items: out.alpha_composite(i.im,(x,Ht-5-i.h)); x+=i.w+10
out.alpha_composite(char(LOOKS['law'],'d',0).im,(140,Ht-5-34+8))
out.resize((out.width*3,out.height*3),Image.NEAREST).save('prev_bld.png')
