---
epoch: 1793902936768
mode: agent
backendId: claude
sessionId: "28ac944f-9227-4b00-ba5b-e4b4e8b15847"
agentLabel: "✅ Para qué sirven ❌ Qué NO buscan Dar elementos reusables de…"
usage: '{"usedTokens":44757,"contextWindow":1000000,"inputTokens":2,"outputTokens":7,"cacheReadTokens":41907,"cacheWriteTokens":2841,"updatedAt":1793903981654}'
tags:
  - copilot-conversation
---

**user**: ✅ Para qué sirven	❌ Qué NO buscan
Dar elementos reusables de diseño	Imponer una alternativa sobre otras
No volver a buscar soluciones ya conocidas	Eliminar la creatividad del diseño
Formar un vocabulario común entre diseñadores	Ser de uso obligatorio
Estandarizar la forma de diseñar	
Facilitar el aprendizaje (condensan experiencia)	
explicame esto
[Timestamp: 2026/11/05 15:22:16]

**ai**: Esa tabla está en la sección 1 de tu resumen [[U5.1 - Patrones de Diseño (V2)]]. Responde dos preguntas: **para qué existen los patrones de diseño** y **qué no pretenden ser**. Te explico cada fila.

## ✅ Para qué sirven

**1. Dar elementos reusables de diseño**
Un patrón es una solución **probada** y **reutilizable**. No es código que copiás y pegás. Es una **estructura de clases** que podés adaptar a distintos problemas. Por ejemplo, State funciona igual para un `Pedido`, un `Semáforo` o una `Cuenta`: siempre hay un contexto que delega en su estado actual.

**2. No volver a buscar soluciones ya conocidas**
Muchos problemas de diseño se repiten, como tener un objeto que cambia de comportamiento según su estado o necesitar una sola instancia de una clase. Alguien ya los resolvió bien, así que no hace falta "reinventar la rueda" en cada proyecto. Te ahorrás tiempo y errores.

**3. Formar un vocabulario común entre diseñadores**
Si le decís a otro diseñador "acá usé un **Singleton**", ya sabe que hay constructor privado, un atributo `static` y un `getInstance()`, sin que se lo expliques. El nombre del patrón **resume un diseño entero en una palabra**. Eso hace más rápida la comunicación y la documentación.

**4. Estandarizar la forma de diseñar**
Como todos resuelven el mismo problema de la misma manera, los diseños se vuelven **predecibles**. Si abrís un sistema ajeno y ves una clase `EstadoRecibido` que implementa `EstadoPedido`, enseguida entendés cómo está armado.

**5. Facilitar el aprendizaje (condensan experiencia)**
Cada patrón resume años de experiencia de diseñadores expertos: qué funcionó, en qué casos conviene y qué consecuencias trae. Estudiarlos te enseña **buenas prácticas de diseño** (por ejemplo, State te enseña de paso el principio Open/Closed) sin tener que cometer todos esos errores vos mismo.

## ❌ Qué NO buscan

**1. Imponer una alternativa sobre otras**
Un patrón es **una** solución posible, no "la" solución correcta. Para el mismo problema puede haber otros diseños igual de válidos. Por ejemplo, si un objeto tiene 2 estados y casi no cambia de comportamiento, un simple `if` puede ser mejor que State.

**2. Eliminar la creatividad del diseño**
El patrón da un **esqueleto**, pero adaptarlo a tu caso sigue siendo trabajo tuyo: qué estados hay, qué transiciones, qué nombres, cómo se combina con otros patrones. No es una receta mecánica.

**3. Ser de uso obligatorio**
Esto se conecta con la frase clave que tenés justo abajo en la nota:

> **"Abusar o forzar el uso de los patrones puede ser un error."**

Usás un patrón **solo si tenés el problema que resuelve** (o uno muy parecido). Meter un Singleton "porque sí" genera estado global y acoplamiento. Meter State en un objeto con 2 estados le agrega clases y complejidad sin ningún beneficio.

## La idea de fondo

Las dos columnas dicen lo mismo desde dos lados. Los patrones son **herramientas de apoyo, no reglas**. La columna izquierda muestra todo lo que te dan. La derecha te recuerda que **el criterio lo seguís poniendo vos**.

Si te lo preguntan en el parcial, una buena forma de cerrar la respuesta es: *"Un patrón se aplica cuando el problema lo justifica. Forzarlo agrega complejidad innecesaria."*
[Timestamp: 2026/11/05 15:22:16]

**user**: Me gustaria que le agreges al resumen eso pero mucho mas breve a modo de explicacion de cada uno . Debe ser breve
[Timestamp: 2026/11/05 15:24:10]

**ai**: Listo. Agregué la explicación breve en la tabla de [[U5.1 - Patrones de Diseño (V2)]], en la sección 1. Cada ítem ahora tiene una frase corta después de la flecha. El resto de la nota no cambió y la "Frase clave" sigue justo debajo.

| ✅ Para qué sirven | ❌ Qué NO buscan |
| --- | --- |
| Dar elementos **reusables** de diseño → *una misma estructura se adapta a distintos problemas* | **Imponer** una alternativa sobre otras → *es **una** solución posible, no la única* |
| No volver a buscar soluciones ya conocidas → *no reinventar la rueda* | **Eliminar la creatividad** del diseño → *da el esqueleto; adaptarlo es trabajo del diseñador* |
| Formar un **vocabulario común** entre diseñadores → *"usé un Singleton" ya explica todo el diseño* | Ser de **uso obligatorio** → *solo se usa si tenés el problema que resuelve* |
| **Estandarizar** la forma de diseñar → *los diseños se vuelven predecibles y fáciles de leer* | |
| Facilitar el **aprendizaje** (condensan experiencia) → *resumen lo que a expertos les funcionó* | |
[Timestamp: 2026/11/05 15:24:10]

**user**: Explicame Catalogo GoF
[Timestamp: 2026/11/05 15:38:55]

**ai**: # Catálogo GoF

## Qué es

**GoF** significa *Gang of Four*, "la banda de los cuatro". Son los cuatro autores del libro *Design Patterns* (1994): Gamma, Helm, Johnson y Vlissides. En ese libro juntaron **23 patrones de diseño** y los ordenaron en una tabla con **dos criterios**. Ese es el catálogo que tenés en [[U5.1 - Patrones de Diseño (V2)]].

## Criterio 1: Propósito (las columnas)

Indica **qué tipo de problema resuelve** el patrón:

- **Creación**: cómo se **crean** los objetos. Ejemplo: Singleton garantiza que haya una sola instancia.
- **Estructura**: cómo se **combinan** clases y objetos para formar estructuras más grandes. Ejemplo: Facade pone una interfaz simple delante de un subsistema complejo.
- **Comportamiento**: cómo los objetos **se comunican** y **se reparten responsabilidades**. Ejemplo: State delega el comportamiento en el estado actual.

## Criterio 2: Alcance (las filas)

Indica **cómo se arma la relación** entre las clases del patrón:

- **De clase**: la relación se arma con **herencia**. Queda **fija al compilar**: una subclase es lo que es y no cambia mientras el programa corre.
- **De objeto**: la relación se arma con **composición**, es decir, un objeto tiene una referencia a otro. **Puede cambiar en ejecución**, porque basta con cambiar la referencia por otro objeto.

> [!example] Ejemplo con State
> State es **de objeto** porque el `Pedido` tiene un atributo `estado`, y en ejecución hace `setEstado(new EstadoListo())`. El comportamiento cambia mientras el programa corre, cosa que con herencia sería imposible.

## La tabla, leída

| Alcance \ Propósito | Creación | Estructura | Comportamiento |
| --- | --- | --- | --- |
| **Clase** (herencia) | Factory Method | Adapter | Interpreter, Template Method |
| **Objeto** (composición) | Abstract Factory, Builder, Prototype, **Singleton** | Adapter, **Bridge**, Composite, Decorator, **Facade**, Proxy | Chain of Responsibility, Command, Iterator, **Mediator**, Memento, Observer, **State**, Strategy, Visitor |

Al leerla conviene notar tres cosas:
- **La mayoría son de objeto.** Esto refleja un principio del propio libro: *preferir composición sobre herencia*, porque la composición es más flexible.
- **En negrita están los que entran en tu unidad.** Singleton y State los ves en la U5.1. Facade, Bridge y Mediator, en [[U5.2 - Patrones de Diseño II (V2)]]. El resto solo aparece en el catálogo.
- **Adapter está en las dos filas** porque tiene dos versiones. Una adapta **heredando** de la clase a adaptar (de clase). La otra adapta **teniendo una referencia** a ella (de objeto).

> [!warning] Error de la diapositiva
> La diapositiva pone **Flyweight** en *comportamiento*, pero en el libro GoF es **estructural**: sirve para compartir objetos y ahorrar memoria. En la tabla de arriba lo saqué de comportamiento y no lo agregué en estructura, para respetar el contenido de la diapositiva. Si te lo preguntan, la respuesta correcta es estructural.

## Cómo usarlo en el parcial

Si te piden **clasificar** un patrón, nombrá los dos ejes:

> *"State es un patrón **de comportamiento** con **alcance de objeto**: resuelve cómo varía el comportamiento según el estado, y lo logra con composición, porque el contexto tiene una referencia a su estado actual y la puede cambiar en ejecución."*
[Timestamp: 2026/11/05 15:38:55]