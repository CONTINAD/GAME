from pix import *
import random
OL='#2a1a12'
def barrel():
    c=Cv(12,16); c.rect(1,2,10,13,'#7a4c2a'); c.rect(2,1,8,15,'#7a4c2a'); c.rect(2,2,3,13,'#9a6a3e'); c.rect(8,2,2,13,'#5a361c')
    c.hline(1,4,10,'#4a4a4a'); c.hline(1,11,10,'#4a4a4a'); c.ellipse(6,2.5,4.5,1.6,'#b3844e'); c.ellipse(6,2.5,3,1,'#7a4c2a'); c.outline(OL); return c
def crate():
    c=Cv(14,16); c.rect(1,5,12,10,'#8f6a3e'); c.rect(1,1,12,5,'#b58a52'); c.line(1,5,12,14,'#5b3d1f'); c.line(12,5,1,14,'#5b3d1f')
    c.hline(1,5,12,'#5b3d1f'); c.vline(1,5,10,'#a37a48'); c.outline(OL); return c
def trough(w,h): # w,h px footprint
    c=Cv(w+2,h+6); c.rect(1,3,w,h+2,'#5e3c22'); c.rect(1,1,w,h,'#7a5132'); c.rect(2,2,w-2,h-2,'#4f8199'); c.hline(3,3,max(1,w//2),'#9cc6d8'); c.outline(OL); return c
def hitch():
    c=Cv(28,10); c.rect(2,2,24,2,'#7d5433'); c.rect(3,3,2,7,'#5b3b21'); c.rect(23,3,2,7,'#5b3b21'); c.hline(2,2,24,'#9b7048'); c.outline(OL); return c
def lamp():
    c=Cv(8,28); c.rect(3,6,2,22,'#3b2a1e'); c.rect(1,1,6,6,'#2b2016'); c.rect(2,2,4,4,'#ffd27a'); c.px(2,2,'#fff4c0'); c.outline(OL); return c
def saguaro(seed):
    r=random.Random(seed); h=26+r.randrange(8); c=Cv(20,h+2); x=10
    def col(cx_,y1,y2,w):
        c.rect(cx_-w//2,y1,w,y2-y1,'#4a6636'); c.rect(cx_-w//2,y1,w-2,y2-y1,'#5f8045'); c.vline(cx_-w//2+1,y1+1,y2-y1-2,'#86a462')
        c.px(cx_-w//2,y1,None); c.px(cx_+w-w//2-1,y1,None)
    col(x,0,h,6)
    ay=r.randrange(8,14); col(3,ay-7,ay+2,4); c.rect(3,ay,6,3,'#4a6636'); c.rect(3,ay,5,2,'#5f8045')
    by=r.randrange(5,11); col(17,by-6,by+2,4); c.rect(12,by,6,3,'#4a6636'); c.rect(12,by,5,2,'#5f8045')
    for yy in range(2,h,3): c.px(x,yy,'#3d5a2c')
    c.outline(OL); return c
def pear(seed):
    r=random.Random(seed); c=Cv(18,16)
    for dx,dy,rx,ry in [(5,10,3,4),(12,10,3,4),(8,5,3,4),(3,4,2,3),(14,4,2,3)]:
        c.ellipse(dx,dy,rx,ry,'#4f7a40'); c.ellipse(dx-1,dy-1,rx-1,ry-1,'#6f9a58')
        for _ in range(2): c.px(dx+r.randrange(-1,2),dy+r.randrange(-2,2),'#d8e0a0')
    c.px(14,1,'#d9486a'); c.px(15,1,'#e8708a'); c.outline(OL); return c
def rock(s,seed,red=False):
    r=random.Random(seed); w=max(6,s); h=max(4,int(s*.7)); c=Cv(w+2,h+2)
    a,b,d=('#b5653d','#cf7e52','#8e4a2c') if red else ('#9a8670','#b8a48c','#76644f')
    c.ellipse(w/2+1,h/2+1,w/2,h/2,a); c.ellipse(w/2,h/2,w/2-1.5,h/2-1.5,b); c.ellipse(w/2+1.5,h/2+1.5,w/2-2,h/2-2,a,only='opaque')
    c.ellipse(w/2-1,h/2-1,max(1,w/4),max(1,h/4),shade(b,.15),only='opaque')
    for _ in range(max(1,s//8)): x=r.randrange(2,w); c.line(x,h//2,x+r.randrange(-3,4),h-1,d)
    c.outline(OL); return c
def tent():
    c=Cv(36,26); c.poly([(1,24),(18,2),(35,24)],'#b9a27a'); c.poly([(18,2),(35,24),(22,24)],'#9c845d'); c.poly([(14,24),(18,12),(22,24)],'#2a1c10')
    c.line(18,0,18,3,'#5b3b21'); c.outline(OL); return c
def wagon(cover=False):
    c=Cv(46,28 if cover else 20); o=8 if cover else 0
    c.rect(2,4+o,42,8,'#5b3b21'); c.rect(2,2+o,42,4,'#7d5433'); c.hline(2,2+o,42,'#9b7048')
    for k in range(6,44,7): c.vline(k,4+o,8,'#4a2f1a')
    if cover:
        c.ellipse(23,8,20,8,'#e8dcc0'); c.rect(3,8,40,6,'#e8dcc0'); c.rect(3,12,40,2,'#c8bca0')
        for k in (10,23,36): c.vline(k,2,12,'#cfc3a6')
    for wx in (10,36):
        c.ellipse(wx,13+o,5.5,5.5,'#3a2615'); c.ellipse(wx,13+o,4,4,None)
        c.ellipse(wx,13+o,4,4,(0,0,0,0)); c.px(wx,13+o,'#3a2615'); c.line(wx-3,13+o,wx+3,13+o,'#5a3a22'); c.line(wx,10+o,wx,16+o,'#5a3a22')
    c.outline(OL); return c
def well():
    c=Cv(26,28); c.ellipse(13,22,11,5,'#7f7466'); c.ellipse(13,21,8,3,'#23272b'); c.rect(3,6,3,16,'#5b3b21'); c.rect(20,6,3,16,'#5b3b21')
    c.poly([(0,8),(13,0),(26,8)],'#7d5433'); c.line(0,8,13,0,'#9b7048'); c.vline(13,8,8,'#bfb39a'); c.rect(11,15,4,3,'#6b4a2a'); c.outline(OL); return c
def pole():
    c=Cv(20,50); c.rect(9,4,3,46,'#4e3520'); c.vline(10,4,46,'#6b4a2d'); c.rect(1,6,18,2,'#5a3d23'); [c.rect(k,4,2,2,'#b9d0d6') for k in (2,7,12,16)]; c.outline(OL); return c
def tumble(f):
    import math
    c=Cv(14,14); r=random.Random(9)
    for k in range(9):  # tangled loops of twig
        a0=r.random()*6.283+f*.6; rx=3+r.random()*3; ry=2+r.random()*3
        for t in range(24):
            a=a0+t*.262; c.px(7+math.cos(a)*rx*math.cos(k)+math.sin(a)*ry*.4,7+math.sin(a)*ry,'#9a7646' if (k+t)%3 else '#c49e64')
    return c
def horse(f):
    c=Cv(36,28); leg=[0,2,0,-2][f]
    for lx,o in [(8,leg),(12,-leg),(24,-leg),(28,leg)]: c.rect(lx+o,16,3,10,'#4e2e18'); c.rect(lx+o,25,3,2,'#2a180c')
    c.ellipse(18,13,13,6,'#6b3f22'); c.ellipse(16,11,10,3.5,'#8a5530',only='opaque')
    c.poly([(26,12),(31,2),(35,4),(31,15)],'#6b3f22'); c.ellipse(33,5,3,2.5,'#6b3f22'); c.px(33,4,'#1a0f08')
    c.line(5,10,1,20,'#2a180c'); c.line(6,10,3,19,'#2a180c'); c.line(29,3,27,10,'#2a180c')
    c.rect(14,7,8,3,'#3a2415'); c.outline(OL); return c
def coin(f):
    c=Cv(6,6); w=[3,2,1,2][f]
    c.ellipse(3,3,w,2.6,'#a8760c'); c.ellipse(3,2.6,max(.6,w-.6),2.1,'#f6c632')
    if f==0: c.px(2,1,'#fff6c8')
    return c
def coinpile(n):
    c=Cv(16,10); r=random.Random(n)
    for _ in range(3+n*2):
        x=r.randrange(2,14); y=r.randrange(3,9); c.rect(x-1,y,3,2,'#a8760c'); c.hline(x-1,y,3,'#f6c632'); c.px(x,y,'#fff3b0' if r.random()<.3 else '#f6c632')
    c.outline('#6d4a08'); return c
def dyn():
    c=Cv(10,12); [c.rect(1+k*3,4,2,8,'#b8322a') for k in range(3)]; c.hline(1,6,8,'#6b4a2a'); c.line(5,4,7,0,'#3b2a1c'); c.outline(OL); return c
def tuft(seed):
    r=random.Random(seed); c=Cv(9,6)
    for k in range(5): c.line(4,5,1+k*2+r.randrange(-1,1),r.randrange(0,3),'#8a8a45' if k%2 else '#a39c58')
    return c
def sage(seed):
    # low desert shrub: dark core, lighter leaf clusters on the lit side, no outline (sits in the ground)
    c=Cv(14,9); r=random.Random(seed)
    for k in range(9):
        x=2+r.randrange(10); y=2+r.randrange(5); c.ellipse(x,y,2,1.6,'#6f7a4c')
    for k in range(7):
        x=2+r.randrange(9); y=1+r.randrange(4); c.px(x,y,'#9aa56c'); c.px(x+1,y,'#b4bc84')
    c.hline(3,8,8,'#5e5136'); return c
def mine():
    # rocky hill with a timbered adit, ore-cart rails running out to the claim, tailings heap
    W,H=100,110; c=Cv(W,H); r=random.Random(21)
    c.ellipse(50,34,46,30,'#8e5a36'); c.ellipse(46,28,40,24,'#a8784b'); c.ellipse(40,22,28,15,'#bd8b58')
    for _ in range(26): x=10+r.randrange(80); y=8+r.randrange(48); c.ellipse(x,y,1.5+r.random()*2.5,1.2+r.random()*1.6,r.choice(['#8e6038','#7a4c2a','#c99a66']),only='opaque')
    c.rect(38,40,24,22,'#1c120a'); c.rect(40,44,20,18,'#0e0905')
    c.rect(35,38,4,25,'#6b4527'); c.rect(61,38,4,25,'#6b4527'); c.rect(33,35,34,4,'#7d5433'); c.hline(33,35,34,'#9b7048')
    c.vline(36,39,24,'#8a6038'); c.vline(62,39,24,'#8a6038')
    for yy in range(63,106,4): c.hline(43,yy,14,'#7a5a3a')
    c.vline(45,62,44,'#5e4a36'); c.vline(54,62,44,'#5e4a36')
    c.ellipse(80,68,15,9,'#9c8a74'); c.ellipse(78,65,10,6,'#b5a48b')
    c.rect(65,74,10,6,'#5b3b21'); c.rect(64,72,12,3,'#7d5433'); c.px(66,80,'#2a1a10'); c.px(73,80,'#2a1a10')
    for x,y in ((18,78),(82,78),(18,104),(82,104)): c.rect(x,y,3,4,'#6b4527')
    return c
