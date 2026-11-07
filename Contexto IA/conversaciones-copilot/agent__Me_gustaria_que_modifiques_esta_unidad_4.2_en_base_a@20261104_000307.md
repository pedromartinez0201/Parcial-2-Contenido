---
epoch: 1793761387264
mode: agent
backendId: claude
sessionId: "b75a0356-76da-4adc-b7b3-3f5f86b78916"
agentLabel: "Me gustaria que modifiques esta unidad 4.2 en base a lo que…"
usage: '{"usedTokens":90332,"contextWindow":1000000,"inputTokens":4,"outputTokens":5,"cacheReadTokens":89152,"cacheWriteTokens":1171,"updatedAt":1793762314843}'
tags:
  - copilot-conversation
---

**user**: Me gustaria que modifiques esta unidad 4.2 en base a lo que hablamos lo que aprendi que te comente asi cuando vuelva a estudiar ya comprenda . Tambien me gustaria compactar mas la unidad. La idea es que crees una carpeta "Unidad 4 compactada" donde vas a agregar cada compactacion ahi dentro . Por el momento solo la 4.2
[Timestamp: 2026/11/04 00:03:07]

**ai**: Estoy recuperando lo que hablamos en la sesión anterior sobre la 4.2 para incorporarlo a la nota. Sigo leyendo el resto de esa conversación.Agrego un enlace desde la nota original a la compactada y guardo en memoria la nueva carpeta.Creé la carpeta **Unidad 4 compactada** con la nota [[U4.2 - Componentes y Despliegue (compactado)]]. Le agregué todo lo que aprendiste en la charla anterior sobre la 4.2. No la abrí en Obsidian, así que conviene que revises que los dos diagramas Mermaid se vean bien.

**Qué tiene la versión compactada**
1. **La 4.2 en 5 frases:** paquete, subsistema, componente, artefacto y nodo.
2. **El mapa completo:** un diagrama corto de cómo se pasa del paquete al nodo (`«manifest»` y `«deploy»`). Abajo hay una tabla que compara los 5 conceptos: qué es cada uno, si existe al ejecutar, si tiene interfaces y en qué diagrama se dibuja.
3. **Lo que me confundió (y la respuesta):** una tabla "Yo pensaba… / En realidad…" con tus dudas ya resueltas:
   - interfaz = contrato, no pantalla;
   - un paquete no es una carpeta de Windows;
   - un paquete puede tener interfaces adentro;
   - qué es un "elemento";
   - un componente no es un `.jar`;
   - layer contra tier y "3 layers en 1 tier";
   - las reglas de negocio no van en Presentación;
   - el código no forma parte del modelo de diseño.
4. **Componente:** una tabla de características explicadas en simple (cohesivo con el ejemplo ✅ `Pagos` / ❌ `Utilidades`, desplegable porque se materializa en un artefacto, etc.). Incluye la idea de "caja negra" y la imagen de la notación.
5. **Paquetes, layers y tiers:** el subsistema explicado como "paquete con ventanilla", con la tabla de qué ves y qué no ves desde afuera. Incluye que los DAO corren en el servidor de aplicación y qué entra y qué no en el modelo de diseño.
6. **Cohesión, acoplamiento y PER/PCC/PRC:** quedaron en dos tablas.
7. **Despliegue:** una tabla de notación, los errores comunes, el diagrama web de 3 capas, la comparación 2 contra 3 capas, los nodos del TP y CampusCoffee resumido en un bloque que se despliega.
8. **Preguntas tipo parcial:** sumé las del cuestionario que hicimos, incluidas las dos que te costaron (la del `AdaptadorMercadoPago` y la de las 3 layers en una sola PC).

**Qué saqué para compactar:** el ejemplo del email con puertos, la imagen de dependencias de paquetes, la tabla larga de notación de paquetes, los ejemplos de Tomcat y Docker y el ejemplo de escritorio en 2 capas. Siguen en la versión completa.

**Otros cambios**
- La nota original [[U4.2 - Componentes y Despliegue]] quedó igual. Solo le agregué, en la línea de navegación, un enlace a la versión compactada.
- Guardé en memoria que las compactaciones van en esa carpeta, así las próximas (4.1, 4.3…) siguen el mismo formato.
[Timestamp: 2026/11/04 00:03:07]

**user**: La diferencia de la interfaz provista con la requerida es la simbologia y que una el componente la ofrece y la otra el componente la requiere?
[Timestamp: 2026/11/04 00:16:41]

**ai**: Sí, la idea está bien. Hay un matiz importante: **no son dos tipos distintos de interfaz.** Es **la misma interfaz (el mismo contrato) vista desde dos lados**. Lo que cambia es la **relación** que cada componente tiene con ella.

| | Interfaz provista | Interfaz requerida |
| --- | --- | --- |
| **Símbolo** | Lollipop (círculo) ○— | Socket (semicírculo) —( |
| **Qué significa** | El componente **ofrece** esas operaciones | El componente **necesita** esas operaciones para funcionar |
| **Qué hace el componente con ella** | La **implementa**: tiene el código de esas operaciones | **Depende** de ella: la usa, pero no sabe quién la implementa |
| **Relación UML** | Realización (implementa) | Dependencia («use») |

**Ejemplo con la misma interfaz `IPago`:**
- `Pagos` **provee** `IPago` (○), porque implementa `procesarPago(monto, medio)`.
- `Pedidos` **requiere** `IPago` (◡), porque para confirmar un pedido necesita cobrar, pero no sabe cómo se cobra.
- En el diagrama, el socket de `Pedidos` **encaja** en el lollipop de `Pagos`. Así se ve que las dos piezas están conectadas.

**Por qué importa la diferencia:** como `Pedidos` solo depende del contrato, cualquier componente que **provea** `IPago` puede reemplazar a `Pagos` sin que `Pedidos` se entere. De ahí sale que los componentes sean **reemplazables**.

> [!tip] Notación alternativa
> En vez del lollipop y el socket, la interfaz también se puede dibujar como un rectángulo con `«interface»`. En ese caso:
> - la **provista** se une al componente con una flecha punteada con punta de triángulo hueco (realización);
> - la **requerida** se une con una flecha punteada común con «use» (dependencia).

**Frase para el parcial:** *"Una interfaz provista es un contrato que el componente implementa y ofrece a otros (lollipop). Una interfaz requerida es un contrato del que el componente depende para funcionar (socket). La misma interfaz puede ser provista por un componente y requerida por otro, y así se conectan."*

¿Querés que agregue esto en la sección 3 de [[U4.2 - Componentes y Despliegue (compactado)]]? También podría sumar una fila en la tabla "Yo pensaba… / En realidad…" que diga que provista y requerida no son dos interfaces distintas, sino dos roles frente al mismo contrato.
[Timestamp: 2026/11/04 00:16:41]

**user**: V/F: "En el diagrama de despliegue se dibujan las clases dentro de cada nodo." esta es falsa dentro de cada nodo va un artifact o otro nodo
[Timestamp: 2026/11/04 00:18:26]

**ai**: Sí, es **falsa** y tu justificación está bien. Le agregaría dos detalles para que la respuesta quede completa.

**Qué puede ir dentro de un nodo**

| Qué va adentro | Ejemplo |
| --- | --- |
| **Artefactos** (`«artifact»`) | `capital-humano.war`, `esquema_capital.sql` |
| **Otros nodos**, normalmente entornos de ejecución (`«executionEnvironment»`) anidados en un `«device»` | `Tomcat 10` dentro de `Servidor de aplicaciones` |
| **Especificaciones de despliegue** (`«deployment spec»`) | `web.xml` |

El anidado puede tener varios niveles: `«device»` → `«executionEnvironment»` → `«artifact»`. Por ejemplo, Servidor → Tomcat → `.war`.

**Por qué no van clases**
- Una clase es un elemento **lógico** del modelo de diseño, no algo que se instala.
- Lo que se instala físicamente es el **archivo** que contiene esas clases ya compiladas, o sea el artefacto (`.jar`, `.war`).
- La relación con lo lógico se muestra con `«manifest»`: el artefacto **manifiesta** un **componente**, no una clase suelta.

> [!warning] Matiz
> En algunos libros o diagramas viejos (UML 1.x) vas a ver **componentes** dibujados dentro de los nodos. En UML 2, que es lo que usa la cátedra, lo correcto es poner el **artefacto** en el nodo y unirlo al componente con `«manifest»`.

**Respuesta para el parcial:** *"Falso. Dentro de los nodos se ubican artefactos (archivos como `.jar`, `.war` o `.sql`) y otros nodos anidados, como los entornos de ejecución. Las clases son elementos lógicos del diseño: llegan al nodo compiladas dentro de un artefacto, que manifiesta al componente correspondiente."*

¿Querés que actualice esta pregunta en [[U4.2 - Componentes y Despliegue (compactado)]] con esta respuesta más completa?
[Timestamp: 2026/11/04 00:18:26]