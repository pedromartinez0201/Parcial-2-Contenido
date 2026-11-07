---
name: armado-resumenes
description: Arma resúmenes de estudio en Obsidian a partir de PDFs de cátedra (presentaciones, apuntes), exámenes anteriores y el TP. Una nota por subtema con TL;DR, callouts por nivel de prioridad, tablas comparativas, diagramas Mermaid/Excalidraw y preguntas tipo parcial; más índices por unidad y un banco de preguntas. Usar cuando Pedro pida resumir una unidad, un tema o un parcial de cualquier materia, o pida "seguir con los resúmenes".
---

# Armado de resúmenes de estudio (Obsidian)

Método acordado con Pedro para armar resúmenes de parciales. Se usó primero en Diseño de Sistemas (Parcial 2: unidades 4, 5 y 6) y sirve para cualquier materia.

Para la sintaxis de Obsidian (callouts, wikilinks, embeds, propiedades) apoyarse en la skill `obsidian-markdown`.

## 1. Antes de escribir

1. **Ubicar el programa oficial** del parcial (imagen, PDF o texto con unidades, temas y bibliografía). Si existe, **manda** sobre la numeración de los archivos: define qué unidades entran y qué presentaciones corresponden a cada una. Si falta, preguntar por él o seguir los nombres de los PDFs.
2. **Leer TODO el material de la unidad** antes de escribir la primera nota, para que las conexiones entre temas sean reales:
   - Texto: `pdftotext -layout -f N -l N archivo.pdf -` página por página. Contar las palabras por página para detectar las diapositivas que son solo imagen.
   - Diapositivas que son imagen (código, diagramas): renderizar con `pdftoppm -r 80 -png` y agrupar de a 4 con `montage p-XX.png ... -tile 2x -geometry +4+4 m.png` para leerlas con Read. **No resumir una diapositiva sin haberla visto.**
   - `.docx`: `unzip -p archivo.docx word/document.xml | sed -e 's/<\/w:p>/\n/g; s/<[^>]*>//g'`.
   - La skill `copilot-read-pdf` puede no estar activa. En ese caso usar directamente las herramientas locales, sin avisar.
3. **Buscar material relacionado fuera de la carpeta de la unidad:** clases prácticas (por ejemplo, `Diagrama de Secuencia y GIT/`), el enunciado del TP y exámenes anteriores (`Exámenes/`).
4. **Cruzar con el TP:** cuando un ejemplo se pueda aplicar al TP, **verificar contra el enunciado** antes de afirmar algo (estados, CU, reglas). Ya pasó dos veces que lo supuesto no coincidía: la clave del CU025 sí se le muestra al consultor, y el cuestionario tiene el estado "Sin Contestar".

## 2. Estructura de carpetas

```
<Parcial> - Contenido/Resumenes/
├── 00 - Índice <Parcial>.md                 ← MOC general + programa oficial embebido
├── Banco de preguntas - Exámenes anteriores.md
├── Unidad N/
│   ├── UN - Índice.md                       ← tabla de subtemas + repaso rápido
│   ├── UN.1 - <Tema>.md
│   └── UN - <Práctica>.md                   ← prácticas sin número propio
```

- Nombres de nota: `UN.M - Tema` (por ejemplo, `U4.3 - Máquinas de Estado`).
- Imágenes en `Assets/` del vault, con nombre descriptivo (`U4.2 - Notacion componente.png`), embebidas con `![[...]]`.

## 3. Plantilla de cada nota de subtema

Ver `plantilla-nota.md` en esta carpeta. Orden fijo:

1. **Propiedades:** `tags` (materia, parcial, unidad-N, tema), `unidad`, `fuente` (ruta de los PDFs; lista si son varios) y `estado: en-progreso`.
2. **Navegación:** `← [[anterior]] · [[UN - Índice]] · Siguiente → [[siguiente]]`.
3. **`> [!abstract] TL;DR`:** de 4 a 7 viñetas con lo esencial.
4. **`> [!note]` de convención o fuentes:** de dónde sale el contenido y la aclaración de que los agregados propios van como `Extra`.
5. **`## Índice`** con links `[[#Encabezado]]`.
6. **Secciones numeradas** (`## 1. …`) siguiendo el orden del apunte.
7. **`## N. Preguntas tipo parcial`** con callouts plegables `> [!question]-`.
8. **Conceptos relacionados:** wikilinks a otras notas.

## 4. Convención de callouts = nivel de prioridad

Esta tabla es la que se le explicó a Pedro. **Respetarla siempre**, porque así distingue qué memorizar de qué solo entender:

| Callout | Uso | Prioridad para estudiar |
| --- | --- | --- |
| `[!abstract]` TL;DR | Lo mínimo indispensable | 🔴 Memorizar |
| `[!quote]` | **Definiciones textuales del apunte** | 🔴 Memorizar |
| `[!summary]` "Ficha" | Ficha de un patrón o concepto (intención, clasificación, aplicabilidad) | 🔴 Memorizar |
| `[!important]` | Reglas clave o algo que se preguntó en exámenes | 🔴 Memorizar |
| `[!warning]` | Trampas de V/F, confusiones típicas, errores del apunte | 🟠 Leer con atención |
| `[!danger]` / `[!bug]` | Errores comunes ("lo que NO hay que hacer") | 🟠 Entender y recordar |
| `[!tip] Extra: …` | **Agregados propios** (bibliografía, analogías, comparaciones) | 🟢 Solo entender |
| `[!example]` | Ejemplos del apunte, del TP o propios | 🟢 Entender (sirven para "ejemplifique") |
| `[!info]` / `[!note]` | Fuentes y aclaraciones | ⚪ Contexto |
| `[!question]-` | Preguntas de práctica (plegadas) | ✍️ Practicar |

Reglas asociadas:
- **Todo lo que no salga del apunte va marcado como `Extra`.** Si una sección entera depende de agregados propios (por ejemplo, diapositivas que son solo diagramas), avisarlo con un `[!warning]` al principio de la nota.
- Las **tablas comparativas** ("X vs. Y") van fuera de los callouts y son contenido 🔴. Los exámenes piden mucho "compare" y "diferencie".
- Los **bloques de código** son 🟢: alcanza con entenderlos.
- Si Pedro pide prioridad explícita, se pueden agregar marcas 🔴 🟠 🟢 en los títulos de sección. No hacerlo sin que lo pida.

## 5. Exámenes anteriores

- Mantener `Banco de preguntas - Exámenes anteriores.md` con las preguntas **ordenadas por unidad del programa actual**, la fuente (`P2 2011`, `Final 03/2012`…) y un **mapa de frecuencia y prioridad**.
- Las preguntas que salieron en exámenes se marcan con **📝** en la nota del tema, con respuesta desarrollada.
- Aclarar siempre qué preguntas **son reales** y cuáles **armé yo** (`> [!info] Origen`).
- Señalar las **respuestas incorrectas** que haya en el material recopilado (`[!bug]`) y los temas viejos que quizás ya no estén en el programa.
- Formato actual de la cátedra: múltiple opción, V/F y desarrollo. Las preguntas de práctica siguen ese formato.

## 6. Diagramas

- **Mermaid** para flujos, clases simples, estados, secuencia y comparaciones. Precauciones:
  - Títulos de `subgraph` con id y comillas: `subgraph SF["Sin fachada"]`.
  - Cuerpos de clase en `classDiagram` en **varias líneas**, no con `;`.
  - Mermaid **no** tiene clase de asociación ni notación lollipop/socket.
- **Lo que Mermaid no puede dibujar bien** (notación UML de componentes, etc.) va como **PNG de Excalidraw** en `Assets/`, nunca como ASCII. Ver la skill `excalidraw-skill`. Si `npx -y mcp-excalidraw-server` falla, usar el binario cacheado `~/.npm/_npx/*/node_modules/.bin/excalidraw-canvas` y exportar con `screenshot --scale 2 --out <ruta>`.

## 7. Reglas de formato (aprendidas)

- **Encabezados sin `:`**: rompen los links `[[Nota#Encabezado]]`. Usar ` - ` (por ejemplo, `## 4. Ejercicio guía - el Pedido`).
- Sin emojis al **principio** de un encabezado que se vaya a enlazar.
- Viñetas con `- `, wikilinks `[[título]]` sin backticks, y LaTeX con `$...$`.
- **Corregir los errores del código del apunte** (typos, código que no compila) y avisarlo en un `[!info]`.
- **Revisar el archivo antes de editar:** Pedro suele modificar secciones por su cuenta (por ejemplo, reemplazar un diagrama por su propia imagen). No revertir sus cambios.

## 8. Al terminar una unidad

1. Actualizar `UN - Índice.md`: estado ✅ de cada subtema y tablas de **repaso rápido**.
2. Actualizar `00 - Índice` y el banco de preguntas (links a las secciones con respuestas).
3. **Validar los wikilinks** con este script (desde `Resumenes/`):
   ```bash
   python3 - <<'EOF'
   import re,glob,os
   files={os.path.splitext(os.path.basename(f))[0]:f for f in glob.glob("**/*.md",recursive=True)}
   def heads(f): return [re.sub(r'^#+\s*','',l).strip() for l in open(f,encoding="utf-8") if re.match(r'^#{1,6}\s',l)]
   for name,f in files.items():
       txt=re.sub(r'```.*?```','',open(f,encoding="utf-8").read(),flags=re.S)
       for mo in re.finditer(r'!?\[\[([^\]|]+?)(?:\\?\|[^\]]*)?\]\]',txt):
           t=mo.group(1).replace('\\','');note,_,h=t.partition('#');note=note.strip() or name
           if note.endswith(('.png','.jpg')): continue
           if note not in files: print(f"{name}: falta nota -> {note}");continue
           if h and h.strip() not in heads(files[note]): print(f"{name}: falta heading -> {note}#{h}")
   EOF
   ```
   Que falten notas de unidades todavía no hechas es esperable. Que falten encabezados, no.
4. En el mensaje final a Pedro, listar las notas creadas y las **cosas para revisar**: contradicciones del material, agregados propios grandes, correcciones hechas contra el TP y archivos faltantes.

## 9. Estilo de trabajo

- Pedro dio permiso para avanzar **sin pedir confirmación** en este trabajo. Avisar en una línea qué se está haciendo y seguir.
- Responder en español rioplatense, claro y concreto.
- Ser honesto sobre las fuentes: si algo no está en el apunte, decirlo.
