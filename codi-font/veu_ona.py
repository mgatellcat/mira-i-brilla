"""Ona (Piper ca_ES-upc_ona-medium) with the ORIGINAL piper-phonemize 1.1.0 (the eSpeak NG the voice was trained with,
same converter as piper-wasm in PictoEscriu). Writes several takes per phrase: outdir/NNN_K.ogg
usage (python 3.11 venv): ona_old.py phrases.json outdir takes"""
import sys, os, json, subprocess
import numpy as np, onnxruntime as ort
from piper_phonemize import phonemize_espeak

HERE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(HERE, 'ca_ES-upc_ona-medium.onnx.json')))
MAP = cfg['phoneme_id_map']; SR = cfg['audio']['sample_rate']
inf = cfg.get('inference', {})
sess = ort.InferenceSession(os.path.join(HERE, 'ca_ES-upc_ona-medium.onnx'), providers=['CPUExecutionProvider'])

def ids_for(phonemes):
    ids = list(MAP['^']) + list(MAP['_'])
    for p in phonemes:
        if p in MAP: ids += list(MAP[p]) + list(MAP['_'])
    return ids + list(MAP['$'])

def synth(text, noise=0.667, length=1.08, noise_w=0.8):
    parts = []
    for sent in phonemize_espeak(text, cfg['espeak']['voice']):
        x = np.array([ids_for(sent)], dtype=np.int64)
        audio = sess.run(None, {'input': x, 'input_lengths': np.array([x.shape[1]], dtype=np.int64),
                                'scales': np.array([noise, length, noise_w], dtype=np.float32)})[0].squeeze()
        parts += [audio, np.zeros(int(SR * 0.12), dtype=np.float32)]
    return np.concatenate(parts)

def to_ogg(w, path):
    w = w / max(1e-6, np.abs(w).max()) * 0.9
    raw = (w * 32767).astype('<i2').tobytes()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-',
                    '-af', 'silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,loudnorm=I=-16:TP=-1.5',
                    '-ar', '24000', '-ac', '1', '-c:a', 'libopus', '-b:a', '32k', path], input=raw, check=True)

if __name__ == '__main__':
    phrases = json.load(open(sys.argv[1])); out = sys.argv[2]; takes = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    os.makedirs(out, exist_ok=True)
    noises = [0.333, 0.5, 0.667, 0.4]
    for i, ph in enumerate(phrases):
        for k in range(takes):
            to_ogg(synth(ph, noise=noises[k % len(noises)]), os.path.join(out, f'{i:03d}_{k}.ogg'))
    print('done', len(phrases))
