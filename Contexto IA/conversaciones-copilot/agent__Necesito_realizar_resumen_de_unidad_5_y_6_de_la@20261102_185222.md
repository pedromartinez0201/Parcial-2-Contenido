---
epoch: 1793656342000
mode: agent
backendId: claude
sessionId: "c21fdf90-c4bf-478f-897e-a19ee07e3fc3"
agentLabel: "Necesito realizar resumen de unidad 5 y 6 de la materia de d…"
lastAccessedAt: 1793760764887
usage: '{"usedTokens":362719,"contextWindow":1000000,"inputTokens":2,"outputTokens":812,"cacheReadTokens":360474,"cacheWriteTokens":1431,"updatedAt":1793761189964}'
tags:
  - copilot-conversation
---

**user**: Necesito realizar resumen de unidad 5 y 6 de la materia de diseño de sistemas . Me gustaria que me ayudes con eso . La idea es que me vayas guiando de como armar el resumen .  Por el momento quisiera que compactes la informacion de forma clara y concisa , buscar comprension y ejemplos utiles para poder entender cada tema . Debe ser formato markdown adaptado para obsidian por lo que tendras que usar wiki links y demas cosas utiles como indices tambien o lo que creas necesario . Me gustaria que arranquemos por Unidad 5.1
[Timestamp: 2026/11/02 18:52:22]

**ai**: Primero voy a revisar qué material tenés en la bóveda para la Unidad 5.Revisé tu bóveda y no hay material de las Unidades 5 y 6. Hay esto:

- [[Clase 16-4-26]] y [[Clase 30-4-26]]: dibujos de Excalidraw sobre captura, validación y codificación de datos (Unidad 2.2).
- `Ejemplo de Parcial/Resumen P1 - Tade.docx`: un resumen que llega hasta la **Unidad 4.1 – Modelo de Diseño en el Proceso Unificado**.
- Enunciados del TP y diagramas PlantUML.

No sé qué temas entran en la 5.1 de tu programa. Puede ser patrones de diseño (GRASP/GoF), arquitectura, persistencia u otra cosa, según la cátedra. No quiero inventarlo, así que **necesito que me pases el material de la Unidad 5.1**. Sirve cualquiera de estas formas:

- Copiar el PDF o las diapositivas a la bóveda (por ejemplo en una carpeta `Unidad 5/`) y decirme el nombre.
- Pegar el texto o el índice del programa acá en el chat.
- Decirme los temas, y lo armo con fuentes confiables que te cito.

## Propuesta de estructura (para que la revises mientras tanto)

```
Resúmenes/
├── 00 - Índice Diseño de Sistemas.md   ← nota mapa (MOC) con links a todo
├── Unidad 5/
│   ├── U5 - Índice.md                   ← mapa de la unidad
│   ├── U5.1 - <Tema>.md
│   ├── U5.2 - <Tema>.md
│   └── ...
└── Unidad 6/
    └── ...
```

Cada nota de subtema tendría:

- **Propiedades** (`tags: [diseño-sistemas, unidad-5]`, `unidad: 5.1`, `estado: en-progreso`) para filtrar y armar una vista con Bases.
- **TL;DR**: 3 o 4 líneas con lo esencial.
- **Conceptos clave**: definiciones cortas y claras.
- **Ejemplos** en callouts (`> [!example]`), si se puede con casos parecidos a tu TP (gestión de evaluaciones de perfiles).
- **Comparaciones en tablas** cuando haya conceptos que se confunden.
- **Diagramas** en Mermaid (se ven directo en Obsidian) cuando ayuden.
- **Preguntas tipo parcial** en callouts plegables (`> [!question]-`). Las armo al estilo de los ejemplos que tenés: verdadero/falso, múltiple opción y "describa…".
- **Wikilinks** a conceptos relacionados, por ejemplo [[U4.1 - Modelo de Diseño en el Proceso Unificado]] o [[Acoplamiento y Cohesión]], para conectar con lo que ya viste.

Pasame el material de la 5.1 y arranco con esa nota y el índice de la Unidad 5. Si querés otra estructura (todo en una sola nota por unidad, por ejemplo), decime y la adapto.
[Timestamp: 2026/11/02 18:52:22]

**user**: Esta es la ubicacion de la 5.1 Parcial 2 - Contenido/Unidad 5/Diseño de Sistemas - Unidad 5.1 - Patrones de Diseño.pdf me gustaria que generes esa estructura que mencionas en Parcial 2 - Contenido/Resumenes
[Timestamp: 2026/11/02 18:56:41]

**ai**: Varias diapositivas (resolución del ejercicio, estructura de State) son imágenes; las reviso para no perder el código.Ya leí las 28 diapositivas, incluido el código que venía como imagen. En tu TP encontré un ejemplo que encaja con State: los estados del Cuestionario. Ahora creo las notas.Armé la estructura en `Parcial 2 - Contenido/Resumenes/` y la nota completa de la 5.1.

## Estructura creada

```
Resumenes/
├── 00 - Índice Parcial 2.md          ← mapa general con links a las unidades
├── Unidad 5/
│   ├── U5 - Índice.md                ← tabla de subtemas y estado de cada uno
│   └── U5.1 - Patrones de Diseño.md  ← ✅ completa
└── Unidad 6/
    └── U6 - Índice.md                ← tabla 6.1 / 6.2 / 6.3
```

En los índices ya dejé los links a las notas que faltan, como [[U5.2 - Patrones de Diseño II]], [[U5.4 - SOLID]] o [[U6.1 - Pruebas]]. En Obsidian aparecen en gris hasta que las creemos, así ves de un vistazo qué falta.

## Qué tiene [[U5.1 - Patrones de Diseño]]

- **TL;DR** y un índice con links a cada sección.
- **Qué es un patrón**, para qué sirve y qué no busca, en tabla comparativa.
- **Categorías** (arquitectura, diseño, dialectos) y **clasificación** (creación, estructurales, comportamiento), con un truco para recordarla.
- **Ejercicio del Pedido**:
  - Diagrama de estados en Mermaid.
  - Código con `if/else`.
  - Tabla con los 6 problemas de esa solución.
- **State**:
  - Ficha del patrón.
  - Diagrama de clases.
  - Tabla de roles (Contexto, State, EstadoConcreto).
  - Código resuelto y lo que se gana con él.
- **Catálogo GoF** en tabla, por propósito y alcance.
- **Singleton**:
  - Las 3 piezas clave.
  - Código y las consideraciones (no clonable, `final`, `synchronized`).
  - Ejemplos típicos y críticas.
- **7 preguntas tipo parcial** en callouts plegables, para practicar sin ver la respuesta.

Para que te sirva más, agregué un ejemplo de State con el **Cuestionario de tu TP**: los estados Activo, En Proceso, Completo e Incompleto salen del enunciado. También conecté State con los diagramas de estado del Parcial 1.

## Cosas para revisar

- **Errores en el código de las diapositivas**: dice `syncronized` en vez de `synchronized`, falta `()` en `CloneNotSupportedException`, y `getInstance()` usa atributos de instancia dentro de un método estático, así que no compila. En el resumen los corregí y lo aclaré en una nota.
- **Flyweight**: el catálogo del apunte lo pone en *comportamiento*, pero en el catálogo original de GoF es *estructural*. Lo marqué como advertencia. Conviene confirmar con la cátedra cuál esperan.
- **No hay PDF de la Unidad 5.3** en la carpeta. Lo dejé anotado en [[U5 - Índice]].

Cuando termines de leer la 5.1, cambiá `estado: en-progreso` a `listo` en sus propiedades. Si te sirve este formato, seguimos con la **5.2**. Si querés más o menos detalle, más ejemplos o menos código, decime y ajusto antes de seguir.
[Timestamp: 2026/11/02 18:56:41]

**user**: Me gusta , digamos que sacaste info de otras unidades tambien y de los parciales? Me sirve eso
[Timestamp: 2026/11/02 19:02:32]

**ai**: No del todo, y te lo aclaro para que sepas qué parte del resumen viene del apunte y cuál no:

**Lo que sí usé además del PDF de la 5.1**

- **Enunciado del TP**: de ahí saqué los estados del Cuestionario (Activo, En Proceso, Completo, Incompleto) para el ejemplo de State.
- **Preguntas del Parcial 1** (los PDF de `Ejemplo de Parcial/`): tienen preguntas sobre acoplamiento, diagramas de estado y los estereotipos del modelo de diseño (interfaz, control, entidad). Las usé para la sección "Conexiones con el Parcial 1" del índice y para relacionar State con los diagramas de estado.
- **Resumen P1 - Tade**: solo miré los títulos de las unidades para entender cómo está organizada la materia. No usé su contenido.

**Lo que NO hice**

- **No leí los otros PDF de la Unidad 5 ni los de la 6** (5.2, 5.4, 5.5, DAO/DTO, 6.x). Solo vi los nombres de los archivos. Los links como [[U5.4 - SOLID]] apuntan a notas que todavía no existen. Que State se relacione con Open/Closed sí aparece en la diapositiva, pero lo de SOLID todavía no lo resumí.
- **Las "preguntas tipo parcial" las escribí yo**, imitando el formato de las preguntas del Parcial 1. No hay preguntas reales del Parcial 2 en tu bóveda.

**Lo que agregué de conocimiento general (no está en el apunte)**

- Que Flyweight es estructural según el catálogo original de GoF.
- La explicación de alcance de clase (herencia) contra alcance de objeto (composición).
- Las críticas a Singleton (estado global, dificulta el testing).
- Ejemplos como MVC o `try-with-resources`, las analogías y los ejemplos típicos de Singleton (logger, pool de conexiones).

## Propuesta para las próximas notas

Para que en el parcial sepas qué es "palabra de la cátedra" y qué es un agregado, puedo marcar el origen de cada cosa:

- `> [!quote] Apunte`: contenido de las diapositivas.
- `> [!tip] Extra`: explicaciones o ejemplos que no están en el apunte.
- `> [!question] Pregunta de práctica`: preguntas armadas por mí, separadas de las de parciales reales.

También puedo **leer primero todos los PDF de la Unidad 5** antes de seguir con la 5.2. Así las conexiones entre temas (State y Open/Closed, Singleton y DAO, etc.) se basan en lo que realmente dice la cátedra y no en lo que yo supongo.

Si tenés **parciales anteriores del segundo parcial**, sumalos a la bóveda. Serían la mejor fuente para las preguntas de práctica.

¿Querés que aplique estas marcas a la nota de la 5.1 antes de pasar a la 5.2?
[Timestamp: 2026/11/02 19:02:32]

**user**: Aca recopile material para que tengas en cuenta quizas sirve aunque algunos son de años posteriores y quizas en diseño las cosas cambian rapido pero es lo que pude conseguir fijate si podes aprender de eso Parcial 2 - Contenido/Exámenes
[Timestamp: 2026/11/02 19:09:51]

**ai**: Ya leí los textos (Word, txt y el PDF de 2016). Ahora reviso las fotos de exámenes, sobre todo la del Parcial 2 de 2017.Ya revisé todo, también las fotos. Armo una nota que organiza las preguntas por unidad.Ahora enlazo el banco desde los índices y la nota 5.1.Revisé todo el material de `Exámenes/`: los Word, los txt, el PDF de 2016 y las 6 fotos. Lo organicé en una nota nueva, [[Banco de preguntas - Exámenes anteriores]], con las preguntas por unidad, cuántas veces aparecen y una prioridad para cada tema.

## Lo que encontré

**1. Pruebas es lo que más preguntan.** Aparece en todos los parciales 2 y en los finales: plan de pruebas, cuándo dar una prueba por terminada, tipos de prueba con y sin usuarios, particiones de equivalencia y el lote de pruebas de los triángulos. El parcial 2 de 2017 dedicó 40 de los 100 puntos a esto.

**2. Patrones, SOLID y DAO/DTO no aparecen en ningún examen viejo.** Es contenido nuevo del programa. Para esos temas las preguntas de práctica las tengo que armar yo; ya lo aclaré en la nota de la 5.1.

**3. Arquitectura sí aparece.** Preguntan por capas o tiers, subsistemas, identificación de mecanismos y clases significativas para la arquitectura. También relaciones entre clases y modelo de diseño, que vienen de la U4 y pueden volver como repaso.

**4. El archivo `Parcial 2 - 2016.pdf` no es un examen.** Es un resumen de teoría de **Pruebas y Debugging**: principios, caja blanca y negra, valores límite, integración, pruebas alfa y beta, criterios de terminación, métodos de debugging. Lo vamos a usar como fuente extra para la Unidad 6. Lo anoté en [[U6 - Índice]].

**5. Hay una respuesta mal en "Preguntas varias".** Para el módulo que lee de 1 a 10.000 registros, el documento propone probar con 0, 1, 500, 1000 y 1001, que son los límites de un rango de 1 a 1000. Lo correcto es **0, 1, 2, 9.999, 10.000 y 10.001**. Lo marqué en el banco para que no lo estudies así.

**6. Hay temas de exámenes viejos que no veo en tus PDFs actuales:** gestión de riesgos, propuesta de sistemas, backup y seguridad informática. Los dejé en una sección "a verificar". Conviene preguntar a la cátedra si siguen en el programa antes de estudiarlos.

**7. El formato cambió.** Los exámenes viejos eran solo de desarrollo. Los ejemplos de parcial 1 de 2026 que tenés mezclan múltiple opción, verdadero/falso y desarrollo. Las preguntas de práctica las sigo armando con el formato actual.

## Cambios hechos
- Nueva nota [[Banco de preguntas - Exámenes anteriores]], enlazada desde [[00 - Índice Parcial 2]].
- En [[U5.1 - Patrones de Diseño]] agregué un aviso: las preguntas de práctica las armé yo, no salen de exámenes.
- En [[U6 - Índice]] agregué el PDF de 2016 como fuente extra y marqué la unidad como la más preguntada.

¿Seguimos con la **5.2**?
[Timestamp: 2026/11/02 19:09:51]

**user**: Si segui hasta terminar toda la unidad 5
[Timestamp: 2026/11/02 19:14:35]

**ai**: Sigo con la 5.2, 5.4, 5.5 y la práctica de DAO/DTO. Primero extraigo el texto de los cuatro PDF.Muchas diapositivas son imágenes (código y diagramas). Las junto de a cuatro para revisarlas más rápido.La 5.2 ya está (Facade, Bridge, Mediator). Ahora la 5.4, SOLID.SOLID listo. Ahora la 5.5, Arquitectura.Arquitectura lista. Casi todas sus diapositivas son diagramas sin texto, así que la explicación de cada estilo la voy a tener que completar y marcar como agregado. Ahora la práctica de DAO y DTO.Ya leí los cuatro PDF, incluidas las diapositivas con imágenes. Empiezo a escribir las notas, primero la 5.2.Ahora la 5.4, SOLID.Ahora la 5.5, Arquitectura.Ahora la última nota de la unidad: la práctica de DAO y DTO, con el ejercicio del TP.Reviso en el enunciado del TP si el CU025 muestra las claves al consultor, para que la propuesta del ejercicio sea correcta.Por último actualizo el índice de la Unidad 5, con un repaso rápido de todos los patrones, y el banco de preguntas.Compruebo que todos los wikilinks (notas y encabezados) apunten a algo que existe.La Unidad 5 está terminada: hay 4 notas nuevas en `Resumenes/Unidad 5/`, el índice de la unidad está actualizado y conecté todo con el banco de preguntas. Revisé todos los wikilinks y funcionan. Los únicos que quedan sin destino son los de la Unidad 6, que todavía no creamos.

## Notas nuevas

| Nota | Contenido |
| --- | --- |
| [[U5.2 - Patrones de Diseño II]] | **Facade**, **Bridge** y **Mediator**: ficha, diagrama, código, ejercicios y las preguntas de las diapositivas respondidas. Agregué una tabla comparativa, Facade contra Mediator y un resumen del mapa de relaciones entre patrones. |
| [[U5.4 - SOLID]] | Los 5 principios con su ejemplo de "antes y después", más IoC y DI. Una tabla muestra qué principio aplica cada patrón que vimos. |
| [[U5.5 - Arquitectura]] | Las 4 dimensiones, partición técnica o por dominio, monolítico o distribuido, las 8 falacias, 9 estilos, escalabilidad y arquitectura en UP. Respondí los 6 ejercicios del apunte y las 5 preguntas de exámenes viejos. |
| [[U5 - Práctica DAO y DTO]] | DTO y DAO, cómo se combinan, el error típico y el **ejercicio del TP de Candidato** con una propuesta de resolución. |
| [[U5 - Índice]] | Agregué **tres tablas de repaso rápido**: patrones, SOLID y estilos de arquitectura. Sirven para la última leída antes del parcial. |

En todas las notas, lo que agregué yo y no está en el apunte va en callouts marcados como **Extra**.

## Cosas para revisar

- **Arquitectura es la nota con más contenido mío.** De los 41 slides, unos 20 son solo diagramas sin texto, entre ellos los de casi todos los estilos. Las descripciones, ventajas y desventajas de cada estilo las armé con el libro del que salen los diagramas (Richards y Ford). Si el profe los explicó distinto en clase, quedate con lo de clase.
- **El ejercicio de Candidato está corregido según el enunciado del TP.** Al principio propuse no mostrar la clave en ningún DTO. Después vi en el enunciado que en el CU025 (paso 11) **el consultor sí ve la clave** y la puede exportar a Excel, y que en el CU026 la clave **se valida contra el cuestionario**. Ajusté la resolución a eso.
- **Hay una contradicción en la práctica de DAO/DTO.** Un slide dice "un DTO por cada clase de dominio con los atributos que quiero guardar en la BD". Los ejemplos de la misma clase usan varios DTO por entidad y un DAO que trabaja con entidades. Lo marqué en la nota y recomiendo seguir el criterio de los ejemplos.
- **Algunos ejemplos están en C#, no en Java:** la sala de chat del Mediator y casi todos los de SOLID. Lo aclaré en cada nota para que no te confunda la sintaxis.
- **Sigue faltando el PDF de la 5.3.**

Cuando quieras arrancamos con la **Unidad 6**. Según el banco de preguntas es el tema que más se tomó en parciales y finales, y además tenés el resumen de Pruebas de 2016 como fuente extra.
[Timestamp: 2026/11/02 19:14:35]

**user**: Aca estan los contenidos del Parcial 2 obsidian://open?vault=Dise%C3%B1o%20de%20Sistemas&file=Parcial%202%20-%20Contenido%2FContenido%20Parcial%202.png , por si sirve . Y Quiero que crees la carpeta y el contenido de la unidad 4 completa
[Timestamp: 2026/11/02 19:32:26]

**ai**: La imagen sirve mucho: confirma que la Unidad 4 entra en el Parcial 2 y aclara lo de la 5.3. Ahora leo los tres PDF de la Unidad 4.La 4.1 está lista. Ahora la 4.2, Componentes y Despliegue.Ahora la 4.3, Máquinas de estado.Ahora las clases prácticas de secuencia y despliegue.Ya leí todo el material de la Unidad 4: los 3 PDF de teoría y las 2 clases prácticas. Empiezo a escribir las notas, primero la 4.1.Ahora la 4.2, Componentes y Despliegue, junto con la práctica del 16/10.Ahora la 4.3, Máquinas de Estado.El enunciado del TP tiene un quinto estado, **"Sin Contestar"**, y reglas exactas para cada transición. Corrijo el ejemplo integrador.Ahora la nota del Diagrama de Secuencia, que sale de la práctica del 11/09.
[Timestamp: 2026/11/02 19:32:26]

**user**: Continua en donde lo dejaste ahora te di permiso asi no me pedis nada
[Timestamp: 2026/11/02 19:42:29]

**ai**: Sigo con la nota del Diagrama de Secuencia.Normalizo todos los encabezados con ":" en todas las notas, porque rompen los links de Obsidian, y valido los links.Todos los links resuelven, salvo el índice de la Unidad 4 (que creo ahora) y las notas de la Unidad 6. Creo el índice de la Unidad 4.Ahora actualizo el índice general, el índice de la Unidad 5 (el programa aclara lo de la 5.3) y el banco de preguntas.La Unidad 4 está completa: hay 5 notas nuevas en `Resumenes/Unidad 4/`. Ya enlacé todo con el índice general, el banco de preguntas y las notas de la Unidad 5. Revisé todos los wikilinks y funcionan; los únicos sin destino son los de la Unidad 6, que todavía no está hecha.

## Lo que aportó la imagen del programa

- **El Parcial 2 incluye las Unidades 4, 5 y 6.** La agregué al índice general.
- **La 5.3 no existe.** La Unidad 5 tiene 5 presentaciones, y una es la práctica de DAO/DTO. Saqué el aviso de "falta la 5.3".
- **El diagrama de secuencia entra en el parcial**, pero no tiene presentación teórica: sale de la clase práctica del 11/09. La encontré en `Diagrama de Secuencia y GIT/` y la usé como fuente. Lo mismo hice con la práctica de despliegue del 16/10, que está en `Diagrama de Despliegue/`.
- Anoté la bibliografía de cada unidad en su índice.

## Notas de la Unidad 4

| Nota | Contenido |
| --- | --- |
| [[U4 - Índice]] | Programa oficial, mapa de cómo se conectan los diagramas, tabla "qué responde cada uno" y repaso rápido |
| [[U4.1 - Modelos de UP y Diagrama de Clases]] | Casos de uso → análisis → diseño, las tablas comparativas, relaciones, clase de asociación, abstractas, interfaces y `<<traza>>` |
| [[U4.2 - Componentes y Despliegue]] | Componentes, paquetes, subsistema, cohesión y acoplamiento, PER/PCC/PRC, notación de despliegue, 2 capas contra 3 capas, el TP y el ejercicio CampusCoffee resuelto |
| [[U4.3 - Máquinas de Estado]] | Transiciones, orden exit → acción → entry, eventos diferidos, super-estados, historia (H), regiones concurrentes y la máquina del cuestionario del TP |
| [[U4 - Diagrama de Secuencia]] | Componentes, mensajes, fragmentos `alt`/`opt`/`loop`/`par`, el ejemplo CU-19 en Mermaid, secuencia contra colaboración y una receta paso a paso |

La Unidad 4 tiene muchas preguntas de exámenes viejos (estereotipos, relaciones, análisis contra diseño, subsistemas, secuencia contra colaboración). Están respondidas en cada nota y marcadas con 📝.

## Cosas para revisar

- **El cuestionario del TP tiene 5 estados, no 4.** Leyendo el enunciado encontré **"Sin Contestar"**: pasa a ese estado cuando se supera el tiempo máximo en estado activo. También vi que a **"Incompleto"** se llega por exceso de accesos o por tiempo vencido. Lo corregí en la 4.3 y en el ejemplo de State de la 5.1.
- **Uno de los ejemplos de la cátedra contradice la práctica de DAO/DTO.** En el ejemplo del TP 2025 que mostraron en la práctica de secuencia, `FacturaDAO` devuelve un `FacturaDTO`, que es justo lo que la práctica de DAO/DTO de 2026 marca como error. Lo aclaré en la nota de secuencia: para el parcial, seguí el criterio de 2026.
- **Parte del contenido de la Unidad 4 es agregado mío:**
  - El apunte solo **nombra** los tipos de cohesión y acoplamiento de componentes y los principios PER/PCC/PRC. Las explicaciones salen de Pressman, que está en la bibliografía del parcial.
  - La composición y las actividades del modelo de diseño salen de UP. No están en las diapositivas, pero se preguntaron varias veces en exámenes viejos.
  - La comparación entre secuencia y colaboración también es agregado mío.

  Todo eso está marcado como **Extra** en las notas.
- **Cambié los títulos de sección con ":" en todas las notas** (por ejemplo, "Ejemplo integrador: …" pasó a "Ejemplo integrador - …"). Los ":" rompen los links a encabezados en Obsidian.

Si querés, sigo con la **Unidad 6** con el mismo formato.
[Timestamp: 2026/11/02 19:42:29]

**user**: Veo que tienen bastante informacion , lo que esta en gris o las definiciones es lo que priorizaste ? Por que me gusta el nivel de detalle pero tambien distinguir que cosas si estudiarme y que cosas entenderlas unicamente . No modifiques nada solo explicame
[Timestamp: 2026/11/03 23:54:19]

**ai**: No, el gris no es una marca de prioridad que haya puesto a propósito. Te explico qué significa cada recuadro y cómo usarlos para separar lo que conviene memorizar de lo que alcanza con entender.

## Lo gris

En el tema de Obsidian por defecto, los recuadros `[!quote]` se ven grises. En esos puse **las definiciones textuales del apunte**: componente, subsistema, diagrama de despliegue, DAO, DTO, los principios SOLID, etc.

Así que, sin querer, lo gris coincide bastante con lo que hay que memorizar, porque son las definiciones como las da la cátedra. Pero no fue un sistema pensado. Y lo importante no está solo ahí: muchas tablas fuera de los recuadros también son contenido clave.

## Qué significa cada tipo de recuadro

| Recuadro (título que ves) | Qué puse ahí | ¿Estudiar o entender? |
| --- | --- | --- |
| **abstract** (TL;DR, arriba de cada nota) | Resumen de lo esencial de la nota | 🔴 **Memorizar.** Es lo mínimo que tenés que saber. |
| **quote** (gris, definiciones) | Definiciones textuales del apunte | 🔴 **Memorizar**, idealmente con palabras parecidas. |
| **summary** ("Ficha del patrón") | Intención, clasificación, aplicabilidad | 🔴 **Memorizar.** En particular la intención y la clasificación. |
| **important** | Reglas clave o algo que se preguntó en exámenes | 🔴 **Memorizar.** |
| **warning** | Trampas, confusiones típicas, errores del apunte | 🟠 **Leer con atención.** Suelen salir como V/F o múltiple opción. |
| **danger** / **bug** | Errores comunes ("lo que NO hay que hacer") | 🟠 **Entender y recordar.** |
| **tip** marcado **Extra** | Cosas que agregué yo: analogías, explicaciones de bibliografía, comparaciones | 🟢 **Entender.** Te ayudan a razonar, pero no son palabra de la cátedra. Excepción: los Extra con 📝, porque salieron en exámenes. |
| **example** | Ejemplos del apunte, del TP o propios | 🟢 **Entender.** Útiles para "ejemplifique" en preguntas de desarrollo. |
| **info** / **note** | Fuentes, aclaraciones de dónde sale algo | ⚪ Contexto, no se estudia. |
| **question** (plegables al final) | Preguntas de práctica | ✍️ **Practicar.** Respondé sin abrirlas. |

**Fuera de los recuadros**, las tablas comparativas (análisis contra diseño, 2 capas contra 3 capas, agregación contra composición, Facade contra Mediator, etc.) son de lo más importante: los exámenes piden mucho "compare" y "diferencie". Los bloques de código solo hace falta entenderlos, no memorizarlos.

## Ejemplo con [[U4.2 - Componentes y Despliegue]]

- 🔴 **Memorizar:**
  - La definición de componente y la de subsistema.
  - Interfaz provista contra requerida.
  - La tabla de elementos del diagrama de despliegue (`«device»`, `«executionEnvironment»`, `«artifact»`, `«manifest»`, protocolos).
  - Los errores comunes.
  - La tabla de 2 capas contra 3 capas.
- 🟠 **Saber nombrar y explicar en una línea:** tipos de cohesión y acoplamiento, y PER/PCC/PRC. El apunte solo los nombra, así que con eso alcanza.
- 🟢 **Solo entender:**
  - Los ejemplos de Tomcat y Docker.
  - La explicación de "puerto".
  - La resolución de CampusCoffee (sirve para practicar).

## Regla rápida para estudiar

1. Leé el **TL;DR** y la sección de **repaso rápido** del índice de la unidad. Eso es lo que no puede faltar.
2. Estudiá los recuadros **quote, summary e important** y las **tablas comparativas**.
3. Leé una vez los **warning** y los **danger**.
4. Usá los **Extra** y los **example** solo para entender. No los memorices, salvo los marcados con 📝.
5. Al final, hacé las **preguntas plegables** sin abrirlas.

Si querés que la prioridad quede marcada de forma explícita en cada nota (por ejemplo, 🔴 memorizar, 🟠 saber explicar, 🟢 solo entender en cada sección), decime y lo agrego. Así no depende del color del tema.
[Timestamp: 2026/11/03 23:54:19]

**user**: Me gustaria que guardes como skills 'armado-resumenes' para proximos resuumenes
[Timestamp: 2026/11/03 23:58:29]

**ai**: Guardé el método como la skill **`armado-resumenes`** en `.claude/skills/armado-resumenes/` dentro de tu bóveda. Ya aparece entre las skills disponibles, así que la próxima vez que me pidas un resumen la uso directamente, o podés pedirla con `/armado-resumenes`.

## Qué quedó guardado

**`SKILL.md`**, con el método completo:
1. **Antes de escribir:** buscar primero el programa oficial y leer todo el material de la unidad, incluidas las diapositivas que son solo imagen. También buscar las clases prácticas y los exámenes, y comprobar contra el enunciado del TP todo ejemplo que lo use.
2. **Carpetas:** `00 - Índice`, banco de preguntas y una carpeta por unidad con su índice. Las notas se llaman `UN.M - Tema`.
3. **Estructura fija de cada nota:** propiedades, navegación, TL;DR, índice, secciones numeradas, preguntas plegables y conceptos relacionados.
4. **Tipo de recuadro según prioridad:** la tabla que te expliqué (🔴 memorizar / 🟠 atención / 🟢 entender), para que todas las notas futuras la respeten.
5. **Exámenes anteriores:** banco por unidad, marca 📝, separar las preguntas reales de las que armo yo y señalar las respuestas incorrectas del material.
6. **Diagramas:** Mermaid con sus precauciones. Lo que Mermaid no puede dibujar va como PNG de Excalidraw en `Assets/`.
7. **Reglas aprendidas:** títulos de sección sin ":", revisar tus cambios antes de editar y corregir el código del apunte.
8. **Cierre de unidad:** actualizar los índices, revisar los links con un script y terminar con un resumen de "cosas para revisar".
9. **Forma de trabajo:** avanzar sin pedir confirmación y ser claro sobre de dónde sale cada cosa.

**`plantilla-nota.md`**: el esqueleto de una nota de tema, para copiar.

Las marcas explícitas 🔴/🟠/🟢 en cada título de sección quedaron como **opcionales**: solo las agrego si me las pedís.

¿Seguimos con la **Unidad 6** usando la skill?
[Timestamp: 2026/11/03 23:58:29]