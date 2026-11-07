---
epoch: 1790205766709
mode: agent
backendId: codex
sessionId: "01a0d089-56b2-77c0-abe0-e5168f04b2f2"
agentLabel: "me pierdo un poco con los nombres a los mensajes cuando uso…"
usage: '{"usedTokens":39496,"contextWindow":258400,"updatedAt":1790207391067}'
tags:
  - copilot-conversation
---

**user**: me pierdo un poco con los nombres a los mensajes cuando uso metodos y cuando un nombre normal
[Timestamp: 2026/09/23 20:22:46]

**ai**: Voy a revisar el PDF de la clase para explicártelo usando exactamente la notación y los ejemplos que están viendo ahí. Para eso usaré la habilidad de lectura de PDF del vault.La lectura integrada del PDF no está activa, así que sigo con el lector local de PDF para no frenarte. Voy a buscar los ejemplos de mensajes, métodos y nombres dentro del material.La regla práctica es: **el nombre del mensaje depende de quién envía y quién recibe la flecha**.

| Comunicación | Cómo nombrarla | Ejemplo |
| --- | --- | --- |
| Actor → Interfaz | Acción en lenguaje natural | `Ingresa filtros y presiona SIGUIENTE` |
| Interfaz → Gestor | Método del gestor | `buscarResponsablePago(filtros)` |
| Gestor → DAO | Método del DAO | `buscarResponsablePago(filtros)` |
| Gestor → Interfaz | Método que ejecuta la interfaz | `mostrarListaResponsables(listaResponsables)` |
| Sistema → Actor | Resultado visible, en lenguaje natural | `Mostrar pantalla para ingresar filtros` |
| Retorno punteado | Dato devuelto | `listaResponsables` |

La pregunta que te destraba es:

> **¿El receptor es un objeto del software al que le estoy pidiendo ejecutar una operación?**

- Si la respuesta es **sí**, escribís un método: `verboObjeto(parámetros)`.
- Si la respuesta es **no** —por ejemplo, el mensaje involucra al actor—, describís la acción normalmente.

En el ejemplo del PDF:

```text
Conserje → UI
Ingresa filtros y presiona "SIGUIENTE"
```

Es lenguaje normal porque el conserje no llama directamente a un método Java.

Después:

```text
UI → GestorResponsablePago
buscarResponsablePago(filtros)
```

Es un método porque la interfaz le pide al gestor que ejecute una operación.

Luego:

```text
GestorResponsablePago → ResponsablePagoDAO
buscarResponsablePago(filtros)
```

También es un método. Además, debería existir como operación en la clase receptora `ResponsablePagoDAO`.

Finalmente, la flecha punteada de regreso:

```text
ResponsablePagoDAO --> GestorResponsablePago
listaResponsables
```

No es otro método: es **el resultado devuelto** por `buscarResponsablePago(...)`.

Una forma rápida de recordarlo:

```text
Actor → Sistema       = qué hace el usuario
Objeto → Objeto       = método(...)
Objeto --> Objeto     = dato retornado
Sistema → Actor       = qué ve el usuario
```

Para los métodos conviene usar:

- Un verbo: `buscar`, `mostrar`, `confirmar`, `calcular`.
- Camel case: `buscarResponsablePago`.
- Paréntesis, aunque no haya parámetros: `mostrarAltaResponsablePago()`.
- Parámetros únicamente cuando ayudan a entender el intercambio: `buscarResponsablePago(filtros)`.
- El mismo nombre que aparece en el diagrama de clases del objeto receptor.

Esta distinción se ve en los casos CU-03 y CU-19 del material. :codex-file-citation{path="/home/pedromartinez/Documentos/Diseño de Sistemas/Diagrama de Secuencia y GIT/Clase de práctica 11_09_26 - Diagrama de secuencia.pdf" purpose="source"}

- :codex-followup[Revisar mi diagrama]{prompt="Revisa los nombres de los mensajes de mi diagrama de secuencia y dime cuáles deberían ser métodos y cuáles texto normal."}
- :codex-followup[Crear una guía breve]{prompt="Crea una nota de estudio breve con las reglas para nombrar mensajes en diagramas de secuencia."}
- :codex-followup[Practicar con ejemplos]{prompt="Dame un ejercicio corto para practicar cómo nombrar mensajes en un diagrama de secuencia y luego corrige mi respuesta."}
[Timestamp: 2026/09/23 20:22:46]

**user**: este caso de uso donde se modela el 2.A
[Timestamp: 2026/09/23 20:35:30]

**ai**: En el diagrama mostrado, el flujo **2.A no está modelado explícitamente**.

El fragmento:

```text
alt [f == NULL]
    mostrar mensaje “No existen facturas pendientes de pago”
```

representa el **4.A**, porque ocurre después de llamar a `buscarFacturas(...)`: la búsqueda se realizó, pero no encontró facturas.

El **2.A** debería aparecer antes de llamar a `buscarFacturas(...)`, validando que el actor haya ingresado al menos un filtro:

```text
Conserje → UI: Ingresa filtros y presiona “BUSCAR”

alt [todos los filtros están vacíos]
    UI → Conserje: Mostrar mensaje “Debe completar CUIT, Tipo o Nro. de documento”
    UI → Conserje: Solicitar reingreso de datos
else [hay al menos un filtro]
    UI → GestorFactura: buscarFacturas(filtros)
    GestorFactura → FacturaDAO: buscarFacturas(filtros)
end
```

Como el punto **2.A.2 dice que se vuelve al paso 2**, incluso quedaría mejor con un `loop`:

```text
loop [mientras no se ingrese ningún filtro]
    Conserje → UI: Ingresa filtros y presiona “BUSCAR”
    UI → Conserje: Mostrar mensaje “Debe completar al menos un filtro”
end

UI → GestorFactura: buscarFacturas(filtros)
```

Después de eso iría otro `alt`, separado, para el 4.A:

```text
alt [facturas encontradas]
    GestorFactura → UI: mostrarGrillaFacturas(facturas)
else [no hay facturas]
    GestorFactura → UI: mostrarMensajeSinFacturas()
end
```

La diferencia clave es:

- **2.A:** no se ingresaron criterios; la búsqueda no debería ejecutarse.
- **4.A:** sí se ingresaron criterios y se buscó, pero no hubo resultados.

Por eso `[f == NULL]`, colocado después del DAO, no alcanza para representar ambos casos. Son validaciones distintas y conviene usar dos fragmentos separados.
[Timestamp: 2026/09/23 20:35:31]

**user**: el DTO no se modela como tal ?
[Timestamp: 2026/09/23 20:41:30]

**ai**: Sí, el DTO **puede modelarse**, pero normalmente se representa como **información transportada**, no como un participante con comportamiento propio.

En este caso:

- `FacturaDTO[]` debería aparecer como retorno de `buscarFacturas(...)`.
- `NotaDeCreditoDTO` puede aparecer como objeto creado y luego enviado al DAO.
- No hace falta dibujar cada DTO como una línea de vida si solamente transporta datos.

Por ejemplo:

```text
FacturaDAO --> GestorFactura:
facturas: FacturaDTO[]
```

Y para la nota de crédito:

```text
GestorFactura → nc:NotaDeCreditoDTO: <<create>>
GestorFactura → NotaDeCreditoDAO: crearNotaCredito(nc)
```

En el diagrama de la clase se muestra `NotaDeCreditoDTO`, pero en la secuencia la línea de vida figura como:

```text
nc:Nota de Crédito
```

Eso es inconsistente. Si realmente están utilizando el DTO definido en el diagrama de clases, debería decir:

```text
nc:NotaDeCreditoDTO
```

Una versión más clara sería:

```text
UI → GestorFactura:
confirmarNotaCredito(facturasSeleccionadas)

GestorFactura → nc:NotaDeCreditoDTO:
<<create>>

GestorFactura → NotaDeCreditoDAO:
crearNotaCredito(nc)

NotaDeCreditoDAO --> GestorFactura:
resultado
```

También se podría omitir la línea de vida del DTO y mostrarlo solamente como parámetro:

```text
GestorFactura → NotaDeCreditoDAO:
crearNotaCredito(notaCreditoDTO)
```

Las dos opciones son válidas. Para un diagrama de secuencia de análisis, suele bastar con poner el DTO como parámetro o retorno. Conviene dibujarlo con línea de vida solamente cuando su creación sea una parte importante de lo que se quiere explicar.

La regla rápida sería:

- Gestor, UI y DAO: normalmente tienen línea de vida porque ejecutan operaciones.
- DTO: normalmente aparece como parámetro o retorno.
- DTO con línea de vida: únicamente si interesa mostrar explícitamente cuándo se crea o cómo se completa.
[Timestamp: 2026/09/23 20:41:30]

**user**: por que se escribe f := buscarFacturas , ese metodo no existe en el diagrama de clases
[Timestamp: 2026/09/23 20:44:54]

**ai**: Exacto: ahí hay una **inconsistencia entre el diagrama de secuencia y el diagrama de clases**.

La expresión:

```text
f := buscarFacturas(...)
```

tiene dos partes:

- `buscarFacturas(...)`: es el método que se invoca.
- `f :=`: significa “guardar el resultado devuelto por el método en la variable `f`”.

Es equivalente a escribir en código:

```java
List<FacturaDTO> f = gestorFactura.buscarFacturas(filtros);
```

El problema no es `f :=`. El problema es que **`buscarFacturas(...)` no aparece como operación en las clases receptoras**.

En el diagrama se hacen dos llamadas:

```text
UI → GestorFactura:
f := buscarFacturas(filtros)

GestorFactura → FacturaDAO:
f := buscarFacturas(filtros)
```

Por lo tanto, deberían existir operaciones compatibles en ambas clases, por ejemplo:

```text
GestorFactura
+ buscarFacturas(filtros: FiltrosFactura): FacturaDTO[]
```

```text
FacturaDAO
+ buscarFacturas(filtros: FiltrosFactura): FacturaDTO[]
```

O, más específico para este caso de uso:

```text
+ buscarFacturasPendientes(
    cuit: String,
    tipoDocumento: TipoDocumento,
    nroDocumento: String
): FacturaDTO[]
```

Que el gestor y el DAO tengan un método con nombre parecido es razonable:

- La UI le pide la búsqueda al gestor.
- El gestor aplica las reglas de negocio.
- El gestor delega el acceso a datos en el DAO.
- El DAO devuelve los `FacturaDTO`.

La secuencia podría quedar más clara separando la llamada del retorno:

```text
UI → GestorFactura:
buscarFacturasPendientes(filtros)

GestorFactura → FacturaDAO:
buscarFacturasPendientes(filtros)

FacturaDAO --> GestorFactura:
facturas: FacturaDTO[]

GestorFactura --> UI:
facturas: FacturaDTO[]
```

Esta notación equivale a colocar directamente:

```text
facturas := buscarFacturasPendientes(filtros)
```

También cambiaría la condición:

```text
[f == NULL]
```

por algo más representativo:

```text
[facturas.isEmpty()]
```

o simplemente:

```text
[no se encontraron facturas]
```

Una colección vacía significa que la búsqueda se realizó pero no encontró resultados. `NULL` podría significar que ocurrió un error o que el método no devolvió correctamente una colección.

En conclusión: **`f :=` es solamente la asignación del resultado**, pero `buscarFacturas(...)` sí debería agregarse al diagrama de clases. Si no aparece, el ejemplo está incompleto o desactualizado respecto del diagrama de clases.
[Timestamp: 2026/09/23 20:44:54]

**user**: digamos esta bien que no exista el metodo buscarFacturas como tal es como para indicar que el emisor pide buscar las facturas y el receptor el DAO le devuelve lo que encuentra
[Timestamp: 2026/09/23 20:48:10]

**ai**: No exactamente. Si la flecha llega al `FacturaDAO` con el nombre:

```text
buscarFacturas(filtros)
```

entonces, en un **diagrama de secuencia de diseño**, eso significa que el receptor debe tener una operación compatible llamada `buscarFacturas(...)`.

Es decir:

```text
GestorFactura → FacturaDAO: buscarFacturas(filtros)
```

se interpreta como:

> El objeto `GestorFactura` invoca el método `buscarFacturas` del objeto `FacturaDAO`.

Después, el DAO devuelve el resultado:

```text
FacturaDAO --> GestorFactura: facturasEncontradas
```

Por tanto, en el diagrama de clases debería aparecer algo semejante a:

```text
FacturaDAO
+ buscarFacturas(filtros): FacturaDTO[]
```

La notación resumida:

```text
f := buscarFacturas(filtros)
```

combina la llamada y la asignación del resultado:

```java
FacturaDTO[] f = facturaDAO.buscarFacturas(filtros);
```

Puede aceptarse que el método todavía no aparezca si el diagrama de secuencia es preliminar o de análisis. En ese caso, el mensaje sirve para **descubrir una operación necesaria** y luego habría que actualizar el diagrama de clases.

La distinción sería:

- **Diagrama de análisis:** el mensaje puede representar una responsabilidad todavía no definida como método.
- **Diagrama de diseño:** el mensaje entre objetos debe corresponder con una operación del receptor.

En este ejemplo, como aparecen clases técnicas como `GestorFactura`, `FacturaDAO` y DTO, parece un diagrama bastante cercano al diseño. Por eso lo consistente sería agregar `buscarFacturas(...)` al `FacturaDAO` y probablemente también al `GestorFactura`.

Tu interpretación de “el gestor pide buscar y el DAO devuelve lo encontrado” es correcta conceptualmente. Lo que cambia es la notación: esa petición, cuando ocurre entre objetos del software, se materializa precisamente como un método del receptor.
[Timestamp: 2026/09/23 20:48:10]

**user**: entonces esta mal en el ejemplo?
[Timestamp: 2026/09/23 20:49:40]

**ai**: Sí, **hay una inconsistencia en el ejemplo**.

El diagrama de secuencia invoca:

```text
buscarFacturas(...)
```

sobre `GestorFactura` y `FacturaDAO`, pero ese método no figura en las clases receptoras del diagrama de clases mostrado.

Para corregirlo deberían agregar, por ejemplo:

```text
GestorFactura
+ buscarFacturas(filtros): FacturaDTO[]
```

```text
FacturaDAO
+ buscarFacturas(filtros): FacturaDTO[]
```

O utilizar otro método que ya exista y represente realmente esa operación. En el diagrama de clases mostrado no parece haber ninguno equivalente.

Una aclaración importante: el ejemplo puede estar mostrando cómo el diagrama de secuencia ayuda a **descubrir métodos que faltan**. En ese caso no estaría mal como borrador, pero el resultado final debería actualizar el diagrama de clases para mantener la consistencia.

Además, el ejemplo tiene otras dos imprecisiones:

- `[f == NULL]` parece representar “no se encontraron facturas”, pero sería más claro usar `[facturas.isEmpty()]`.
- Ese fragmento representa el flujo **4.A**, no el **2.A** de filtros vacíos.

Así que tu observación es correcta: **si ambos diagramas se presentan como versión final, el ejemplo está incompleto o mal sincronizado**.
[Timestamp: 2026/09/23 20:49:40]