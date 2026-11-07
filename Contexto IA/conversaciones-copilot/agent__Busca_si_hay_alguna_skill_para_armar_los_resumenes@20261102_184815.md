---
epoch: 1793656095402
mode: agent
backendId: claude
sessionId: "dd1b0665-bd24-4ca3-ad51-65eb51bee78b"
agentLabel: "Busca si hay alguna skill para armar los resumenes"
usage: '{"usedTokens":33339,"contextWindow":1000000,"inputTokens":2,"outputTokens":870,"cacheReadTokens":31380,"cacheWriteTokens":1087,"updatedAt":1793656167046}'
tags:
  - copilot-conversation
---

**user**: Busca si hay alguna skill para armar  los resumenes
[Timestamp: 2026/11/02 18:48:15]

**ai**: No hay ninguna skill pensada específicamente para armar resúmenes. Busqué en las skills disponibles y en las carpetas `.claude/skills` y `copilot/skills` del vault.

**Skills que sirven para resumir según la fuente**
- `copilot-read-pdf` extrae el texto de un PDF en Markdown. Es la más útil para resumir apuntes, papers o diapositivas de la facultad.
- `copilot-web-fetch` lee una página web como Markdown, para resumir artículos o documentación.
- `copilot-youtube-transcript` obtiene la transcripción de un video, para resumir clases o charlas.
- `copilot-fetch-x` trae el texto de un post de X.

**Skills que sirven para dar formato al resumen**
- `obsidian-markdown` aplica la sintaxis de Obsidian: wikilinks, callouts, propiedades y tags.
- `obsidian-bases` sirve si querés una vista tipo tabla de todos tus resúmenes, filtrada por materia o fecha.
- `json-canvas` sirve para mapas conceptuales o esquemas visuales.

Los resúmenes en sí los hago yo directamente, usando una de esas skills para obtener el contenido y `obsidian-markdown` para el formato.

Si querés un formato fijo, por ejemplo con secciones como conceptos clave, definiciones, patrones y preguntas de repaso para Diseño de Sistemas, puedo crear una skill propia con `skill-creator`. También puedo escribir ese formato en un `AGENTS.md` dentro de esta carpeta, que es más simple. ¿Cuál preferís?
[Timestamp: 2026/11/02 18:48:15]

**user**: Necesito generar un prompt para crear una skill , para armar los resumenes de esta materia ayudame con eso
[Timestamp: 2026/11/02 18:49:07]

**ai**: Miré tu carpeta y tu `Resumen Clases.md`, así que el prompt ya usa tu estilo real: frontmatter con tags, callout `abstract` de idea central, esquemas en bloques de texto, ejemplos concretos y diagramas embebidos. Pegalo tal cual en una conversación con la skill `skill-creator`:

````text
Quiero que crees una skill llamada `resumen-diseno-sistemas` para armar resúmenes de estudio de la materia "Diseño de Sistemas" dentro de mi vault de Obsidian.

## Cuándo debe activarse
Cuando le pida resumir, armar o actualizar un resumen de una clase, unidad, tema o parcial de Diseño de Sistemas. También cuando pase un PDF, apunte, transcripción de video o página web de la materia y pida resumirlo.

## Fuentes que debe poder usar
- Notas del vault (Unidad 1.md, Unidad 2.md, apuntes de clase, borradores, etc.). Leer siempre la nota antes de resumirla.
- PDFs: usar la skill `copilot-read-pdf`.
- Páginas web: usar `copilot-web-fetch`.
- Videos de YouTube: usar `copilot-youtube-transcript`.
- Si hay varias fuentes sobre un mismo tema, combinarlas y señalar contradicciones.

## Contenido de la materia
Temas típicos: cualidades del software, cohesión y acoplamiento, componentes y paquetes, capas lógicas y físicas, patrones de diseño, DTO y DAO, casos de uso, diagramas UML (clases, secuencia, despliegue, máquina de estados), entidad-relación y PlantUML. Usar terminología rigurosa y consistente con la cátedra.

## Formato de salida (nota de Obsidian en español)
1. Frontmatter con `title`, `date` (fecha de hoy) y `tags: [diseño-de-sistemas, resumen]`, más un tag por unidad o tema (por ejemplo `unidad-3`) y `parcial` si corresponde.
2. Un callout `> [!abstract] Idea central` con 2-3 líneas.
3. Una sección "Mapa general" con un esquema en bloque ```text (jerarquía o flujo).
4. Secciones numeradas por concepto. En cada una:
   - Definición en una oración, con los términos clave en **negrita**.
   - Viñetas cortas con características, ventajas y desventajas.
   - Un ejemplo concreto (preferentemente del dominio de alquiler de autos, que es el que usamos en la materia).
5. Para comparaciones (por ejemplo cohesión vs. acoplamiento, DTO vs. DAO), usar tablas.
6. Callouts para lo importante: `[!warning]` para errores comunes y trampas de parcial, `[!tip]` para trucos de memoria.
7. Al final, una sección "Preguntas de repaso" con 5-8 preguntas tipo parcial, y sus respuestas dentro de un callout plegable `> [!question]- Respuesta`.
8. Enlazar con wikilinks `[[ ]]` a las notas relacionadas del vault (otras unidades, diagramas, ejercicios).

## Diagramas
- Si el tema lo amerita, generar diagramas en PlantUML (en bloque ```plantuml) siguiendo mi nota [[Sintaxis Basica de PlantUML]].
- Si ya existe una imagen o diagrama en el vault, embeberlo con `![[archivo]]` en lugar de recrearlo.

## Reglas
- Fidelidad: no inventar contenido que no esté en las fuentes. Si falta información o algo es ambiguo, marcarlo con un callout `[!question]` en vez de rellenar.
- Concisión: es un resumen para estudiar, no una copia. Priorizar definiciones, relaciones entre conceptos y lo que suele caer en parcial.
- Guardar el resultado en la carpeta `Resumenes/` con el nombre `Resumen - <tema>.md`. Si ya existe, preguntar si actualizar o crear una versión nueva; nunca sobrescribir sin avisar.
- Usar la sintaxis de Obsidian correcta (skill `obsidian-markdown`): viñetas con `- `, ecuaciones con `$...$`, títulos de notas como `[[título]]`.
- Responder siempre en español.

## Qué quiero que entregues
La carpeta de la skill con su `SKILL.md` (con `name` y `description` que describan bien cuándo activarla), y una plantilla de ejemplo en un archivo aparte (por ejemplo `references/plantilla-resumen.md`) para que el formato sea consistente. Probala con la nota [[Unidad 1.5 Cualidades del Software]] y mostrame el resultado antes de darla por terminada.
````

Dos cosas para ajustar antes de usarlo:

- **Carpeta de destino:** `Resumenes/` y `Resumen Clases/` están casi vacías y tenés resúmenes sueltos en la raíz. Elegí una carpeta y cambiá la regla de guardado.
- **Dominio de ejemplos:** asumí el de alquiler de autos porque aparece en tu resumen. Si la cátedra usa otro, cambialo.

¿Querés que también cree la skill yo ahora con este prompt?
[Timestamp: 2026/11/02 18:49:07]