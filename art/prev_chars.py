from chars import *
names=list(LOOKS); out=Cv(W*12,H*len(names))
for i,n in enumerate(names):
    for j,(d,f) in enumerate([(d,f) for d in 'dsu' for f in range(4)]):
        out.paste(char(LOOKS[n],d,f),j*W,i*H)
bg=Image.new('RGBA',out.im.size,(214,176,118,255)); bg.alpha_composite(out.im)
bg.resize((bg.width*4,bg.height*4),Image.NEAREST).save('prev_chars.png')
