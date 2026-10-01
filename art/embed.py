# Injects art/atlas.png + atlas.json into index.html between the ATLAS markers.
import base64,json,re,os
D=os.path.dirname(os.path.abspath(__file__)); H=os.path.join(D,'..','index.html')
b64=base64.b64encode(open(os.path.join(D,'atlas.png'),'rb').read()).decode(); M=open(os.path.join(D,'atlas.json')).read()
blk=f'<script id="atlas">/*ATLAS*/window.ATLAS_SRC="data:image/png;base64,{b64}";window.ATLAS_MAP={M};/*/ATLAS*/</script>\n'
s=open(H).read()
if '<script id="atlas">' in s: s=re.sub(r'<script id="atlas">.*?</script>\n',lambda m:blk,s,flags=re.S)
else: s=s.replace('<script>\n',blk+'<script>\n',1)
open(H,'w').write(s); print('embedded',len(b64)//1024,'KB')
