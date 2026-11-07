---
name: diagramas-excalidraw-png
description: Diagramas que Mermaid no puede representar → dibujarlos con Excalidraw y embeberlos como PNG en la nota
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8469ee59-0a9e-4b82-ab07-f27c16749074
  modified: 2026-11-06T02:10:11.972Z
---

Cuando un diagrama no se puede representar bien con Mermaid (ej. notación UML de componentes con lollipop/socket), dibujarlo con Excalidraw y agregarlo a la nota como imagen PNG, no como dibujo ASCII.

**Why:** Pedro lo pidió explícitamente (2026-11-03) al ver un diagrama de componentes hecho en ASCII en U4.2.

**How to apply:**
- Guardar el PNG en `Assets/` del vault (attachmentFolderPath) con nombre descriptivo, ej. `U4.2 - Notacion componente.png`, y embeber con `![[nombre.png]]`.
- `npx -y mcp-excalidraw-server` falla con "npm error Invalid Version"; usar directo el binario cacheado `~/.npm/_npx/a2c48f8a55ba023a/node_modules/.bin/excalidraw-canvas` (v2.x). Exportar con `screenshot --scale 2 --out <ruta>`.
- Si `screenshot --out` directo al vault pide permiso, exportar a `/tmp/exdraw/` y copiar con `cp`. Generar las escenas con un script Python (helpers en `/tmp/exdraw/lib.py`, puede no persistir). Las etiquetas dentro de cajas ignoran `fontSize`/`fontFamily`: cortar texto largo con `\n` o ensanchar la caja; evitar emojis.
- Revisar la nota antes de editar: Pedro suele modificar las secciones por su cuenta (ej. reemplazó una sección por su propia imagen).

Para diagramas de clases UML, Pedro también aceptó PlantUML (2026-11-05). No hay comando `plantuml`, pero sí un jar local: `java -DGRAPHVIZ_DOT=/usr/bin/dot -jar ~/.var/app/com.visualstudio.code/data/vscode/extensions/jebbs.plantuml-2.18.1/plantuml.jar -charset UTF-8 -tsvg <archivo.puml>`. Usar `<<crea>>` y no `«crea»` en las etiquetas, porque PlantUML descarta las comillas angulares; con `skinparam style strictuml`, declarar `<<interface>>` a mano.

Relacionado: [[diseno-sistemas-parcial2]]
