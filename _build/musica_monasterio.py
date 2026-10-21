# Música del vídeo del monasterio de Didákora: un bucle «chiptune» medieval compuesto para el portfolio (original, sin licencias).
# Re dórico, 120 pulsaciones por minuto, 16 compases (32 s): la melodía sola y después con contracanto y percusión.
# Instrumentos de consola clásica: onda cuadrada (melodía y contracanto), triangular (bajo), arpegios y ruido (percusión).
# Uso: python _build/musica_monasterio.py → assets/proyectos/monasterio-didakora/musica.wav (necesita numpy)
import os, wave
import numpy as np

SR, BPM = 22050, 120
NEGRA = 60 / BPM
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTAS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
def hz(n):  # «D5», «A4»…
    return 440 * 2 ** ((NOTAS[n[0]] + 12 * (int(n[-1]) + 1) - 69) / 12)

def env(n, a=.006, r=.05, sus=.75):
    e = np.ones(n) * sus; ka, kr = int(a * SR), int(r * SR)
    e[:ka] = np.linspace(0, 1, ka); e[ka:ka + int(.04 * SR)] = np.linspace(1, sus, len(e[ka:ka + int(.04 * SR)]))
    if kr < n: e[-kr:] *= np.linspace(1, 0, kr)
    return e

def cuadrada(f, dur, duty=.25, vib=0.0):
    n = int(dur * SR); t = np.arange(n) / SR
    fase = np.cumsum(f * (1 + vib * np.sin(2 * np.pi * 5.5 * t) * np.clip(t / .25, 0, 1)) / SR)
    return np.where((fase % 1) < duty, 1.0, -1.0) * env(n)

def triangular(f, dur):
    n = int(dur * SR); fase = (np.arange(n) * f / SR) % 1
    return (4 * np.abs(fase - .5) - 1) * env(n, r=.03, sus=.9)

def ruido(dur, caida):
    n = int(dur * SR); rng = np.random.default_rng(7)
    return rng.uniform(-1, 1, n) * np.exp(-np.arange(n) / (caida * SR))

def pista(notas, instr, **kw):  # notas: [(«D5» o None, negras)]
    partes = []
    for nota, b in notas:
        d = b * NEGRA
        partes.append(np.zeros(int(d * SR)) if nota is None else instr(hz(nota), d, **kw))
    return np.concatenate(partes)

# melodía (8 compases): Dm | C | Dm | Am | F | G | Am | Dm
MEL = [("D5", 1), ("F5", .5), ("E5", .5), ("D5", 1), ("A4", 1),
       ("C5", 1), ("E5", .5), ("D5", .5), ("C5", 1), ("G4", 1),
       ("D5", .5), ("E5", .5), ("F5", .5), ("G5", .5), ("A5", 1), ("F5", 1),
       ("E5", 1.5), ("D5", .5), ("C5", 1), ("A4", 1),
       ("F5", 1), ("A5", .5), ("G5", .5), ("F5", 1), ("C5", 1),
       ("G5", 1), ("B5", .5), ("A5", .5), ("G5", 1), ("D5", 1),
       ("A5", .5), ("G5", .5), ("F5", .5), ("E5", .5), ("D5", .5), ("E5", .5), ("C5", 1),
       ("D5", 3), (None, 1)]
# contracanto (segunda vuelta): notas largas por debajo de la melodía
CONTRA = [("A4", 2), ("F4", 2), ("G4", 2), ("E4", 2), ("A4", 2), ("C5", 2), ("E4", 2), ("C4", 2),
          ("A4", 2), ("F4", 2), ("B4", 2), ("G4", 2), ("C5", 2), ("G4", 2), ("A4", 4)]
ACORDES = [("D", "F", "A"), ("C", "E", "G"), ("D", "F", "A"), ("A", "C", "E"), ("F", "A", "C"), ("G", "B", "D"), ("A", "C", "E"), ("D", "F", "A")]
BAJO = ["D3", "C3", "D3", "A2", "F2", "G2", "A2", "D3"]

def arpegios():
    notas = []
    for acorde in ACORDES:
        for i in range(8): notas.append((acorde[[0, 1, 2, 1][i % 4]] + "4", .5))
    return pista(notas, cuadrada, duty=.5)

def bajo():
    notas = []
    for b in BAJO: notas += [(b, 1), (b[0] + str(int(b[1]) + 1), .5), (b, .5), (b, 1), (b[0] + str(int(b[1]) + 1), 1)]
    return pista(notas, triangular)

def percusion(compases):
    n = int(compases * 4 * NEGRA * SR); out = np.zeros(n)
    for k in range(compases * 4):
        i = int(k * NEGRA * SR)
        golpe = ruido(.12, .02) * (.9 if k % 2 else .55)  # pandero suave a contratiempo
        out[i:i + len(golpe)] += golpe[:max(0, n - i)]
    return out

def mezcla(*capas):
    n = max(len(c) for c, _ in capas); out = np.zeros(n)
    for c, v in capas: out[:len(c)] += c * v
    return out

mel, arp, bas = pista(MEL, cuadrada, duty=.25, vib=.006), arpegios(), bajo()
vuelta1 = mezcla((mel, .20), (arp, .05), (bas, .24))
vuelta2 = mezcla((mel, .20), (pista(CONTRA, cuadrada, duty=.125), .09), (arp, .06), (bas, .26), (percusion(8), .05))
audio = np.concatenate([vuelta1, vuelta2])
audio = np.convolve(audio, np.ones(3) / 3, mode="same")  # suaviza un poco los bordes de la onda cuadrada
audio = audio / np.max(np.abs(audio)) * .7
salida = os.path.join(ROOT, "assets", "proyectos", "monasterio-didakora", "musica.wav")
with wave.open(salida, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((audio * 32767).astype("<i2").tobytes())
print(salida, f"{len(audio) / SR:.1f} s")
