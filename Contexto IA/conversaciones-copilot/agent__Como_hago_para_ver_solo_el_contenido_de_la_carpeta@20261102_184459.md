---
epoch: 1793655899871
mode: agent
backendId: claude
sessionId: "a968ca04-041a-4b04-93a3-935b235d2a85"
agentLabel: "Como hago para ver solo el contenido de la carpeta en que me…"
usage: '{"usedTokens":26054,"contextWindow":1000000,"inputTokens":4,"outputTokens":2,"cacheReadTokens":17391,"cacheWriteTokens":8657,"updatedAt":1793655983206}'
tags:
  - copilot-conversation
---

**user**: Como hago para ver solo el contenido de la carpeta en que me encuentro en el explorador de archivos por ejemplo "Parcial 2 - Contenidos "
[Timestamp: 2026/11/02 18:44:59]

**ai**: Tienes dos formas de hacerlo en Obsidian:

**Opción 1: "Enfocar" una carpeta (Focus)**
Esta es la opción más directa si quieres que el explorador muestre solo el contenido de esa carpeta.

1. Haz clic derecho sobre la carpeta (por ejemplo, "Parcial 2 - Contenido").
2. Busca una opción como **"Enfocar en esta carpeta"** o **"Focus on folder"**. Esta opción aparece si tienes instalado un plugin comunitario como **Folder Focus** o **Focus Folder in File Explorer**.

Obsidian por sí solo no trae esta función de forma nativa, así que necesitarás el plugin:

1. Ve a **Ajustes → Complementos de la comunidad → Explorar**.
2. Busca **"Folder Focus"** (o "Focus Folder"), instálalo y actívalo.
3. Luego, haz clic derecho en la carpeta y elige la opción de enfocar.

**Opción 2: Usar el botón de "Mostrar archivo actual" (sin plugin)**
Esto no oculta el resto, pero te ayuda a ubicarte:

- Arriba en el explorador hay un botón para **"Revelar el archivo actual en el explorador"**.
- Combínalo con el botón de **"Colapsar todo"** (la flecha doble hacia arriba, `⌃`, que ya tienes en la barra superior) para dejar cerradas todas las carpetas excepto la que te interesa.

**Opción 3: Abrir la carpeta como vault aparte**
Si realmente quieres aislar una carpeta, puedes abrirla como una bóveda independiente (**Abrir otra bóveda → Abrir carpeta como bóveda**). La desventaja es que pierdes los enlaces a notas fuera de esa carpeta.

No estoy seguro del nombre exacto que tiene el plugin en tu versión de Obsidian, así que si no lo encuentras al buscarlo, dime y lo revisamos juntos.
[Timestamp: 2026/11/02 18:44:59]

**user**: tengo solo estas opciones
[Timestamp: 2026/11/02 18:46:18]

**ai**: Correcto: ese menú es el nativo de Obsidian y no incluye "Enfocar". Esa opción solo aparece si instalas un plugin de la comunidad.

**Lo que puedes hacer ahora mismo, sin plugin:**

1. Pulsa el botón de **Colapsar todo** (la flecha doble `⌃` de la barra superior del explorador). Así quedan cerradas todas las carpetas.
2. Abre solo la carpeta que te interesa, por ejemplo "Parcial 2 - Contenido".

Con eso ves solo su contenido desplegado, aunque el resto de carpetas siguen apareciendo cerradas en la lista.

**Para ocultar de verdad lo demás, necesitas un plugin:**

1. Ve a **Ajustes → Complementos de la comunidad**. Si está desactivado el modo restringido, pulsa **Activar complementos de la comunidad**.
2. Pulsa **Explorar** y busca "focus folder" o "folder focus" (también puedes probar "Notebook Navigator" o "Folder Notes").
3. Instala y activa el que te aparezca. Después, el clic derecho en la carpeta mostrará la opción de enfocar.

No puedo asegurarte cuál es el nombre exacto del plugin en el catálogo actual, así que revisa lo que te salga en la búsqueda.

**Alternativa nativa:** el botón **Buscar en la carpeta** de tu menú abre una búsqueda limitada a esa carpeta (`path:"Parcial 2 - Contenido"`). Te muestra solo los archivos de ahí, en la barra lateral de búsqueda.
[Timestamp: 2026/11/02 18:46:18]