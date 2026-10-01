from pix import *
OL='#2a1a12'
LOOKS={
 'law':dict(hat='#b08850',band='#5a3a1c',coat='#2c4580',shirt='#d6d2c6',pants='#6b4a2e',boots='#5a3a22',skin='#d49a6a',long=1,star=1,stache='#3a2414'),
 'outlaw':dict(hat='#2a2628',band='#b8322a',coat='#34292b',shirt='#c8b08a',pants='#4a372a',boots='#2c1f16',skin='#c08660',bandana='#c0352c',bando=1),
 'prospector':dict(hat='#8a6a40',band='#3e2c18',coat='#7a7445',shirt='#e8dcc0',pants='#6a4c30',boots='#4a3322',skin='#d0946a',beard='#8a6a4a',pick=1,sus='#3e5a2e'),
 'hunter':dict(hat='#5e5a55',band='#2b2a28',coat='#7a5634',shirt='#b24e34',pants='#3e3226',boots='#2e241a',skin='#c48a60',long=1,rifle=1),
 'banker':dict(hat='#3a2b1e',band='#1a120b',coat='#5b3e27',shirt='#e8b64a',pants='#4a3322',boots='#1f1812',skin='#e0aa82',bowler=1),
 'barkeep':dict(hair='#3a2a1c',coat='#2c2829',shirt='#f2eee4',pants='#2c2522',boots='#2a1d14',skin='#d89e74',apron=1,stache='#3a2414'),
 'lady':dict(hair='#5a3826',coat='#5e7d44',shirt='#f0e4c8',pants='#5e7d44',boots='#3a2a1c',skin='#e8b090',dress=1,bun=1),
 'clerk':dict(hair='#2e2218',visor='#3e8a4a',coat='#e8e2d4',shirt='#eee8dc',pants='#2e2e33',boots='#2a1d14',skin='#d8a47c',vest='#3a3a40'),
 'farmer':dict(hat='#e0c070',band='#8a6a34',coat='#5478ab',shirt='#e6dcc4',pants='#5478ab',boots='#4a3322',skin='#d2966a',straw=1),
 'miner':dict(hat='#6b4e30',band='#3a2a18',coat='#e2d6bb',shirt='#e2d6bb',pants='#5f4a33',boots='#3f2e20',skin='#c68c60',sus='#7a3a26',beard='#5a3f28'),
}
W,H=24,34   # cell; feet baseline y=31, centre x=12
def char(L,d,f,riding=False):
    c=Cv(W,H); cx=12; walk=[0,1,0,-1][f]; bob=-1 if f in (1,3) else 0
    side=d=='s'; back=d=='u'
    sk,sk2=hx(L['skin']),shade(L['skin'],-.25)
    co,co2,co3=hx(L['coat']),shade(L['coat'],-.28),shade(L['coat'],.18)
    pa,pa2=hx(L['pants']),shade(L['pants'],-.3)
    bo=hx(L['boots'])
    top=bob
    # ---- legs ----
    if not riding:
        if L.get('dress'):
            c.poly([(cx-5,19+top),(cx+4,19+top),(cx+6,30),(cx-7,30)],co2); c.poly([(cx-5,19+top),(cx+2,19+top),(cx+3,30),(cx-7,30)],co)
            c.rect(cx-5,30,4,2,bo); c.rect(cx+1,30,4,2,bo)
        elif side:
            a,b=walk*3,-walk*3
            c.rect(cx-2+a,21+top,4,8-top,pa2); c.rect(cx-2+a,29,5,2,shade(L['boots'],-.2)) # far leg
            c.rect(cx-1+b,21+top,4,8-top,pa); c.rect(cx-1+b,29,5,2,bo)
        else:
            l1=2 if walk>0 else 0; l2=2 if walk<0 else 0
            c.rect(cx-4,21+top,3,9-top-l1,pa); c.rect(cx+1,21+top,3,9-top-l2,pa2 if not back else pa)
            c.rect(cx-4,21+top,1,9-top-l1,shade(L['pants'],.12))
            c.rect(cx-5,29-l1,4,2,bo); c.rect(cx+1,29-l2,4,2,bo)
    # ---- torso ----
    ty=12+top; tw=8 if side else 10; tx=cx-tw//2
    th=9
    c.rect(tx,ty,tw,th,co); c.rect(tx+tw-2,ty,2,th,co2); c.rect(tx,ty,1,th,co3)
    if L.get('long') and not riding:
        lx=0 if side else 0
        c.rect(tx,ty+th,tw,4,co); c.rect(tx+tw-2,ty+th,2,4,co2)
        if not side and not back: c.vline(cx,ty+th,4,co2)
        if side: c.rect(tx-1+(walk if walk>0 else 0),ty+th+1,2,3,co)
    if not back:
        if side: c.rect(tx+tw-3,ty,2,5,hx(L['shirt']))
        else:
            c.rect(cx-1,ty,3,5,hx(L['shirt'])); c.px(cx-2,ty,hx(L['shirt'])); c.px(cx+2,ty,hx(L['shirt']))
        if L.get('vest') and not side: c.rect(tx,ty,3,th,hx(L['vest'])); c.rect(tx+tw-3,ty,3,th,hx(L['vest']))
        if L.get('apron'): c.rect(cx-3,ty+4,7,9,'#f4f1e8'); c.hline(cx-3,ty+4,7,'#d8d2c2')
        if L.get('sus') and not side: c.vline(cx-3,ty,6,hx(L['sus'])); c.vline(cx+3,ty,6,hx(L['sus']))
        if L.get('star'): c.px(tx+2 if not side else tx+tw-2,ty+3,'#f2f4f6'); c.px(tx+1 if not side else tx+tw-3,ty+3,'#b8bec4'); c.px(tx+2 if not side else tx+tw-2,ty+2,'#b8bec4')
    if L.get('bando'):
        for k in range(7): c.px(tx+1+k*(tw-2)/6, ty+k*1.2, '#6a4422')
        for k in range(0,7,2): c.px(tx+1+k*(tw-2)/6, ty+k*1.2, '#e0b84a')
    # belt
    c.hline(tx,ty+th-1,tw,'#3a2414')
    if not side: c.px(cx,ty+th-1,'#d9b24c')
    # ---- arms ----
    sw=walk*2 if not riding else 0
    if side:
        c.rect(cx-1-sw//2,ty+1,3,8,co2); c.rect(cx-1-sw//2,ty+9,3,2,sk)
    else:
        c.rect(tx-2,ty+1+(sw>0),2,8,co2 if not back else co); c.rect(tx-2,ty+9+(sw>0),2,2,sk)
        c.rect(tx+tw,ty+1+(sw<0),2,8,co2); c.rect(tx+tw,ty+9+(sw<0),2,2,sk2)
    # ---- head ----
    hy=4+top
    hw=7 if side else 8; hxl=cx-hw//2+(1 if side else 0)
    c.rect(hxl,hy,hw,8,sk); c.rect(hxl+hw-2,hy,2,8,sk2) if not back else None
    if back and not L.get('hair'): c.rect(hxl,hy,hw,6,'#4a3020'); c.rect(hxl,hy+6,hw,2,sk2)
    for xx in (hxl,hxl+hw-1): c.px(xx,hy+7,None)
    if L.get('hair'):
        c.rect(hxl,hy,hw,3,hx(L['hair']))
        if back: c.rect(hxl,hy,hw,8,hx(L['hair']))
        if side: c.rect(hxl,hy,3,6,hx(L['hair']))
        if L.get('bun'): c.rect(cx-2 if not side else hxl-2,hy-2,4,3,hx(L['hair']))
    if not back:
        if side: c.px(hxl+hw-2,hy+4,OL); c.px(hxl+hw,hy+5,sk)  # eye + nose
        else: c.px(cx-2,hy+4,OL); c.px(cx+1,hy+4,OL)
        if L.get('stache'): c.hline(cx-2 if not side else hxl+hw-3,hy+6,4 if not side else 3,hx(L['stache']))
        if L.get('beard'): c.rect(cx-3 if not side else hxl+2,hy+6,6 if not side else 5,3,hx(L['beard']))
        if L.get('bandana'): c.rect(hxl,hy+5,hw+(1 if side else 0),3,hx(L['bandana'])); c.px(cx if not side else hxl+hw-2,hy+8,hx(L['bandana']))
    elif L.get('bandana'): c.rect(cx-1,hy+6,2,2,hx(L['bandana']))
    # ---- hat ----
    if L.get('hat'):
        h1,h2=hx(L['hat']),shade(L['hat'],-.3)
        if L.get('bowler'):
            c.rect(hxl-1,hy+1,hw+2,1,h2); c.rect(hxl,hy-3,hw,4,h1); c.rect(hxl+1,hy-4,hw-2,1,h1); c.hline(hxl,hy,hw,hx(L['band']))
        else:
            bw=14 if not side else 13; bx=cx-bw//2+(1 if side else 0)
            c.rect(bx,hy+1,bw,2,h2); c.rect(bx+1,hy+1,bw-2,1,h1)
            if L.get('straw'): c.rect(bx,hy+1,bw,2,h1); c.hline(bx,hy+2,bw,h2)
            c.rect(hxl,hy-3,hw,4,h1); c.rect(hxl+1,hy-4,hw-2,1,h1)
            if not L.get('straw'): c.px(cx if not side else cx+1,hy-4,None); c.px(cx-1 if not side else cx,hy-4,h2)
            if not L.get('straw') and not side: c.px(bx,hy,h2); c.px(bx+bw-1,hy,h2)
            c.hline(hxl,hy,hw,hx(L['band']))
            c.rect(hxl+hw-2,hy-3,2,3,h2)
    elif L.get('visor'):
        c.hline(hxl,hy,hw,hx(L['visor'])); c.hline(hxl+(2 if side else 0),hy+1,hw if not side else hw,shade(L['visor'],-.2))
    # ---- tools ----
    if L.get('pick'):
        if back or side: c.line(cx-4,ty-1,cx+3,ty+8,'#7a5433'); c.line(cx-6,ty+1,cx-2,ty-3,'#9aa1a8')
        else: c.line(tx+tw+1,ty+10,tx+tw+3,ty+1,'#7a5433'); c.line(tx+tw,ty+1,tx+tw+5,ty+2,'#9aa1a8')
    if L.get('rifle'):
        if back: c.line(cx-4,ty-2,cx+4,ty+8,'#3b3e42'); c.line(cx+2,ty+6,cx+4,ty+8,'#6a4428')
        else: c.line(tx-1,ty-3,tx+3,ty+6,'#3b3e42') if not side else c.line(tx-2,ty-2,tx+2,ty+7,'#3b3e42')
    c.outline(OL)
    return c
def sack(n):
    c=Cv(14,14); s=min(5,2+n)
    c.ellipse(7,9,4+s*.4,4,'#a07444'); c.ellipse(6,8,3+s*.3,3,'#c89a5a'); c.rect(5,3,4,2,'#6a4a24')
    c.px(4,2,'#f6c632'); c.px(7,1,'#f6c632'); c.px(9,2,'#f6c632'); c.px(6,7,'#5a3a1c'); c.px(7,7,'#5a3a1c')
    c.outline(OL); return c
