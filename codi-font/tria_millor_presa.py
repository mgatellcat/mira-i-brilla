"""Pick, for every phrase, the take that Whisper understands best. usage: pick_best.py phrases.json takesdir clips.json report.txt"""
import sys, os, json, re, glob, base64, subprocess, difflib
import numpy as np
from faster_whisper import WhisperModel
phrases = json.load(open(sys.argv[1])); d = sys.argv[2]
asr = WhisperModel('small', device='cpu', compute_type='int8')
NUM = ['zero','una','dues','tres','quatre','cinc','sis','set','vuit','nou','deu','onze','dotze','tretze','catorze','quinze','setze','disset','divuit','dinou','vint']
def norm(t):
    t = re.sub(r'\d+', lambda x: NUM[int(x.group())] if int(x.group()) <= 20 else x.group(), t).lower().replace('’', "'")
    t = re.sub(r"[^\w' ]", ' ', t); return ' '.join(t.split())
def load(f):
    raw = subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)
mp, rep, exact, tot = {}, [], 0, 0
for i, ph in enumerate(phrases):
    best = None
    for f in sorted(glob.glob(os.path.join(d, f'{i:03d}_*.ogg'))):
        segs, _ = asr.transcribe(load(f), language='ca', beam_size=5)
        h = ''.join(s.text for s in segs).strip()
        sc = difflib.SequenceMatcher(None, norm(ph), norm(h)).ratio()
        if best is None or sc > best[0]: best = (sc, f, h)
        if sc == 1.0: break
    exact += best[0] == 1.0; tot += best[0]
    rep.append(f'{best[0]:.2f}\t{ph}\t=> {best[2]}')
    mp[ph] = 'data:audio/ogg;base64,' + base64.b64encode(open(best[1], 'rb').read()).decode()
json.dump(mp, open(sys.argv[3], 'w'), ensure_ascii=False)
open(sys.argv[4], 'w').write('\n'.join(rep))
print('EXACT', exact, 'of', len(phrases), 'MEAN', tot / len(phrases))
