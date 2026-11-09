# Mira i Brilla ✨

Joc kawaii per practicar el control amb la mirada (Tobii + TD Control). És per a una nena que va amb el seu **pony**, un caminador Motilo amb corsé a mida, i a qui li agraden molt el rosa i l'Aitana. Després de jugar, la pantalla final recull en pictogrames ARASAAC el que ha fet, per poder-ne parlar amb el comunicador.

**Jugar:** obriu `index.html` amb Chrome o Edge. És un sol fitxer: els pictogrames i la veu ja hi van a dins, i funciona sense internet.

## Jocs
1. **Passeig amb el pony.** Mira l'estrella i la nena hi va caminant amb el pony per agafar-la.
2. **Encén el concert.** El joc diu què ha de buscar («Busca el globus!») i ensenya el pictograma. Només reacciona l'objecte demanat. Al final hi ha un concert.
3. **Vesteix-te d'estrella.** Tria el pentinat, el vestit, les sabates, què porta al cap, el color del pony i els adhesius. Després li fan una foto i li pregunten coses sobre la foto, amb respostes en pictogrames.

També hi ha l'opció **Tots els jocs**, que els juga seguits. Sempre s'acaba amb la pantalla **«Què he fet avui?»**.

## Configuració (botó ⚙ a la pantalla inicial)
- Temps de mirada (0,3–5 s), tolerància si la mirada surt un moment, i com s'activa: mirant, amb el clic de TD Control o de les dues maneres.
- De 2 a 8 opcions per triar i de 2 a 8 respostes a les preguntes.
- Quines coses pot triar al Joc 3, i quants objectes hi ha i quants ha de buscar al Joc 2.
- Nom de la nena, idioma (català o castellà), veu, mida dels objectes, i el cercle i el punt de mirada.
- Una cançó i una foto pròpies per al concert. Es guarden només en aquell navegador.

Durant el joc, els botons «⌂ Inici» i «⏭ Següent» són per a l'adult i només funcionen amb clic.

## Codi font (`codi-font/`)
- `src.html`: el joc, sense els pictogrames ni la veu.
- `build.py`: posa els pictogrames i la veu dins del fitxer i genera `index.html`.
- `synth.py` i `phrases.json`: generen els àudios de totes les frases amb la veu Ona (Piper).
- `frases.js`: extreu del joc la llista de frases.

## Crèdits
- **Pictogrames:** Sergio Palao. Origen: ARASAAC (https://arasaac.org). Llicència: CC BY-NC-SA. Propietat: Govern d'Aragó.
- **Veu:** Ona, del projecte Festcat (UPC), en la versió per al motor de veu Piper (`ca_ES-upc_ona-medium`). Consulteu-ne la llicència a la fitxa del model.
- Les il·lustracions de la nena, del pony i dels escenaris són pròpies del joc.

Ús educatiu i sense ànim de lucre.
