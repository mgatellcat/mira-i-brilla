# Mira i Brilla ✨

Joc kawaii per practicar el control amb la mirada (Tobii + TD Control). És per a una nena que va amb el seu **pony**, un caminador Motilo amb corsé a mida, i a qui li agraden molt el rosa i l'Aitana. Fa servir pictogrames ARASAAC per poder parlar després de l'activitat amb el comunicador.

**Jugar:** obriu `index.html` amb Chrome o Edge. És un sol fitxer: els pictogrames i la veu ja hi van a dins, i funciona sense internet.

## Jocs
1. **Passeig amb el pony.** Mira l'estrella i la nena s'hi gira de perfil i hi va caminant amb el pony (mou les cames i giren les rodes).
2. **Encén el concert.** A l'escenari hi ha pictogrames ARASAAC de colors, roba i instruments, sempre visibles. El joc diu què ha de buscar («Busca la guitarra!») i ensenya el pictograma. Només reacciona el que se li demana: li cau el focus, balla i surten estrelles. Al final hi ha un concert.
3. **Vesteix-te d'estrella.** Amb opcions que són només pictogrames ARASAAC, tria el pentinat, el vestit, les sabates, què porta al cap, el color del pony i els adhesius. Després li fan una foto, que queda a l'esquerra, i a la dreta li pregunten què ha triat («Quin pentinat has triat?») amb 4, 6 o 8 opcions en pictogrames ARASAAC. Si encerta, la nena de la foto balla i surten estrelles. Si s'equivoca, el joc diu «Mira bé la foto i torna-ho a intentar!».

   Al costat de la nena hi ha el botó **«Descansar la mirada»**. Mentre està en pausa, la mirada no tria res i pot mirar les opcions amb calma. Es torna a activar mirant el botó, tocant-lo a la pantalla o amb el ratolí.

També hi ha l'opció **Tots els jocs**, que els juga seguits. En acabar, el joc la felicita i torna a l'inici.

## Configuració (botó ⚙ a la pantalla inicial)
- Temps de mirada (0,3–5 s), tolerància si la mirada surt un moment, i com s'activa: mirant, amb el clic de TD Control o de les dues maneres.
- Joc 3: 4, 6 o 8 opcions per triar i 4, 6 o 8 respostes a les preguntes.
- El **rosa** surt sempre entre els colors del pony i del vestit (es pot desactivar).
- Quines coses pot triar al Joc 3. Al Joc 2, quin vocabulari surt a l'escenari (colors, roba, instruments), quants pictogrames hi ha i quants n'ha de buscar.
- Nom de la nena, idioma (català o castellà), veu, mida dels objectes, i el cercle i el punt de mirada.
- Una cançó i una foto pròpies per al concert. Es guarden només en aquell navegador.

Cada vegada que s'obre el programa, la nena comença amb la roba inicial; el que tria es manté fins que es tanca.

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
