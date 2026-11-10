import base64,json,re,sys,os
d=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(d,'src.html')).read()
img=sys.argv[1]
mp={}
ids={int(n) for n in re.findall(r'\b(\d{4,5})\b',src) if os.path.exists(os.path.join(img,n+'.png'))}
for i in sorted(ids):
    f=os.path.join(img,f'{i}.png')
    if not os.path.exists(f): print('MISSING',i); continue
    mp[str(i)]='data:image/png;base64,'+base64.b64encode(open(f,'rb').read()).decode()
print(len(mp),'pictos')
out=src.replace('"__PICTOS__"',json.dumps(mp))
out=out.replace('/*__JSPDF__*/', open(os.path.join(d,'jspdf.umd.min.js')).read())
vj=sys.argv[4] if len(sys.argv)>4 else None
out=out.replace('"__VOICE__"', open(vj).read() if vj else '{}')
open(sys.argv[2],'w').write(out)
open(sys.argv[3],'w').write('<!doctype html>\n<html lang="ca">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'+out+'\n</html>\n')
print(os.path.getsize(sys.argv[2])//1024,'KB')
