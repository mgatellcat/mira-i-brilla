import json, sys, os, wave, base64, subprocess
from piper import PiperVoice
from piper.config import SynthesisConfig

phrases = json.load(open(sys.argv[1]))
outdir = sys.argv[2]
os.makedirs(outdir, exist_ok=True)
v = PiperVoice.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ca_ES-upc_ona-medium.onnx'))
# a touch slower and more expressive for a child
cfg = SynthesisConfig(length_scale=1.08, noise_scale=0.667, noise_w_scale=0.8)
mp = {}
for i, ph in enumerate(phrases):
    wav = os.path.join(outdir, f'{i:03d}.wav')
    ogg = os.path.join(outdir, f'{i:03d}.ogg')
    with wave.open(wav, 'wb') as w:
        v.synthesize_wav(ph, w, syn_config=cfg)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-af', 'silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,loudnorm=I=-16:TP=-1.5',
                    '-ar', '24000', '-ac', '1', '-c:a', 'libopus', '-b:a', '32k', ogg], check=True)
    mp[ph] = 'data:audio/ogg;base64,' + base64.b64encode(open(ogg, 'rb').read()).decode()
json.dump(mp, open(sys.argv[3], 'w'), ensure_ascii=False)
print(len(mp), 'clips', os.path.getsize(sys.argv[3]) // 1024, 'KB')
