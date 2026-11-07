---
epoch: 1793918315746
mode: agent
backendId: claude
sessionId: "3bbbe329-21af-4ba0-8a8e-98088c9c776e"
agentLabel: "En la unidad 6 aparece algo sobre debugging?"
usage: '{"usedTokens":43549,"contextWindow":1000000,"inputTokens":2,"outputTokens":876,"cacheReadTokens":41601,"cacheWriteTokens":1070,"updatedAt":1793918360533}'
tags:
  - copilot-conversation
---

**user**: En la unidad 6 aparece algo sobre debugging?
[Timestamp: 2026/11/05 19:38:35]

**ai**: **Casi no.** En las presentaciones de la Unidad 6 el debugging aparece una sola vez y de pasada. El tema desarrollado está en otro PDF, `Exámenes/Parcial 2/Parcial 2 - 2016.pdf`, que en [[U6 - Índice]] ya figura como fuente extra de la unidad.

También busqué en las notas, pero las de la unidad (U6.1, U6.2 y U6.3) todavía están pendientes. La búsqueda fue por las palabras "debug" y "depura", así que no detectaría el tema si aparece con otros términos, como "corrección de errores".

## Dónde aparece

| Fuente | Qué dice |
| --- | --- |
| `Unidad 6.1 - Pruebas v2.pdf` | No lo menciona. |
| `Unidad 6.2 - Tipos de Pruebas.pdf`, diapositiva 5 | Solo dice que las pruebas de unidad facilitan el debugging: "si falla, el sospechoso está acotado". |
| `Unidad 6.3 - Implementación v2.pdf`, diapositiva 13 | "Limpiar y depurar" se refiere a limpiar datos en una migración, no a debugging. |
| `Parcial 2 - 2016.pdf`, págs. 11-13 | Desarrolla el tema completo (detalle abajo). |
| [[Banco de preguntas - Exámenes anteriores]] | Tiene 3 preguntas: métodos de debugging, inconvenientes del esparcimiento de sentencias y diferencia entre un caso de prueba para probar y uno para debugging. También lo marca como prioridad alta, junto con inspecciones. |

## Qué dice el PDF de 2016

El debugging se hace **después de un caso de prueba exitoso**, es decir, uno que encontró un error. Tiene dos partes: ubicar el error, que es el 95% del problema, y corregirlo.

**Métodos sistemáticos:**
- **Deducción:** parte de todas las causas posibles y las va eliminando hasta que queda una.
- **Inducción:** parte de los síntomas particulares y busca relaciones entre ellos para formular una hipótesis.
- **Rastreo hacia atrás:** recorre la lógica hacia atrás hasta el punto donde se desvía. Sirve para programas pequeños.
- **Por medio de pruebas:** escribe variantes del caso de prueba original para ubicar el error con exactitud.

**Métodos asistemáticos**, recomendados solo si fallan los otros o como complemento:
- **Vuelco de memoria:** probablemente el más ineficiente, porque da una imagen estática y con mucha información irrelevante.
- **Esparcimiento de sentencias:** agrega mensajes o muestra variables dentro del programa. Sus inconvenientes son:
  - Es prueba y error, sin pensar en el problema.
  - Puede generar muchísimos datos para analizar.
  - Modificar el programa puede enmascarar el error.
  - En programas extensos puede ser muy costoso, y en algunos, imposible.
- **Debuggers:** analizan la dinámica del programa sin modificarlo, usando puntos de detención.

**Caso de prueba para probar y para debugging:**

| | Para probar | Para debugging |
| --- | --- | --- |
| **Propósito** | Exponer errores no detectados | Obtener información para ubicar un error determinado |
| **Forma** | "Gordo": cubre muchas condiciones con pocos casos | "Delgado": cubre una o pocas condiciones por caso |

**Principios para buscar errores:**
- Pensar.
- Si te trabás, descansar o contarle el problema a otra persona.
- Usar las herramientas solo como segundo recurso.
- Dejar los experimentos como último recurso.

**Principios para reparar errores:**
- Donde hay una falla, probablemente haya otra.
- Arreglar el error, no solo un síntoma.
- Nunca asumir que la corrección está 100% bien; esa probabilidad baja a medida que el programa es más grande.
- Hacer una prueba de deterioro, porque corregir puede introducir errores nuevos.
- Volver temporariamente a la etapa de diseño.

## Para el parcial

Las presentaciones actuales casi no lo tratan y el material fuerte es de 2016. Por eso conviene estudiarlo, porque el banco lo pregunta, pero no puedo asegurar que siga vigente en el programa actual. Si podés, confirmalo con la cátedra.
[Timestamp: 2026/11/05 19:38:35]