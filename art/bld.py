from pix import *
from font import text, width
import random
OL='#2a1a12'
def wood(c,x,y,w,h,base,vert=True,gap=3,seed=1):
    r=random.Random(seed); b=hx(base); d=shade(base,-.22); l=shade(base,.12)
    c.rect(x,y,w,h,b)
    if vert:
        for k in range(x,x+w,gap):
            c.vline(k,y,h,d)
            for yy in range(y,y+h):
                if r.random()<.06: c.px(k+1+r.randrange(max(1,gap-1)),yy,l)
    else:
        for k in range(y,y+h,gap):
            c.hline(x,k,w,d)
            c.hline(x,k+1,w,l) if k+1<y+h else None
def brick(c,x,y,w,h,base,seed=2):
    r=random.Random(seed); b=hx(base); m=shade(base,.35); d=shade(base,-.18)
    c.rect(x,y,w,h,b)
    for rr,yy in enumerate(range(y,y+h,3)):
        c.hline(x,yy,w,m)
        off=0 if rr%2 else 3
        for xx in range(x+off,x+w,6): c.px(xx,yy+1,m); c.px(xx,yy+2,m)
        for xx in range(x,x+w):
            if r.random()<.05: c.px(xx,yy+1+r.randrange(2),d)
def shingle_roof(c,x,y,w,h,base,seed=3):
    """front-facing pitched roof: rows of shakes, top lighter (sun from upper-left)"""
    r=random.Random(seed)
    for i,yy in enumerate(range(y,y+h)):
        t=(yy-y)/max(1,h-1); col=shade(base,.16-t*.34)
        c.hline(x,yy,w,col)
    for rr,yy in enumerate(range(y+2,y+h,3)):
        c.hline(x,yy,w,shade(base,-.35))
        off=r.randrange(4)
        for xx in range(x+off,x+w,r.choice([4,5,6])): c.px(xx,yy-1,shade(base,-.3)); c.px(xx,yy-2,shade(base,-.18))
    for _ in range(w*h//30): c.px(x+r.randrange(w),y+r.randrange(h),shade(base,.25))
    c.hline(x,y,w,shade(base,.3))
def window(c,x,y,w,h,lit=False,arch=False,frame='#e6dcc4'):
    c.rect(x-1,y-1,w+2,h+2,frame)
    c.rect(x,y,w,h,'#3a3230')
    gl=hx('#e8b85a') if lit else hx('#7d98a6')
    c.rect(x,y+h//3,w,h-h//3,gl); c.px(x,y+h//3,shade(gl,.4)); c.px(x+1,y+h//3,shade(gl,.4))
    c.vline(x+w//2,y,h,frame); c.hline(x,y+h//2,w,frame)
    if arch: c.px(x-1,y-1,None); c.px(x+w,y-1,None); c.hline(x,y-2,w,frame)
    c.hline(x-1,y+h+1,w+2,shade(frame,-.35))
def door(c,x,y,w,h,col='#5c3a1e',trim=None):
    c.rect(x,y,w,h,shade(col,-.45)); c.rect(x+1,y+1,w-2,h-1,col); c.vline(x+w//2,y+1,h-1,shade(col,-.35))
    c.px(x+w//2-2,y+h//2,'#d9b24c'); c.px(x+w//2+1,y+h//2,'#d9b24c')
    if trim: c.rect(x-1,y-1,w+2,1,trim); c.vline(x-1,y-1,h+1,trim); c.vline(x+w,y-1,h+1,trim)
def sign(c,cx,y,s,bg='#4a2c16',fg='#f6c632',edge='#c9a152',pad=2):
    w=width(s)+pad*2+2; x=cx-w//2
    c.rect(x,y,w,9,hx(edge)); c.rect(x+1,y+1,w-2,7,hx(bg)); text(c,x+pad+1,y+2,s,fg,shade(bg,-.4))
def porch(c,x,y,w,roof='#6e4a2e',floor='#8f6440',posts='#5a3a1f',depth=8,seed=4):
    # awning over the boardwalk, posts down to the walk
    shingle_roof(c,x-2,y,w+4,5,roof,seed)
    c.hline(x-2,y+5,w+4,shade(roof,-.45))
    for px_ in range(x,x+w+1,max(8,w//5)):
        c.rect(px_,y+6,2,depth,posts); c.vline(px_,y+6,depth,shade(posts,.25))
def shadow_band(c,x,y,w,h,a=70):
    for yy in range(y,y+h):
        for xx in range(x,x+w):
            p=c.get(xx,yy)
            if p[3]: c.px(xx,yy,(int(p[0]*.72),int(p[1]*.7),int(p[2]*.78),255))

# ------------------------------------------------------------------ buildings
# each returns Cv sized (w/2, h/2 + extra) with the footprint bottom at the bottom row; 'extra' px rise above the footprint top
def bank(W,Hh):
    ex=8; c=Cv(W,Hh+ex); y0=ex
    fh=48; fy=Hh+ex-fh       # facade top
    roofh=fy-y0
    # flat tar roof with parapet + coping
    c.rect(0,y0,W,roofh,'#8e4632')
    c.rect(4,y0+4,W-8,roofh-6,'#6e5a4c'); c.noise(4,y0+4,W-8,roofh-6,'#7d6858',.25,11); c.noise(4,y0+4,W-8,roofh-6,'#5c4a3e',.12,12)
    c.hline(4,y0+4,W-8,'#4a3a30'); c.vline(4,y0+4,roofh-6,'#4a3a30')
    c.rect(0,y0,W,2,'#e3d3b0'); c.rect(0,y0,2,roofh,'#d8c6a0'); c.rect(W-2,y0,2,roofh,'#b8a47e')
    # skylight, hatch, chimney
    c.rect(14,y0+10,22,12,'#3a2a20'); c.rect(15,y0+11,9,10,'#9cb8c6'); c.rect(25,y0+11,10,10,'#86a2b0'); c.px(16,y0+12,'#e6f2f6')
    c.rect(W-30,y0+12,12,10,'#5a4a3e'); c.rect(W-29,y0+13,10,8,'#463a30'); c.hline(W-29,y0+16,10,'#5a4a3e')
    c.rect(W-14,y0-6,7,12,'#9a4630'); c.rect(W-15,y0-7,9,2,'#d8c6a0'); brick(c,W-14,y0-5,7,10,'#9a4630',9)
    # front parapet with medallion (rises above roof line)
    c.rect(0,fy-8,W,8,'#a1432c'); brick(c,0,fy-8,W,8,'#a1432c',5); c.rect(0,fy-9,W,2,'#e8dcc0'); c.hline(0,fy-1,W,'#c9b48c')
    for k in (0,W-6): c.rect(k,fy-12,6,12,'#e8dcc0'); c.rect(k+1,fy-11,4,1,'#fff6e0'); c.vline(k+5,fy-11,11,'#b8a47e')
    mx=W//2; c.ellipse(mx,fy-13,8,8,'#7a5006'); c.ellipse(mx,fy-13,7,7,'#f0c231'); c.ellipse(mx-1,fy-14,4,4,'#ffe58a'); text(c,mx-1,fy-15,'$','#8a5e08')
    # brick facade, stone base + string course
    brick(c,0,fy,W,fh,'#a1432c',6)
    c.hline(0,fy+22,W,'#d4c19c'); c.hline(0,fy+23,W,'#a8946e')
    c.rect(0,fy+fh-5,W,5,'#a99a84'); c.hline(0,fy+fh-5,W,'#cbbca4')
    for k in range(4,W,10): c.vline(k,fy+fh-4,4,'#8c7e6a')
    # windows: upper row arched, lower flank windows
    for wx in [8,22,W-30,W-16]: window(c,wx,fy+5,7,12,False,True)
    for wx in [10,26,W-34,W-18]: window(c,wx,fy+27,7,11,False,True)
    for wx in [W//2-18,W//2+13]: window(c,wx,fy+5,6,12,False,True)
    # entrance: stone surround, double doors, gold trim, sign
    ex0=W//2-9; c.rect(ex0-3,fy+20,24,fh-25,'#d4c19c'); c.rect(ex0-2,fy+21,22,1,'#efe2c4')
    door(c,ex0,fy+24,18,fh-29,'#5c3a1e','#e0b43c')
    sign(c,W//2,fy+10,'BANK','#2a1a0c','#f6c632','#d9b24c')
    # steps
    c.rect(ex0-4,Hh+ex-3,26,3,'#bdb09a'); c.hline(ex0-4,Hh+ex-3,26,'#ddd2bc')
    return c
def saloon(W,Hh):
    ex=14; c=Cv(W,Hh+ex); y0=ex; fh=40; fy=Hh+ex-fh
    shingle_roof(c,3,y0+4,W-6,fy-y0-4,'#7a5439',21)
    c.vline(3,y0+4,fy-y0-4,'#4a2f1c'); c.vline(W-4,y0+4,fy-y0-4,'#4a2f1c')
    # tall false front with stepped top
    ff=fy-20; wood(c,8,ff,W-16,22,'#9a6a40',True,3,22)
    c.rect(6,ff-3,W-12,3,'#6c4424'); c.rect(W//2-20,ff-9,40,7,'#9a6a40'); wood(c,W//2-20,ff-9,40,7,'#9a6a40',True,3,23); c.rect(W//2-22,ff-11,44,3,'#6c4424')
    sign(c,W//2,ff+4,'SALOON','#3a2412','#f6c632','#c9a152')
    # upper balcony windows on the false front
    for wx in [14,W-22]: window(c,wx,ff+5,7,9,True)
    # facade
    wood(c,0,fy,W,fh,'#8a5a34',True,3,24)
    for wx in [10,26,W-34,W-18]: window(c,wx,fy+12,8,12,True)
    # batwing doors
    dx=W//2-8; c.rect(dx,fy+14,16,fh-14,'#2a170b'); c.rect(dx+1,fy+20,6,11,'#b8322a'); c.rect(dx+9,fy+20,6,11,'#b8322a'); c.hline(dx+1,fy+20,6,'#d9554a'); c.hline(dx+9,fy+20,6,'#d9554a')
    porch(c,0,fy+2,W,'#6e4a2e','#8f6440','#5a3a1f',fh-4,25)
    shadow_band(c,0,fy+8,W,3)
    c.rect(0,Hh+ex-3,W,3,'#7a5434'); c.hline(0,Hh+ex-3,W,'#a07650')
    return c
def sheriff(W,Hh):
    ex=16; c=Cv(W,Hh+ex); y0=ex; fh=38; fy=Hh+ex-fh
    shingle_roof(c,3,y0+6,W-6,fy-y0-6,'#5b6573',31)
    ff=fy-18; wood(c,10,ff,W-20,20,'#a5a7a2',True,3,32); c.rect(8,ff-3,W-16,3,'#5e6168')
    # gabled false-front crown with star
    c.poly([(W//2-22,ff),(W//2,ff-12),(W//2+22,ff)],'#a5a7a2'); c.line(W//2-23,ff,W//2,ff-13,'#5e6168'); c.line(W//2,ff-13,W//2+23,ff,'#5e6168')
    st=[(0,-5),(1,-2),(4,-2),(2,0),(3,3),(0,1),(-3,3),(-2,0),(-4,-2),(-1,-2)]
    c.poly([(W//2+a,ff-3+b) for a,b in st],'#e6e9ec'); c.px(W//2,ff-3,'#8c939b')
    sign(c,W//2,ff+6,'SHERIFF','#2f3848','#f2f4f6','#cfd3d8')
    wood(c,0,fy,W,fh,'#8f918d',True,3,33)
    window(c,9,fy+12,8,12); window(c,W-17,fy+12,8,12)
    for k in range(4): c.vline(W-16+k*2,fy+12,12,'#2a2a2a')
    door(c,W//2-7,fy+14,14,fh-17,'#51545a')
    porch(c,0,fy+2,W,'#4d5664','#8f6440','#4a4c50',fh-5,34)
    c.rect(0,Hh+ex-3,W,3,'#7a5434'); c.hline(0,Hh+ex-3,W,'#a07650')
    return c
def telegraph(W,Hh):
    ex=12; c=Cv(W,Hh+ex); y0=ex; fh=34; fy=Hh+ex-fh
    shingle_roof(c,3,y0+6,W-6,fy-y0-6,'#6e4b33',41)
    ff=fy-14; wood(c,6,ff,W-12,16,'#a47850',True,3,42); c.rect(4,ff-3,W-8,3,'#6c4424')
    sign(c,W//2,ff+4,'TELEGRAPH','#efe0b8','#2b1d10','#6b4a22',1)
    wood(c,0,fy,W,fh,'#8a6440',True,3,43)
    window(c,8,fy+10,8,11,True); window(c,W-16,fy+10,8,11)
    door(c,W//2-6,fy+12,12,fh-15,'#3a2412')
    # insulator crossarm on the roof
    c.vline(W-12,y0-8,16,'#4e3520'); c.hline(W-18,y0-6,13,'#4e3520'); [c.px(W-18+k,y0-7,'#b9d0d6') for k in (0,4,8,12)]
    porch(c,0,fy+2,W,'#5e3e28','#8f6440','#5a3a1f',fh-5,44)
    c.rect(0,Hh+ex-3,W,3,'#7a5434'); c.hline(0,Hh+ex-3,W,'#a07650')
    return c
def stables(W,Hh):
    # barn seen from the yard side: big gambrel roof, wide doors, hay loft
    ex=12; c=Cv(W,Hh+ex); y0=ex; fh=34; fy=Hh+ex-fh
    shingle_roof(c,0,y0,W,fy-y0,'#7d5536',51)
    c.rect(W//2-14,y0+14,28,12,'#2a190c'); r=random.Random(5)
    for _ in range(70): c.px(W//2-13+r.randrange(26),y0+19+r.randrange(7),'#e0bb55')
    c.vline(W//2-12,y0-10,10,'#5a3a1f'); c.vline(W//2+12,y0-10,10,'#5a3a1f')
    sign(c,W//2,y0-11,'STABLES','#3a2412','#f6c632','#c9a152')
    wood(c,0,fy,W,fh,'#7a4f2c',True,3,52)
    c.rect(W//2-16,fy+6,32,fh-6,'#231509')
    for k,dx in enumerate((W//2-16,W//2+1)):
        wood(c,dx,fy+6,15,fh-6,'#8c5c34',True,3,53+k); c.line(dx,fy+6,dx+14,fy+fh-1,'#5a3a1c'); c.line(dx+14,fy+6,dx,fy+fh-1,'#5a3a1c'); c.hline(dx,fy+6,15,'#5a3a1c')
    for wx in (10,W-18): window(c,wx,fy+10,8,8)
    return c
def church(W,Hh):
    ex=40; c=Cv(W,Hh+ex); y0=ex; fh=40; fy=Hh+ex-fh
    shingle_roof(c,2,y0+8,W-4,fy-y0-8,'#3f4756',61)
    # steeple at the street (north) end, rising above the roof
    tx=W//2; c.rect(tx-11,y0-6,22,22,'#efe8da'); c.rect(tx+6,y0-6,5,22,'#d6cebd')
    for yy in range(y0-6,y0+16,3): c.hline(tx-11,yy,22,'#d8cfbe')
    c.rect(tx-5,y0-3,10,9,'#2a2420'); c.rect(tx-3,y0-1,6,6,'#c9a152'); c.hline(tx-4,y0+5,8,'#8a6a2a')
    c.poly([(tx-13,y0-6),(tx,y0-30),(tx+13,y0-6)],'#2e3440'); c.poly([(tx,y0-30),(tx+13,y0-6),(tx,y0-6)],'#454e5f')
    c.vline(tx,y0-38,8,'#e8e2d4'); c.hline(tx-3,y0-35,7,'#e8e2d4')
    # white clapboard wall
    c.rect(0,fy,W,fh,'#efe8da')
    for yy in range(fy,fy+fh,3): c.hline(0,yy,W,'#d8cfbe')
    c.rect(W-6,fy,6,fh,'#d6cebd')
    for wx in (8,22,W-30,W-16): window(c,wx,fy+9,7,16,False,True,'#ffffff')
    c.rect(W//2-6,fy+12,12,fh-12,'#e8e0d0'); c.poly([(W//2-6,fy+12),(W//2,fy+6),(W//2+6,fy+12)],'#e8e0d0')
    c.rect(W//2-4,fy+14,8,fh-14,'#5a3a22'); c.vline(W//2,fy+14,fh-14,'#3a2412')
    return c
def annex_closed(W,Hh,boards=False):
    ex=4; c=Cv(W,Hh+ex); y0=ex; fh=16; fy=Hh+ex-fh
    c.rect(0,y0,W,fy-y0,'#9a958b')
    r=random.Random(7)
    for rr,yy in enumerate(range(y0,fy,6)):
        c.hline(0,yy,W,'#7f7a71'); off=0 if rr%2 else 6
        for xx in range(off,W,12): c.vline(xx,yy,6,'#7f7a71')
    c.noise(0,y0,W,fy-y0,'#aaa59b',.08,8)
    c.rect(0,y0,W,2,'#c8c3b8'); c.rect(0,y0,2,fy-y0,'#b5b0a6'); c.rect(W-2,y0,2,fy-y0,'#6f6a62')
    for xx in range(4,W,8): c.px(xx,y0+3,'#e0e4e8'); c.px(xx,fy-3,'#e0e4e8')
    c.rect(0,fy,W,fh,'#7d786f')
    for yy in range(fy,fy+fh,4): c.hline(0,yy,W,'#67635b')
    c.rect(W//2-6,fy+3,12,10,'#2a2c2f')
    for k in range(4): c.vline(W//2-4+k*3,fy+3,10,'#8d949b')
    if boards:
        for k in range(4):
            y=y0+14+k*9; c.rect(W-16,y,18,4,'#8a5e37'); c.hline(W-16,y,18,'#a87a4a'); c.px(W-14,y+2,'#3b2a1c'); c.px(W,y+2,'#3b2a1c')
    return c
