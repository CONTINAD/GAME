# Builds art/atlas.png + art/atlas.json — every sprite the game draws. Run: python3 build.py
import json
from pix import *
from chars import char, sack, LOOKS
import bld, props
S={}
for n,L in LOOKS.items():
    for d in 'dsu':
        for f in range(4): S[f'{n}_{d}{f}']=char(L,d,f)
    for f in range(4): S[f'{n}_r{f}']=char(L,'s',f,riding=True)
for k in range(1,6): S[f'sack{k}']=sack(k)
B={'bank':(125,100),'saloon':(120,110),'sheriff':(95,90),'telegraph':(75,80),'stables':(115,85),'church':(85,115)}
for k,(w,h) in B.items(): S['b_'+k]=getattr(bld,k)(w,h)
S['annex']=bld.annex_closed(52,70); S['annex_b']=bld.annex_closed(52,70,True); S['annex_floor']=bld.annex_floor(52,70); S['annex_wn']=bld.annex_wall(52,True); S['annex_ws']=bld.annex_wall(52,False)
P=props
S['barrel']=P.barrel(); S['crate']=P.crate(); S['trough_v']=P.trough(11,26); S['trough_h']=P.trough(26,10)
S['hitch']=P.hitch(); S['lamp']=P.lamp(); S['tent']=P.tent(); S['wagon']=P.wagon(); S['wagonH']=P.wagon(True); S['well']=P.well(); S['pole']=P.pole(); S['dyn']=P.dyn(); S['mine']=P.mine()
for i in range(4): S[f'saguaro{i}']=P.saguaro(i*7+1); S[f'tumble{i}']=P.tumble(i); S[f'horse{i}']=P.horse(i); S[f'coin{i}']=P.coin(i)
for i in range(3): S[f'pear{i}']=P.pear(i*5+2); S[f'tuft{i}']=P.tuft(i); S[f'sage{i}']=P.sage(i)
for s in range(6,13): S[f'rock{s}']=P.rock(s,s)
for s in range(26,50,2): S[f'boulder{s}']=P.rock(s,s,True)
for n in range(1,6): S[f'pile{n}']=P.coinpile(n)
# shelf-pack
items=sorted(S.items(),key=lambda kv:-kv[1].h); AW=1024; x=y=rowh=0; M={}
for k,c in items:
    if x+c.w>AW: x=0; y+=rowh+1; rowh=0
    M[k]=[x,y,c.w,c.h]; x+=c.w+1; rowh=max(rowh,c.h)
atlas=Image.new('RGBA',(AW,y+rowh),(0,0,0,0))
for k,c in S.items(): atlas.alpha_composite(c.im,tuple(M[k][:2]))
atlas.save('atlas.png',optimize=True); json.dump(M,open('atlas.json','w'),separators=(',',':'))
print(len(S),'sprites',atlas.size)
