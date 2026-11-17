"""Monographic communication board for «Mira i Brilla» (3 A4 landscape pages).
Organisation: CACE-UTAC semantic categories, ordered left to right like a sentence (who -> does -> what -> how ->
expressions -> questions), with the Fitzgerald colour key used by ARASAAC on the pictogram frames.
usage: build_plafo.py <pictogram dir> <out.html>"""
import sys, os, base64, html

IMG = sys.argv[1]
COL = {'P': '#f2c500', 'V': '#2fae4e', 'N': '#f08a1c', 'Q': '#1e44b0', 'S': '#d6339a', 'M': '#9a9aa6'}
LEG = [('P', 'Persones i pronoms'), ('V', 'Accions (verbs)'), ('N', 'Noms: objectes, roba, llocs'), ('Q', 'Qualitats: colors, com és, com em sento'), ('S', 'Expressions socials'), ('M', 'Preguntes, temps i altres')]

# each page: title, subtitle, list of blocks (CACE category, colour, cells top-to-bottom, columns)
PAGES = [
 ('Parlem de Mira i Brilla', 'Plafó general de l’activitat', [
   ('Persones', 'P', [('JO',2617),('TU',2608),('ELL',6480),('ELLA',7028),('NOSALTRES',7183),('VOSALTRES',7306),
                      ('ELLS',7032),('ELLES',7030),('NENA',2484),('NEN',2485),('MESTRA',2456),('FISIO',2395)]),
   ('Accions', 'V', [('JUGAR',2439),('MIRAR',2474),('TRIAR',30510),('VOLER',5441),('DESCANSAR',3299),('SER',5581),
                     ('CAMINAR',3251),('CANTAR',2315),('BALLAR',2652),('VESTIR',2781),('TENIR',7271),('ESCOLTAR',2381)]),
   ('Objectes, aparells i activitats', 'N', [('JOC D’ORDINADOR',29153),('ORDINADOR',2487),('ULLS',2876),('PONY',25800),('ESTRELLA',2752),('CONCERT',11586),
                     ('ROBA',7233),('FOTO',7107),('FITXA',11263),('CANÇÓ',38000),('ROCK',38704),('CANTANT',11201)]),
   ('Sentiments', 'Q', [('CONTENT/A',9907),('DIVERTIT',24735),('CANSAT/DA',2314),('ENFADAT/DA',2374),('FÀCIL',4645),('DIFÍCIL',4629)]),
   ('Expressions', 'S', [('SÍ',5584),('NO',5526),('M’AGRADA',38891),('NO M’AGRADA',38890),('MÉS',3220),('JA ESTÀ',28429),
                         ('MOLT BÉ',38564),('UNA ALTRA VEGADA',37162),('AJUDA',12252),('NO HO SÉ',7180),('HOLA',6009),('ADÉU',5896)]),
   ('Preguntes i temps', 'M', [('QUÈ?',22620),('QUI?',9853),('ON?',7764),('AVUI',7131),('ARA',13026),('NO TINC LA PARAULA',9851)]),
 ]),
 ('Vestir-me d’estrella o de rocker', 'Joc 3 · Vesteix-te', [
   ('Persones', 'P', [('JO',2617),('TU',2608),('ELL',6480),('ELLA',7028),('NENA',2484),('NEN',2485)]),
   ('Accions', 'V', [('PORTAR',32135),('POSAR',6989),('TREURE',5568),('TRIAR',30510),('SER',5581),('TENIR',7271)]),
   ('Roba i calçat', 'N', [('VESTIT',2613),('TUTÚ',2653),('SAMARRETA',2309),('FALDILLA',2391),('PANTALONS',2565),('JERSEI',2436),
                           ('DESSUADORA',8701),('JAQUETA',23921),('SABATES',2622),('VAMBES',2621),('BOTES',2667),('SANDÀLIES',2556)]),
   ('Complements Aitana', 'N', [('CORONA',2718),('DIADEMA',3304),('LLAÇ',2946),('FLOR',3102),('COLLARET',2347),('ARRACADES',2515)]),
   ('Complements Rock', 'N', [('GUITARRA ELÈCTRICA',8599),('MOCADOR',5417),('GORRA',2411),('ULLERES DE SOL',3330),('BANYES DE DIABLE',8549),('POLSERA',2537)]),
   ('Cabells', 'N', [('CABELLS',2851),('CUA',5429),('DUES CUES',2484),('TRENA',5599),('MONYO',26230),('CRESTA',7069)]),
   ('Colors', 'Q', [('ROSA',2807),('BLAU',4869),('LILA',2940),('VERMELL',2808),('GROC',2648),('VERD',4886),
                    ('TARONJA',2888),('NEGRE',2886),('BLANC',8043),('GRIS',3340),('DAURAT',2739),('COLOR',5968)]),
   ('Com és', 'Q', [('LLARG',4675),('CURT',4615),('ARRISSAT',26392),('MACO/A',4660),('IGUAL',4667),('DIFERENT',4628)]),
   ('Expressions', 'S', [('M’AGRADA',38891),('NO M’AGRADA',38890),('SÍ',5584),('NO',5526),('MÉS',3220),('JA ESTÀ',28429)]),
 ]),
 ('El passeig i el concert', 'Joc 1 · Passeig amb el pony   ·   Joc 2 · Encén el concert', [
   ('Persones', 'P', [('JO',2617),('TU',2608),('NOSALTRES',7183),('CANTANT',11201),('AMIC',8487),('AMIGA',8486)]),
   ('Accions', 'V', [('CAMINAR',3251),('PASSEJAR',8649),('MIRAR',2474),('BUSCAR',6946),('TROBAR',5990),('AGAFAR',10148),
                     ('CANTAR',2315),('BALLAR',2652),('TOCAR LA GUITARRA',8709),('TOCAR LA BATERIA',23819),('APLAUDIR',4563),('FER UNA FOTO',37806)]),
   ('El passeig', 'N', [('PARC',2859),('PONY',25800),('ESTRELLA',2752),('LLUNA',2933),('LLAMP',2819),('NIT',35789)]),
   ('El concert', 'N', [('CONCERT',11586),('ESCENARI',8106),('MICRÒFON',2912),('GUITARRA',2417),('GUITARRA ELÈCTRICA',8599),('BATERIA',5923),
                        ('PIANO',2521),('TAMBOR',2578),('ALTAVEU',8336),('LLUM',10321),('CANÇÓ',38000),('ROCK',38704)]),
   ('Sentiments', 'Q', [('CONTENT/A',9907),('DIVERTIT',24735),('CANSAT/DA',2314),('TRIST/A',2606),('NERVIÓS/A',11312),('AVORRIT/DA',2245)]),
   ('Expressions', 'S', [('SÍ',5584),('NO',5526),('M’AGRADA',38891),('NO M’AGRADA',38890),('MOLT BÉ',38564),('UNA ALTRA VEGADA',37162)]),
   ('Preguntes i temps', 'M', [('ON?',7764),('QUÈ?',22620),('AVUI',7131),('AHIR',6926),('DESPRÉS',13080),('NO TINC LA PARAULA',9851)]),
 ]),
]
ROWS = 6

def uri(i):
    return 'data:image/png;base64,' + base64.b64encode(open(os.path.join(IMG, f'{i}.png'), 'rb').read()).decode()

css = """
@page{size:A4 landscape;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Nunito','Arial',sans-serif;color:#2a2230;background:#fff}
.page{width:297mm;height:210mm;padding:8mm 9mm 6mm;display:grid;grid-template-rows:auto 1fr auto;gap:3mm;page-break-after:always;break-after:page;overflow:hidden}
.page:last-child{page-break-after:auto;break-after:auto}
header{display:flex;align-items:baseline;justify-content:space-between;gap:6mm;border-bottom:.6mm solid #2a2230;padding-bottom:1.5mm}
header h1{margin:0;font:900 7.5mm/1 'Nunito','Arial',sans-serif;letter-spacing:.02em;text-transform:uppercase}
header h1 span{color:#d6339a}
header p{margin:0;font:700 3.4mm/1.2 'Nunito','Arial',sans-serif;color:#555}
.board{display:grid;grid-auto-flow:column;gap:0 2.2mm;min-height:0}
.block{display:grid;grid-template-rows:auto 1fr;gap:1mm;min-height:0}
.block h2{margin:0;font:900 2.5mm/1.1 'Nunito','Arial',sans-serif;text-transform:uppercase;letter-spacing:.03em;text-align:center;padding:.5mm 1mm;border-radius:1.2mm;color:#fff;min-height:6.4mm;display:flex;align-items:center;justify-content:center;text-wrap:balance}
.cells{display:grid;grid-template-rows:repeat(6,minmax(0,1fr));grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);gap:1.6mm;min-height:0}
.cell{border:1.1mm solid;border-radius:2.2mm;background:#fff;display:grid;grid-template-rows:auto minmax(0,1fr);align-items:center;justify-items:center;padding:.8mm .6mm 1mm;min-height:0;min-width:0}
.cell b{font:900 2.75mm/1.05 'Nunito','Arial',sans-serif;text-align:center;letter-spacing:.01em;min-height:3mm;display:flex;align-items:center}
.cell img{width:100%;height:100%;object-fit:contain;min-height:0}
.cell.empty{border-style:dashed;border-width:.4mm;border-color:#ccc}
footer{display:flex;justify-content:space-between;align-items:center;gap:4mm;font:700 2.3mm/1.25 'Nunito','Arial',sans-serif;color:#555}
.legend{display:flex;gap:3mm;flex-wrap:wrap}
.legend i{display:inline-block;width:3.4mm;height:3.4mm;border:.8mm solid;border-radius:.8mm;vertical-align:-0.8mm;margin-right:1mm}
"""
out = ['<!doctype html><html lang="ca"><meta charset="utf-8"><title>Plafó Mira i Brilla</title>',
       '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;900&display=swap">',
       f'<style>{css}</style><body>']
for n, (title, sub, blocks) in enumerate(PAGES, 1):
    out.append('<section class="page">')
    out.append(f'<header><h1>Mira <span>i</span> Brilla · {html.escape(title)}</h1><p>{html.escape(sub)} · Plafó {n} de {len(PAGES)}</p></header>')
    cols = sum(-(-len(c) // ROWS) for _, _, c in blocks)
    out.append(f'<div class="board" style="grid-template-columns:{" ".join(f"{-(-len(c)//ROWS)}fr" for _,_,c in blocks)}">')
    for name, k, cells in blocks:
        ncol = -(-len(cells) // ROWS)
        out.append(f'<div class="block"><h2 style="background:{COL[k]}">{html.escape(name)}</h2><div class="cells">')
        for label, pid in cells:
            out.append(f'<div class="cell" style="border-color:{COL[k]}"><b>{html.escape(label)}</b><img alt="" src="{uri(pid)}"></div>')
        for _ in range(ncol * ROWS - len(cells)):
            out.append('<div class="cell empty"></div>')
        out.append('</div></div>')
    out.append('</div>')
    out.append('<footer><div class="legend">' + ''.join(f'<span><i style="border-color:{COL[k]}"></i>{html.escape(t)}</span>' for k, t in LEG) + '</div>'
               '<div>Pictogrames: Sergio Palao. Origen: ARASAAC (arasaac.org). Llicència: CC BY-NC-SA. Propietat: Govern d’Aragó.<br>'
               'Organització segons el vocabulari CACE-UTAC (UTAC, Universitat de Barcelona) i la clau de colors Fitzgerald.</div></footer>')
    out.append('</section>')
out.append('</body></html>')
open(sys.argv[2], 'w').write('\n'.join(out))
print('ok', sum(len(c) for _, _, b in PAGES for _, _, c in b), 'cells')
