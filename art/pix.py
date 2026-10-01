# Tiny pixel canvas on top of Pillow: everything the atlas build needs, nothing else.
from PIL import Image, ImageDraw
import random
def hx(c,a=255):
    if isinstance(c,tuple): return c if len(c)==4 else (*c,a)
    c=c.lstrip('#'); return (int(c[0:2],16),int(c[2:4],16),int(c[4:6],16),a)
def mix(a,b,t):
    a,b=hx(a),hx(b); return tuple(round(a[i]+(b[i]-a[i])*t) for i in range(3))+(255,)
def shade(c,f): # f>0 lighten toward warm, f<0 darken toward cool
    r,g,b,_=hx(c)
    if f>=0: return mix((r,g,b,255),(255,244,214,255),f)
    return mix((r,g,b,255),(40,26,44,255),-f)
class Cv:
    def __init__(s,w,h): s.w,s.h=w,h; s.im=Image.new('RGBA',(w,h),(0,0,0,0)); s.p=s.im.load()
    def px(s,x,y,c,only=None):
        x,y=int(x),int(y)
        if 0<=x<s.w and 0<=y<s.h:
            if only=='opaque' and s.p[x,y][3]==0: return
            if only=='empty' and s.p[x,y][3]!=0: return
            s.p[x,y]=hx(c) if c is not None else (0,0,0,0)
    def get(s,x,y): return s.p[x,y] if 0<=x<s.w and 0<=y<s.h else (0,0,0,0)
    def rect(s,x,y,w,h,c,only=None):
        for yy in range(int(y),int(y+h)):
            for xx in range(int(x),int(x+w)): s.px(xx,yy,c,only)
    def hline(s,x,y,w,c,only=None): s.rect(x,y,w,1,c,only)
    def vline(s,x,y,h,c,only=None): s.rect(x,y,1,h,c,only)
    def line(s,x0,y0,x1,y1,c,only=None):
        x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); dx,dy=abs(x1-x0),-abs(y1-y0); sx=1 if x0<x1 else -1; sy=1 if y0<y1 else -1; e=dx+dy
        while True:
            s.px(x0,y0,c,only)
            if x0==x1 and y0==y1: break
            e2=2*e
            if e2>=dy: e+=dy; x0+=sx
            if e2<=dx: e+=dx; y0+=sy
    def ellipse(s,cx,cy,rx,ry,c,only=None):
        for yy in range(int(cy-ry-1),int(cy+ry+2)):
            for xx in range(int(cx-rx-1),int(cx+rx+2)):
                if ((xx+.5-cx)/max(rx,.01))**2+((yy+.5-cy)/max(ry,.01))**2<=1: s.px(xx,yy,c,only)
    def poly(s,pts,c):
        m=Image.new('L',(s.w,s.h),0); ImageDraw.Draw(m).polygon([tuple(p) for p in pts],fill=255); mp=m.load()
        for y in range(s.h):
            for x in range(s.w):
                if mp[x,y]: s.px(x,y,c)
    def noise(s,x,y,w,h,c,d,seed,only='opaque'):
        r=random.Random(seed)
        for yy in range(int(y),int(y+h)):
            for xx in range(int(x),int(x+w)):
                if r.random()<d: s.px(xx,yy,c,only)
    def outline(s,c,diag=False):
        c=hx(c); todo=[]; nb=[(1,0),(-1,0),(0,1),(0,-1)]+([(1,1),(1,-1),(-1,1),(-1,-1)] if diag else [])
        for y in range(s.h):
            for x in range(s.w):
                if s.p[x,y][3]==0 and any(s.get(x+dx,y+dy)[3]>0 and s.get(x+dx,y+dy)[:3]!=c[:3] for dx,dy in nb): todo.append((x,y))
        for x,y in todo: s.p[x,y]=c
    def paste(s,o,x,y,flip=False):
        im=o.im if isinstance(o,Cv) else o
        if flip: im=im.transpose(Image.FLIP_LEFT_RIGHT)
        s.im.alpha_composite(im,(int(x),int(y)))
    def flip(s):
        n=Cv(s.w,s.h); n.paste(s,0,0,True); return n
