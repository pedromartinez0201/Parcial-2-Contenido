---
epoch: 1793990506622
mode: agent
backendId: claude
sessionId: "9c045ffa-61ab-4e9e-80f9-dcb0cbcdac3b"
agentLabel: "En S de principios , razon para cambiar hace referencia a la…"
usage: '{"usedTokens":153967,"contextWindow":1000000,"inputTokens":4,"outputTokens":3,"cacheReadTokens":153427,"cacheWriteTokens":533,"updatedAt":1794010588382}'
tags:
  - copilot-conversation
---

**user**: En S de principios , razon para cambiar hace referencia a la razon para modificar el codigo ?
[Timestamp: 2026/11/06 15:41:46]

**ai**: **Sí.** "Razón para cambiar" significa un motivo por el que tendrías que volver a abrir esa clase y modificar su código.

Sin embargo, no se refiere a cualquier edición, como arreglar un typo o renombrar una variable. Apunta al **origen del cambio**: qué necesidad o requisito distinto te obligaría a tocar la clase. Martin lo resume más tarde así: una razón para cambiar equivale a **un actor o interesado** que puede pedir ese cambio.

**Ejemplo de tu nota: `ReportManager`**

| Si cambia... | Hay que modificar | Razón para cambiar |
| --- | --- | --- |
| El contenido o formato del reporte | La parte que lo genera | Generación |
| Dónde o cómo se guarda (por ejemplo, de archivo a BD) | La parte que lo guarda | Persistencia |
| Cómo se envía (por ejemplo, de SMTP a otro proveedor) | La parte del email | Notificación |

Son 3 motivos independientes que caen sobre la misma clase, así que viola SRP. Tocar el envío de emails podría romper la generación de reportes, y por eso la nota menciona los **errores colaterales** como lo que SRP evita.

Al separarla, cada clase queda con un solo motivo:
- `ReportGenerator` cambia solo si cambia la generación.
- `ReportSaver` cambia solo si cambia la persistencia.
- `EmailService` cambia solo si cambia el envío.

**Cómo detectarlo:** preguntate "¿qué cosas distintas podrían obligarme a modificar esta clase?". Si la respuesta incluye más de un motivo no relacionado, probablemente viola SRP.

**Para el parcial:** SRP no significa "una clase, un solo método". Una clase puede tener varios métodos y cumplirlo, siempre que todos respondan a la misma razón para cambiar. Por eso se relaciona con la **cohesión**.

Referencia: [[U5.4 - SOLID (V2)]], sección "S — Responsabilidad Única".
[Timestamp: 2026/11/06 15:41:46]

**user**: Y la señan de violacion "hace X y Y y Z " sirve para darme cuenta que no tiene una responsabilidad unica?
[Timestamp: 2026/11/06 15:43:35]

**ai**: **Sí, sirve, pero como alerta y no como prueba definitiva.** Si para describir la clase necesitás varios "y", conviene revisar si esas tareas tienen razones distintas para cambiar.

**Cuándo el "y" indica una violación**

`ReportManager` "genera el reporte **y** lo guarda **y** lo envía por email". Cada "y" une tareas que pueden cambiar por motivos independientes: el formato, la persistencia y el envío. Acá la señal acierta.

**Cuándo el "y" no indica una violación**

`Carrito` "agrega productos **y** quita productos **y** calcula el total". Hay varios "y", pero todo responde a una misma responsabilidad, gestionar el contenido del carrito, así que probablemente cambien por el mismo motivo.

También importa cómo describís la clase. Decir que `ReportManager` "gestiona reportes" evita los "y", pero no arregla nada, porque sigue teniendo las 3 razones para cambiar. Por eso, las palabras como "gestiona" o "maneja" también merecen una segunda mirada.

**Cómo usarla en dos pasos**

1. **Describí la clase en concreto**, sin términos genéricos, y mirá si aparecen varios "y".
2. **Preguntate por cada parte unida con "y":** ¿podría cambiar por un motivo que no afecte a las otras?
   - Si la respuesta es sí, probablemente viola SRP y conviene separarla.
   - Si la respuesta es no, probablemente sea la misma responsabilidad y la clase esté bien.

**Para el parcial:** el criterio que vale es la **razón para cambiar**, y el "y" es solo una forma rápida de detectar el problema. Conviene justificar con algo como "viola SRP porque tiene más de una razón para cambiar: X e Y". Además, esta señal está marcada como *(extra)* en tu nota, así que no sale del apunte de la cátedra.
[Timestamp: 2026/11/06 15:43:35]

**user**: que significa SRP
[Timestamp: 2026/11/06 15:45:24]

**ai**: **SRP** son las siglas de **Single Responsibility Principle**, en español **Principio de Responsabilidad Única**. Es la **S** de SOLID.

Las siglas de los otros principios también vienen del inglés:

| Letra | Sigla | En inglés | En español |
| --- | --- | --- | --- |
| **S** | SRP | Single Responsibility Principle | Responsabilidad Única |
| **O** | OCP | Open/Closed Principle | Abierto-Cerrado |
| **L** | LSP | Liskov Substitution Principle | Sustitución de Liskov |
| **I** | ISP | Interface Segregation Principle | Segregación de Interfaces |
| **D** | DIP | Dependency Inversion Principle | Inversión de Dependencias |
[Timestamp: 2026/11/06 15:45:24]

**user**: cuando dice cada clase o modulo , a que hace referencia con modulo
[Timestamp: 2026/11/06 15:46:03]

**ai**: **Módulo** es cualquier unidad de código que agrupa cosas relacionadas para cumplir un propósito y que se puede tratar como una pieza del sistema. No tiene una definición única, porque su tamaño y forma dependen del lenguaje y del diseño.

Según el contexto, puede ser:
- **Un archivo:** por ejemplo, `reportes.py` en Python, con funciones y clases relacionadas.
- **Un paquete o namespace:** por ejemplo, un `package` en Java o un `namespace` en C#.
- **Un componente del sistema:** por ejemplo, el módulo de "Facturación" o de "Notificaciones", formado por varias clases.

**¿Por qué la definición dice "clase o módulo"?** Porque SRP no se aplica solo a las clases, sino también a unidades más grandes. Un módulo de "Facturación" debería ocuparse de facturar, no también de enviar campañas de marketing. Si mezcla ambas cosas, tiene dos razones para cambiar, igual que `ReportManager` a nivel de clase.

**Otro uso en tu nota:** en DIP, "módulos de alto nivel" y "de bajo nivel" tienen el mismo sentido amplio. Ahí el ejemplo de alto nivel es `OrderService` y el de bajo nivel es `EmailService`, así que un módulo también puede ser una sola clase.
[Timestamp: 2026/11/06 15:46:03]

**user**: digamos que no se aplica solo a las clases sino que el modulo Notificacion que tiene .java y .py no deberia de modificarse el .py por guardar informacion de marketin por ejemplo
[Timestamp: 2026/11/06 15:48:11]

**ai**: **Sí, la idea es correcta:** guardar información de marketing no le corresponde al módulo `Notificacion`, porque le agrega una segunda razón para cambiar.

Solo le haría un ajuste a tu ejemplo: **no importa si es el `.py` o el `.java`**. El problema es que esa responsabilidad entre al módulo, sin importar el archivo o lenguaje donde la pongas. Tampoco se resuelve creando un archivo nuevo dentro del módulo, como `marketing.py`, porque `Notificacion` seguiría teniendo las dos responsabilidades.

| Módulo | Responsabilidad | Razón para cambiar |
| --- | --- | --- |
| `Notificacion` | Enviar notificaciones | Cambia cómo se envían, por ejemplo, de proveedor de email |
| `Marketing` | Gestionar campañas y sus datos | Cambian las reglas o los datos de las campañas |

**¿Y si una campaña tiene que enviar notificaciones?** `Marketing` puede **usar** a `Notificacion`: guarda sus datos y le pide que envíe el mensaje. Así, `Notificacion` no necesita saber qué es una campaña.

**Una aclaración:** modificar `Notificacion` por un cambio pedido desde marketing no siempre viola SRP. Por ejemplo, si piden enviar también por WhatsApp, el pedido viene de marketing, pero el cambio sigue siendo sobre cómo se envían las notificaciones. En cambio, guardar datos de campañas no tiene relación con esa responsabilidad.
[Timestamp: 2026/11/06 15:48:11]

**user**: que era acoplamiento era cuanto depende una clase por ejemplo de otras
[Timestamp: 2026/11/06 15:49:28]

**ai**: **Sí.** El **acoplamiento** es el grado en que una clase o módulo depende de otros. Importa tanto la cantidad de dependencias como lo fuertes que son: cuánto necesita saber una clase sobre los detalles internos de la otra.

En diseño se busca **bajo acoplamiento**, para que un cambio en una clase afecte lo menos posible a las demás.

**Ejemplo con tu nota (DIP)**

Acoplamiento más alto, porque `OrderService` depende de una clase concreta y la crea:

```java
class OrderService {
    private EmailService notificador = new EmailService();
}
```

Si querés cambiar email por SMS, tenés que modificar `OrderService`.

Acoplamiento más bajo, porque depende de una abstracción y la recibe desde afuera:

```java
class OrderService {
    private NotificationService notificador;

    public OrderService(NotificationService notificador) {
        this.notificador = notificador;
    }
}
```

Podés pasarle otra implementación sin tocar `OrderService`. Sigue teniendo una dependencia, pero ya no está atado a una implementación concreta. El objetivo no es eliminar todas las dependencias, porque las clases necesitan colaborar entre sí, sino evitar las innecesarias o demasiado rígidas.

**No confundir con cohesión**

| Concepto | Qué mide | Lo deseable |
| --- | --- | --- |
| **Acoplamiento** | Cuánto depende una clase de **otras** | **Bajo** |
| **Cohesión** | Cuán relacionadas están las tareas **dentro** de una clase | **Alta** |

Por eso, en tu nota, SRP se relaciona con la cohesión y DIP con el acoplamiento.
[Timestamp: 2026/11/06 15:49:28]

**user**: explicame el por que de  **Ventajas:** facilita el mantenimiento, evita errores colaterales, mejora la reutilización y favorece las pruebas unitarias.
[Timestamp: 2026/11/06 15:50:30]

**ai**: Las cuatro ventajas tienen la misma causa: **si cada clase hace una sola cosa, cada cambio y cada prueba queda limitado a una parte chica del código.** Lo vemos con `ReportManager`, separado en `ReportGenerator`, `ReportSaver` y `EmailService`.

**1. Facilita el mantenimiento**

Cuando algo cambia, sabés dónde ir y tenés menos código para leer. Si cambia el proveedor de email, vas directo a `EmailService`. Con todo en `ReportManager`, primero tendrías que encontrar esa parte entre la generación y el guardado.

**2. Evita errores colaterales**

Un error colateral aparece cuando cambiás una cosa y se rompe otra que no querías tocar. Si las tres tareas conviven en una clase, pueden compartir atributos y métodos auxiliares. Por ejemplo, podrías cambiar un atributo pensando en el email y romper sin querer el guardado. Al separarlas, ese riesgo baja porque cada clase tiene su propio código. Igual no desaparece del todo, porque un error todavía puede afectar a las clases que la usan.

**3. Mejora la reutilización**

Podés usar una clase sin arrastrar lo que no necesitás. Si otra parte del sistema quiere enviar emails, por ejemplo para recuperar contraseñas, puede usar `EmailService`. Si el envío estuviera dentro de `ReportManager`, tendrías que depender de una clase que también genera y guarda reportes, o copiar el código.

**4. Favorece las pruebas unitarias**

Una prueba unitaria verifica una pieza de código de forma aislada. Con clases separadas:
- **Hay menos que preparar:** para probar `ReportGenerator`, no necesitás una base de datos ni un servidor de email.
- **Los casos son más simples:** probás solo el comportamiento de esa clase, sin combinarlo con los otros.
- **Las fallas son más claras:** si falla la prueba de `ReportSaver`, el problema probablemente esté en el guardado.

Con todo junto, probar la generación del reporte podría terminar guardando archivos o enviando emails reales.

**Para el parcial:** podés resumirlo así: "al tener una sola razón para cambiar, los cambios quedan localizados, se reduce el impacto sobre el resto del sistema y la clase resulta más fácil de reutilizar y probar".
[Timestamp: 2026/11/06 15:50:30]

**user**: 3. Mejora la reutilizacion por que ?
[Timestamp: 2026/11/06 15:52:09]

**ai**: Porque **una clase con una sola responsabilidad se puede usar en otro lugar sin traer funcionalidades que ese lugar no necesita.**

Supongamos que el sistema de recuperar contraseñas necesita enviar un email.

**Sin SRP:** el envío está dentro de `ReportManager`.

```java
class ReportManager {
    void generar() { ... }
    void guardar() { ... }
    void enviarEmail() { ... }
}
```

Para recuperar contraseñas tenés dos opciones, y ninguna es buena:
- **Usar `ReportManager`:** dependés de una clase de reportes solo para enviar un email. Además, un cambio en la generación o el guardado podría afectarte, y quizás ni siquiera puedas crear esa clase sin configurar lo que necesita para generar y guardar reportes.
- **Copiar el código de `enviarEmail()`:** queda duplicado, y si cambia el proveedor de email tenés que modificarlo en dos lugares.

**Con SRP:** el envío está en su propia clase.

```java
class EmailService {
    void enviar(String destino, String mensaje) { ... }
}
```

Tanto los reportes como la recuperación de contraseñas pueden usar `EmailService`. El código del envío queda en un solo lugar y ninguno de los dos depende del otro.

**Una analogía:** es como querer usar solo un destornillador. Si viene suelto, agarrás ese. Si viene soldado a un taladro y una sierra, tenés que cargar con todo para usar una sola herramienta.
[Timestamp: 2026/11/06 15:52:09]

**user**: Claro y 4. por que una prueba unitaria testea una pieza de codigo de forma aislada
[Timestamp: 2026/11/06 15:57:25]

**ai**: Porque el objetivo de una prueba unitaria es comprobar **si esa pieza funciona bien por sí sola**. Si dependiera de otras partes, una falla no te diría dónde está el problema.

Por ejemplo, supongamos que una prueba de `ReportGenerator` usa también una base de datos real y un servidor de email reales. Si falla, el error podría estar en la generación, en la base de datos, en el servidor o incluso en la conexión de red.

**Qué ganás al aislarla**

- **Sabés dónde buscar:** si falla, el problema probablemente esté en esa pieza o en la prueba misma.
- **Es rápida:** no espera respuestas de una base de datos o de la red, así que podés ejecutar muchas pruebas seguido.
- **Es estable:** no falla porque se cayó la red o porque cambiaron los datos de la base.
- **No tiene efectos secundarios:** no envía emails reales ni modifica datos reales.

**¿Y si la clase necesita a otra?**

Se reemplaza esa dependencia por un objeto de prueba, a menudo llamado *mock*. Por ejemplo, un `OrderService` que recibe un `NotificationService` se puede probar con una versión falsa de la notificación:

```java
NotificationService falso = mock(NotificationService.class);
OrderService service = new OrderService(falso);

service.confirmarPedido(pedido);

verify(falso).enviar(any());
```

Esta prueba (acá con la librería Mockito) verifica que `OrderService` pidió enviar la notificación, sin enviar un mensaje real. Esto es posible porque `OrderService` recibe la dependencia desde afuera, que es lo que propone **DIP**.

**Cómo se relaciona con SRP:** cuanto menos cosas hace una clase, menos dependencias suele necesitar y menos hay que aislar. Por eso SRP favorece las pruebas unitarias.

**Las otras pruebas también hacen falta:** el aislamiento no comprueba que las piezas funcionen bien juntas. Para eso están las **pruebas de integración**, que sí pueden usar una base de datos real, por ejemplo.
[Timestamp: 2026/11/06 15:57:25]

**user**: Ahora que significa OCP
[Timestamp: 2026/11/06 16:00:03]

**ai**: **OCP** son las siglas de **Open/Closed Principle**, en español **Principio de Abierto-Cerrado**. Es la **O** de SOLID y dice que el software debe estar:

- **Abierto para la extensión:** se le puede agregar comportamiento nuevo.
- **Cerrado para la modificación:** para eso no hace falta cambiar el código que ya funciona.

En resumen, **agregás funcionalidad con código nuevo en lugar de editar el existente.**

**Ejemplo de tu nota: calcular áreas**

Sin OCP, cada figura nueva obliga a modificar el método:

```csharp
double CalcularArea(object figura) {
    if (figura is Circulo c) return Math.PI * c.Radio * c.Radio;
    else if (figura is Rectangulo r) return r.Ancho * r.Alto;
    throw new ArgumentException("Figura no soportada");
}
```

Para agregar un triángulo, tenés que sumar otro `else if` a un método que ya estaba probado, y podrías romper algo.

Con OCP, cada figura implementa una interfaz:

```csharp
interface IFigura {
    double CalcularArea();
}

class Circulo : IFigura {
    public double Radio { get; set; }
    public double CalcularArea() => Math.PI * Radio * Radio;
}

class Rectangulo : IFigura {
    public double Ancho { get; set; }
    public double Alto { get; set; }
    public double CalcularArea() => Ancho * Alto;
}
```

Para agregar un triángulo, creás una clase nueva:

```csharp
class Triangulo : IFigura {
    public double Base { get; set; }
    public double Altura { get; set; }
    public double CalcularArea() => Base * Altura / 2;
}
```

El código que usa `IFigura` no cambia, porque solo llama a `figura.CalcularArea()` sin preguntar de qué tipo es. Esto funciona gracias al **polimorfismo**: cada figura resuelve el cálculo a su manera.

**Señal de violación:** cadenas de `if/else` o `switch` por tipo que tenés que editar cada vez que aparece un caso nuevo.

**Dos aclaraciones**

- **"Cerrado" no significa que nunca se pueda tocar:** si hay un bug, lo corregís. El principio apunta a que **agregar comportamiento nuevo** no te obligue a modificar lo existente.
- **Algún punto del sistema suele cambiar:** por ejemplo, el lugar donde se crea el `new Triangulo()`. Lo importante es que no cambie la lógica que trabaja con `IFigura`.
[Timestamp: 2026/11/06 16:00:03]

**user**: Ahora explicame de forma resumida cada ventaja de OCP
[Timestamp: 2026/11/06 16:02:22]

**ai**: Las ventajas de OCP que lista tu nota salen de la misma idea: **lo nuevo se agrega en clases nuevas, sin editar lo que ya funciona.**

- **Reduce el impacto de los cambios:** agregar `Triangulo` no obliga a tocar `Circulo`, `Rectangulo` ni el código que usa `IFigura`. El cambio queda concentrado en la clase nueva y en el lugar donde se crea.
- **No rompe lo ya probado:** si no editás el código existente, es difícil introducirle errores nuevos. Igual conviene volver a ejecutar las pruebas y probar la clase nueva.
- **Favorece abstracciones e interfaces:** para poder agregar clases sin tocar el resto, el código tiene que depender de un contrato común, como `IFigura`, y no de cada figura concreta.
- **Fomenta la reutilización:** el código escrito para `IFigura` sirve para cualquier figura, incluso las que se creen más adelante. Por ejemplo, un método que suma áreas funciona igual con círculos, rectángulos o triángulos.
- **Fomenta la mantenibilidad:** cada figura tiene su cálculo en su propia clase, en lugar de estar todo en una cadena de `if/else`. Así es más fácil encontrar qué modificar y entender cada caso.
[Timestamp: 2026/11/06 16:02:22]

**user**: que seria una entidad de software
[Timestamp: 2026/11/06 16:04:05]

**ai**: Una **entidad de software** es cualquier pieza de código que tenga una función propia dentro del programa. Es un término general para no limitar el principio a un solo tipo de elemento.

En la definición de OCP, suele referirse a:

- **Clases:** por ejemplo, `Circulo`.
- **Módulos:** por ejemplo, el módulo `Notificacion`.
- **Funciones o métodos:** por ejemplo, `CalcularArea()`.

Entonces, cuando OCP dice que "las entidades de software deben estar abiertas para la extensión y cerradas para la modificación", significa que esto vale para cualquiera de esas piezas. Por ejemplo, tu nota muestra que el método `CalcularArea(object figura)` viola OCP porque hay que modificarlo cada vez que aparece una figura nueva.

**No confundir con otros usos de "entidad":** no es lo mismo que una entidad de base de datos, como la tabla `Cliente`, o una entidad del dominio, como `Pedido`. En OCP, "entidad" es simplemente una pieza de código.
[Timestamp: 2026/11/06 16:04:05]

**user**: En OCP agregalo como extra o recordatorio o glosario resumido corto a que hace referencia y tambien en SRP a lo que dice de modulo
[Timestamp: 2026/11/06 16:05:14]

**ai**: Listo, agregué las dos aclaraciones a [[U5.4 - SOLID (V2)]] como callouts `Glosario (extra)`, justo debajo de cada definición:

- **SRP:** explica qué es un **módulo**.
- **OCP:** explica qué es una **entidad de software** y aclara que no es una entidad de base de datos ni del dominio.

También vi los cambios que hiciste mientras estudiabas, como las secciones `### Ventajas`, y no los toqué. Lo único que cambió son esos dos callouts.

**Errores que encontré en tus cambios (no los corregí):**
- **Línea 35:** dice "Single Responsability Principie"; lo correcto es "Single **Responsibility Principle**".
- **Línea 50:** dice "Open/Closed Principie"; lo correcto es "Open/Closed **Principle**".
- **Línea 60:** el espacio antes del cierre en `**Reduce el impacto de los cambios **` puede hacer que la negrita no se muestre bien.

**Ventajas de OCP repetidas:** en la línea 56 todavía está la lista resumida, y en la 59 empezaste la sección `### Ventajas`. En SRP sacaste la lista cuando armaste esa sección, así que cuando la termines podrías hacer lo mismo acá.

¿Querés que corrija esos errores?
[Timestamp: 2026/11/06 16:05:14]

**user**: que es una clase derivada
[Timestamp: 2026/11/06 16:16:50]

**ai**: Una **clase derivada** (también llamada **subclase** o **clase hija**) es una clase que **hereda** de otra, la **clase base** (también llamada **superclase** o **clase padre**). Recibe los atributos y métodos accesibles de la base, y puede agregar los suyos o redefinir los que la base permite.

**Ejemplo de tu nota (LSP):**

```csharp
class Ave {                       // clase base
    public virtual void Comer() { ... }
}

class Gorrion : Ave {             // clase derivada
    public void Volar() { ... }   // agrega un método propio
}
```

`Gorrion` hereda `Comer()` sin tener que escribirlo de nuevo y además suma `Volar()`. Como `Gorrion` **es un** `Ave`, se puede usar donde se espera un `Ave`:

```csharp
Ave ave = new Gorrion();
ave.Comer();
```

**Cómo se relaciona con LSP:** cuando la definición dice que los objetos de una clase derivada deben poder sustituir a los de la clase base, significa que el código que usa un `Ave` tiene que seguir funcionando bien si recibe un `Gorrion` o cualquier otra derivada.

Por eso, en tu nota, `Pinguino` viola LSP: si `Ave` tuviera `Volar()`, `Pinguino` lo heredaría y lanzaría una excepción al llamarlo. El código que espera que cualquier `Ave` pueda volar se rompería.
[Timestamp: 2026/11/06 16:16:50]

**user**: Agregamelo como glosario en Sustitucion de Liskov
[Timestamp: 2026/11/06 16:17:17]

**ai**: Listo, agregué **clase derivada** como `Glosario (extra)` en la sección de Sustitución de Liskov de [[U5.4 - SOLID (V2)]], justo debajo de la definición. También incluye los otros nombres que pueden aparecer: subclase, clase hija, clase base, superclase y clase padre.

El ejemplo `Gorrion : Ave` lo inventé para explicártelo, así que no sale del apunte de la cátedra. La nota volvió a cambiar mientras estudiabas, y no toqué nada más.
[Timestamp: 2026/11/06 16:17:17]

**user**: Explicame LSP
[Timestamp: 2026/11/06 16:20:30]

**ai**: **LSP** son las siglas de **Liskov Substitution Principle**, en español **Principio de Sustitución de Liskov**. Es la **L** de SOLID y dice que **una clase derivada tiene que poder reemplazar a su clase base sin romper el programa**.

En otras palabras, el código que usa la clase base no debería tener que saber qué derivada recibió. Si la base promete algo, todas las derivadas tienen que cumplirlo.

**Ejemplo de tu nota: aves que vuelan**

Sin LSP, `Ave` promete que todas las aves vuelan, pero `Pinguino` no puede cumplirlo:

```csharp
class Ave {
    public virtual void Volar() { Console.WriteLine("Volando"); }
}

class Pinguino : Ave {
    public override void Volar() {
        throw new NotImplementedException();
    }
}
```

El problema aparece en el código que usa `Ave`:

```csharp
void HacerVolar(Ave ave) {
    ave.Volar();
}

HacerVolar(new Pinguino());   // lanza una excepción
```

`HacerVolar` confía en lo que promete `Ave`, y aun así falla con un `Pinguino`. Por eso, `Pinguino` no puede sustituir a `Ave`.

Con LSP, `Volar()` pasa a una interfaz que implementan solo las aves que vuelan:

```csharp
class Ave { }

interface IVolador {
    void Volar();
}

class Gorrion : Ave, IVolador {
    public void Volar() { Console.WriteLine("Volando"); }
}

class Pinguino : Ave { }
```

Ahora `HacerVolar` recibe un `IVolador`, así que no se le puede pasar un `Pinguino`:

```csharp
void HacerVolar(IVolador volador) {
    volador.Volar();
}
```

**La analogía de tu nota:** un control remoto universal (la base) tiene que funcionar con cualquier televisor (las derivadas). Si un modelo no responde a los mismos comandos, el control deja de servir.

**Señales de violación**

- Una subclase lanza una excepción en un método heredado.
- El código tiene que preguntar por el tipo concreto, como `if (obj is Pinguino)`.
- Una subclase hace algo distinto de lo que promete la base, aunque no lance ninguna excepción.

**Para el parcial:** la frase clave es *"es un" no alcanza: tiene que "comportarse como"*. En la realidad, un pingüino **es un** ave, pero acá no se **comporta como** el `Ave` del código, porque no vuela. Heredar solo porque "suena lógico" no garantiza cumplir LSP.
[Timestamp: 2026/11/06 16:20:30]

**user**: Ahora explicame las ventajas en una frase corta
[Timestamp: 2026/11/06 16:27:11]

**ai**: Las ventajas de LSP que lista tu nota, cada una en una frase:

- **Evita errores sutiles al heredar:** una subclase no falla ni se comporta de forma inesperada cuando reemplaza a la base.
- **Mantiene el comportamiento coherente al sustituir:** el programa sigue funcionando bien, sin importar qué derivada reciba.
- **Da polimorfismo seguro:** podés usar cualquier derivada a través de la base sin preguntar de qué tipo es.
- **Mejora la reutilización:** el código escrito para la base sirve también para todas sus derivadas.
- **Fija un contrato claro:** queda definido qué promete la base y qué debe cumplir cada subclase.
[Timestamp: 2026/11/06 16:27:11]

**user**: Mantiene el compartmiento coherente al sustituir quiere decir que sea cualquiera de la derivada que sustituya va a funcionar bien
[Timestamp: 2026/11/06 16:31:46]

**ai**: **Sí, exacto:** si se cumple LSP, cualquier derivada que uses en lugar de la base va a funcionar bien, porque todas respetan lo que la base promete.

Eso no significa que todas hagan lo mismo por dentro. Cada una puede hacerlo a su manera, siempre que cumpla la promesa:

```csharp
interface IFigura {
    double CalcularArea();   // promete devolver el área de la figura
}
```

- **`Circulo`:** calcula $\pi r^2$.
- **`Rectangulo`:** calcula ancho por alto.

Las fórmulas son distintas, pero el comportamiento es coherente, porque las dos devuelven el área. En cambio, no sería coherente una figura que lanzara una excepción o que devolviera siempre `0`.
[Timestamp: 2026/11/06 16:31:46]

**user**: Ahora que significa ISP
[Timestamp: 2026/11/06 16:34:34]

**ai**: **ISP** son las siglas de **Interface Segregation Principle**, en español **Principio de Segregación de Interfaces**. Es la **I** de SOLID y dice que **una clase no debería verse obligada a depender de métodos que no usa**.

"Segregar" significa separar. Por eso, es mejor tener varias interfaces chicas y específicas que una sola grande y genérica.

**Ejemplo de tu nota: vehículos**

Sin ISP, una sola interfaz obliga a `Auto` a tener métodos que no le sirven:

```csharp
interface IVehiculo {
    void Conducir();
    void Volar();
    void Navegar();
}

class Auto : IVehiculo {
    public void Conducir() { Console.WriteLine("Conduciendo"); }
    public void Volar() { throw new NotImplementedException(); }
    public void Navegar() { throw new NotImplementedException(); }
}
```

Con ISP, la interfaz se separa y cada clase implementa solo lo que puede hacer:

```csharp
interface IConducible { void Conducir(); }
interface IVolador { void Volar(); }
interface INavegable { void Navegar(); }

class Auto : IConducible {
    public void Conducir() { Console.WriteLine("Conduciendo"); }
}

class AutoVolador : IConducible, IVolador {
    public void Conducir() { Console.WriteLine("Conduciendo"); }
    public void Volar() { Console.WriteLine("Volando"); }
}
```

Como una clase puede implementar varias interfaces, `AutoVolador` puede combinar las que necesita. Además, el código que solo necesita conducir puede pedir un `IConducible`, sin depender de `Volar()` ni `Navegar()`.

**Señales de violación**

- Una clase deja métodos vacíos o con `throw` porque la interfaz la obliga a implementarlos.
- Una interfaz reúne métodos que no suelen usarse juntos.

**Para el parcial:** como dice tu nota, **ISP** mira las interfaces (¿obligan a implementar cosas que no se usan?), mientras que **LSP** mira la herencia (¿la subclase cumple lo que promete la base?). Suelen aparecer juntos, porque una interfaz demasiado grande termina en métodos con `throw`.
[Timestamp: 2026/11/06 16:34:34]

**user**: Ahora DIP
[Timestamp: 2026/11/06 16:43:43]

**ai**: **DIP** son las siglas de **Dependency Inversion Principle**, en español **Principio de Inversión de Dependencias**. Es la **D** de SOLID y dice dos cosas:

1. Los **módulos de alto nivel no deben depender de los de bajo nivel**; ambos deben depender de **abstracciones**.
2. Las abstracciones no dependen de los detalles; **los detalles dependen de las abstracciones**.

**Los tres conceptos**

| Concepto | Qué es | Ejemplo de tu nota |
| --- | --- | --- |
| **Alto nivel** | Orquesta la lógica de negocio | `OrderService` |
| **Bajo nivel** | Ejecuta detalles concretos | `EmailService` |
| **Abstracción** | Contrato sin implementación | `NotificationService` |

**Ejemplo**

Sin DIP, la lógica de negocio depende directamente de un detalle:

```java
class OrderService {
    private EmailService notificador = new EmailService();
}
```

La dependencia va así: `OrderService → EmailService`. Si querés notificar por SMS, tenés que modificar `OrderService`, aunque las reglas del pedido no hayan cambiado.

Con DIP, los dos dependen de una interfaz:

```java
interface NotificationService {
    void enviar(String mensaje);
}

class EmailService implements NotificationService {
    public void enviar(String mensaje) { /* envía un email */ }
}

class OrderService {
    private NotificationService notificador;

    public OrderService(NotificationService notificador) {
        this.notificador = notificador;
    }
}
```

Ahora la dependencia va así: `OrderService → NotificationService ← EmailService`.

**¿Qué se invierte?** Antes, la clase de bajo nivel no dependía de ninguna abstracción, y la de alto nivel dependía de ella. Ahora, `EmailService` **depende de la abstracción**, porque tiene que cumplir ese contrato. Para sumar SMS, creás `SmsService` y `OrderService` no cambia.

**DIP, IoC y DI**

- **DIP** es el principio: depender de abstracciones.
- **IoC (Inversión de Control):** otro decide cuándo y cómo se crean los objetos, como un contenedor o un framework.
- **DI (Inyección de Dependencias):** es una forma concreta de IoC, en la que la clase no crea sus dependencias, sino que las recibe. El constructor de `OrderService` es un ejemplo.

Las dependencias se pueden inyectar de tres formas: por **constructor** (la más común), por **propiedad** o por **método**.

**Señales de violación**

- La lógica de negocio crea sus dependencias con `new EmailService()`.
- Una clase de alto nivel declara atributos o parámetros de una clase concreta en lugar de una interfaz.

**Para el parcial**

- Frase clave de tu nota: **toda DI aplica IoC, pero no toda IoC usa DI**. Por ejemplo, los *callbacks* y los *eventos* son IoC sin DI.
- No hay que confundir DIP con DI: DIP indica de qué depender, y DI es una forma de entregar esa dependencia a la clase.
[Timestamp: 2026/11/06 16:43:43]

**user**: explicame esto
[Timestamp: 2026/11/06 16:58:45]

**ai**: La tabla compara una idea general con una forma concreta de aplicarla: **IoC** es ceder el control a algo externo, y **DI** es una manera de hacerlo, en la que la clase recibe lo que necesita.

**Sin IoC ni DI: tu clase controla todo**

```java
class OrderService {
    private EmailService notificador = new EmailService();
}
```

`OrderService` decide qué dependencia usar y cuándo crearla.

**Con DI: la clase recibe la dependencia**

```java
class OrderService {
    private NotificationService notificador;

    public OrderService(NotificationService notificador) {
        this.notificador = notificador;
    }
}
```

Ahora `OrderService` no crea el notificador. Alguien de afuera se lo entrega:

```java
OrderService service = new OrderService(new EmailService());
```

Eso es "inyectar desde afuera". `OrderService` usa el notificador, pero ya no decide cuál se crea.

**Con un contenedor: otro crea y gestiona los objetos**

En lugar de escribir esos `new`, podés delegarlo a un framework como Spring:

```java
@Service
class EmailService implements NotificationService { ... }

@Service
class OrderService {
    public OrderService(NotificationService notificador) { ... }
}
```

Spring crea los objetos, ve que `OrderService` necesita un `NotificationService` y le pasa `EmailService`. Por eso la tabla dice que "otro decide cuándo y cómo se crean las cosas".

**Analogía: comer en un restaurante**

- **Sin IoC:** cocinás en tu casa, así que elegís los ingredientes y hacés todo vos.
- **IoC:** vas a un restaurante y le cedés el control de la cocina.
- **DI:** el plato llega a tu mesa, sin que tengas que prepararlo.

**Por qué no toda IoC usa DI**

También hay IoC cuando un framework decide cuándo ejecutar tu código, sin inyectarte ninguna dependencia:

```java
boton.addActionListener(e -> guardar());
```

No llamás a `guardar()` directamente en ese momento: el sistema lo hace cuando alguien aprieta el botón. Es IoC porque otro controla cuándo se ejecuta, pero no es DI porque no le entrega ninguna dependencia a tu clase.

Por eso, **toda DI aplica IoC, pero no toda IoC usa DI**.
[Timestamp: 2026/11/06 16:58:45]

**user**: digamos que DI es por ejemplo Vehiculo auto = new Vehiculo(new Auto) esto seria un DI por que inyecta una dependencia desde fuera
[Timestamp: 2026/11/06 17:06:42]

**ai**: **Sí, la idea es correcta:** es DI porque el objeto se crea afuera y se le pasa a `Vehiculo`, en lugar de que `Vehiculo` lo cree por dentro. Faltan los paréntesis: `new Auto()`.

Lo único raro es el ejemplo, porque un auto normalmente **es un** vehículo, así que sería herencia (`Auto : Vehiculo`) y no una dependencia. Una dependencia es algo que la clase **necesita para funcionar**, como un motor. Por eso queda más claro con el ejemplo de `Car` de tu nota:

```csharp
class Car {
    private IEngine engine;

    public Car(IEngine engine) {   // recibe la dependencia
        this.engine = engine;
    }
}

Car auto = new Car(new GasEngine());       // se inyecta desde afuera
Car autoElectrico = new Car(new ElectricEngine());
```

`GasEngine` y `ElectricEngine` son clases de ejemplo que implementan `IEngine`. Así, podés cambiar el motor sin modificar `Car`.

En cambio, esto **no** es DI, porque la clase crea su propia dependencia:

```csharp
class Car {
    private IEngine engine = new GasEngine();
}
```
[Timestamp: 2026/11/06 17:06:42]

**user**: No me queda claro el IoC
[Timestamp: 2026/11/06 17:07:36]

**ai**: **IoC significa que tu código deja de dirigir una parte del programa y otro, como un framework, decide cuándo ejecutarla.** La idea se resume en una frase conocida: *"no nos llames, nosotros te llamamos"*.

La pregunta para reconocerlo es: **¿quién decide cuándo se ejecuta esto?**

**Sin IoC: tu código dirige**

```java
String nombre = leerNombre();   // 1. tu código pide el dato
guardar(nombre);                // 2. tu código decide guardarlo
mostrarMensaje();               // 3. tu código decide mostrar el mensaje
```

Vos escribís el orden, y cada paso se ejecuta porque tu código lo llama.

**Con IoC: otro dirige**

```java
boton.addActionListener(e -> guardar());
```

Acá solo indicás qué hacer si aprietan el botón. Tu código no llama a `guardar()` en ese momento: el sistema de la ventana espera el clic y lo ejecuta cuando ocurre. **Se invirtió el control**, porque ahora el sistema llama a tu código.

**Otro ejemplo: una API web con Spring**

```java
@GetMapping("/pedidos")
public List<Pedido> listarPedidos() { ... }
```

Nunca escribís una llamada a `listarPedidos()`. Spring recibe la petición y llama al método cuando alguien entra a `/pedidos`.

**¿Y qué tiene que ver con crear objetos?**

Es el mismo cambio, aplicado a otra decisión:

| ¿Quién decide...? | Sin IoC | Con IoC |
| --- | --- | --- |
| **Cuándo se ejecuta un método** | Tu código lo llama | El framework lo llama |
| **Cómo se crean los objetos** | Tu código hace `new` | El contenedor los crea |

Por eso tu tabla dice que un contenedor "crea y gestiona los objetos": es uno de los casos de IoC.

**Dónde entra DI:** cuando el contenedor crea `OrderService` y le pasa el `NotificationService`, eso es DI. El botón, en cambio, es IoC sin DI, porque el sistema decide cuándo ejecutar `guardar()`, pero no le entrega una dependencia a tu clase.
[Timestamp: 2026/11/06 17:07:36]

**user**: Explicame el patron strategy
[Timestamp: 2026/11/06 17:13:24]

**ai**: **Strategy** es un patrón de comportamiento que **separa varias formas de hacer una misma tarea en clases intercambiables**. Así, el objeto que realiza la tarea puede usar una u otra sin cambiar su código.

**El problema**

Supongamos que un pedido se puede cobrar de varias formas:

```java
class Pedido {
    void cobrar(String medio, double monto) {
        if (medio.equals("tarjeta")) {
            // cobrar con tarjeta
        } else if (medio.equals("transferencia")) {
            // cobrar por transferencia
        }
    }
}
```

Cada medio de pago nuevo obliga a modificar `Pedido`, lo que **viola OCP**. Además, `Pedido` termina conociendo los detalles de cada cobro.

**La solución**

Cada forma de cobrar pasa a ser una clase que implementa la misma interfaz:

```java
interface MedioPago {                                 // Strategy
    void cobrar(double monto);
}

class PagoTarjeta implements MedioPago {              // ConcreteStrategy
    public void cobrar(double monto) { /* tarjeta */ }
}

class PagoTransferencia implements MedioPago {        // ConcreteStrategy
    public void cobrar(double monto) { /* transferencia */ }
}

class Pedido {                                        // Context
    private MedioPago medioPago;

    public Pedido(MedioPago medioPago) {
        this.medioPago = medioPago;
    }

    public void pagar(double monto) {
        medioPago.cobrar(monto);   // delega, sin preguntar cuál es
    }
}
```

Se usa así:

```java
Pedido pedido = new Pedido(new PagoTarjeta());
pedido.pagar(1000);
```

Para agregar un medio de pago, por ejemplo `PagoQR`, creás una clase nueva y `Pedido` no cambia.

**Participantes**

| Participante | Qué hace | En el ejemplo |
| --- | --- | --- |
| **Context** | Usa una estrategia y le delega la tarea | `Pedido` |
| **Strategy** | Define la interfaz común | `MedioPago` |
| **ConcreteStrategy** | Implementa una variante | `PagoTarjeta`, `PagoTransferencia` |

**Cuándo usarlo**

- Hay varias formas de resolver una misma tarea.
- Querés elegir o cambiar esa forma según el caso, incluso mientras corre el programa.
- Tenés un `if/else` o `switch` que selecciona una variante del algoritmo.

**Relación con lo que venías viendo**

- **OCP:** una variante nueva es una clase nueva.
- **SRP:** cada clase se ocupa de una sola forma de cobrar.
- **DIP y DI:** `Pedido` depende de una interfaz y la recibe desde afuera.

**No confundir con State**

Su estructura es muy parecida, pero cambia la intención:

| | Strategy | State |
| --- | --- | --- |
| **Qué representa** | **Cómo** se hace una tarea | **En qué estado** está el objeto |
| **Quién suele elegir la variante** | El cliente o quien configura el objeto | El contexto o los propios estados, durante las transiciones |
| **Ejemplo** | Cobrar con tarjeta o transferencia | Pedido pendiente, pagado o enviado |

**Para el parcial:** en tus resúmenes, Strategy aparece solo por nombre en el catálogo de patrones de comportamiento y en el mapa de relaciones, sin un desarrollo propio. Según lo que revisamos antes, las presentaciones tampoco lo desarrollan, así que esta explicación sale del patrón en general y no de tus apuntes. Conviene confirmar con la cátedra si lo toman con este nivel de detalle.
[Timestamp: 2026/11/06 17:13:24]

**user**: los PCC PRC PER que soin
[Timestamp: 2026/11/06 17:18:58]

**ai**: **PER, PCC y PRC** son principios de cohesión para decidir **qué clases conviene poner juntas en un mismo paquete o componente**. Según tus notas, son los criterios de organización de componentes de la Unidad 4.

| Sigla | Nombre | Idea | Equivale a |
| --- | --- | --- | --- |
| **PER** | Equivalencia de reutilización/liberación | Lo que se reutiliza se **libera junto** | — |
| **PCC** | Cierre común | Lo que **cambia junto va junto** | SRP a nivel de paquete |
| **PRC** | Reutilización común | Lo que **no se usa junto no va junto** | ISP a nivel de paquete |

**PER: Principio de Equivalencia de Reutilización/Liberación**

La unidad que se reutiliza tiene que ser la misma que se publica y versiona. Si usás una librería de pagos, recibís versiones como la 1.0 o 1.1 del paquete completo, sin tener que seguir cada clase por separado.

**PCC: Principio de Cierre Común**

Las clases que cambian por las mismas causas deberían estar en el mismo paquete, para que un cambio afecte a un solo paquete. Por ejemplo, si cambia una regla de facturación y hay que tocar `Factura` y `CalculadoraImpuestos`, conviene que estén juntas en `facturacion`.

**PRC: Principio de Reutilización Común**

Si usás una clase del paquete, deberías necesitar también las demás. Si no, dependés de código que no usás y te pueden afectar sus cambios. Por ejemplo, si un paquete tiene `GuardarHabitacion` y `GestionarUsuario`, y quien usa una nunca necesita la otra, viola PRC y conviene separarlas.

**Para recordarlos**

- **PER:** se **libera** junto.
- **PCC:** **cambia** junto.
- **PRC:** se **usa** junto.

**Dónde están en tus notas:** [[U4.2 - Componentes y Despliegue]] y [[Resumen Clases]], sección 13. Tu simulador también tiene preguntas sobre esto, y suele darte la frase o un caso para que identifiques el principio.
[Timestamp: 2026/11/06 17:18:58]

**user**: explicame factory
[Timestamp: 2026/11/06 17:29:16]

**ai**: **Factory** suele referirse a **Factory Method**, un patrón creacional que **delega en las subclases la decisión de qué objeto concreto crear**. Así, el código principal trabaja con una interfaz y no depende de los `new` de cada clase concreta.

**El problema**

```java
class ServicioAvisos {
    void avisar(String tipo, String mensaje) {
        Notificacion n;
        if (tipo.equals("email")) {
            n = new Email();
        } else {
            n = new Sms();
        }
        n.enviar(mensaje);
    }
}
```

Cada tipo nuevo obliga a modificar este método, lo que **viola OCP**. Además, `ServicioAvisos` queda acoplado a las clases concretas.

**La solución**

```java
interface Notificacion {                              // Product
    void enviar(String mensaje);
}

class Email implements Notificacion {                 // ConcreteProduct
    public void enviar(String mensaje) { /* email */ }
}

class Sms implements Notificacion {                   // ConcreteProduct
    public void enviar(String mensaje) { /* SMS */ }
}

abstract class ServicioAvisos {                       // Creator
    abstract Notificacion crearNotificacion();        // factory method

    void avisar(String mensaje) {
        Notificacion n = crearNotificacion();
        n.enviar(mensaje);
    }
}

class ServicioEmail extends ServicioAvisos {          // ConcreteCreator
    Notificacion crearNotificacion() { return new Email(); }
}

class ServicioSms extends ServicioAvisos {            // ConcreteCreator
    Notificacion crearNotificacion() { return new Sms(); }
}
```

Se usa así:

```java
ServicioAvisos servicio = new ServicioEmail();
servicio.avisar("Tu pedido fue enviado");
```

`avisar()` no sabe si está usando un email o un SMS. Para sumar WhatsApp, creás `Whatsapp` y `ServicioWhatsapp`, sin modificar `ServicioAvisos`.

**Participantes**

| Participante | Qué hace | En el ejemplo |
| --- | --- | --- |
| **Product** | Define la interfaz de lo que se crea | `Notificacion` |
| **ConcreteProduct** | Es el objeto concreto que se crea | `Email`, `Sms` |
| **Creator** | Declara el factory method y usa el producto | `ServicioAvisos` |
| **ConcreteCreator** | Decide qué producto crear | `ServicioEmail`, `ServicioSms` |

**Cuándo usarlo**

- Una clase necesita crear objetos, pero no debería depender de cuál es la clase concreta.
- Querés que las subclases decidan qué objeto crear.
- Esperás sumar nuevos tipos de productos.

**Variantes que se suelen confundir**

| | Qué hace | Ejemplo |
| --- | --- | --- |
| **Simple Factory** | Una clase centraliza el `if/switch` que crea los objetos. No es un patrón del catálogo GoF | `NotificacionFactory.crear("email")` |
| **Factory Method** | Una subclase decide qué **producto** crear | `ServicioEmail` crea un `Email` |
| **Abstract Factory** | Crea **familias** de objetos relacionados | Una fábrica de botones y ventanas para Windows, y otra para Mac |

**Relación con lo que venías viendo**

- **OCP:** un tipo nuevo se agrega con clases nuevas.
- **SRP:** la creación del objeto queda separada de su uso.
- **DIP:** `avisar()` depende de la interfaz `Notificacion`, no de `Email` ni de `Sms`.

**Para el parcial:** según lo que revisamos antes, las presentaciones nombran Factory Method y Abstract Factory, pero no los desarrollan. Esta explicación sale del patrón en general y no de tus apuntes.
[Timestamp: 2026/11/06 17:29:16]

**user**: En la arquitectura los componentes son los que vi en diagrama de componentes?
[Timestamp: 2026/11/06 18:11:28]

**ai**: **Sí, es la misma idea:** en ambos casos, un componente es una parte del sistema que cumple una función y se comunica con otras. Pero en arquitectura el término es **más amplio**: no se limita al elemento que dibujás en UML.

| | Diagrama de componentes | Arquitectura |
| --- | --- | --- |
| **Qué es** | Un diagrama UML que muestra el sistema | La organización general del sistema |
| **Componente** | Una pieza modelada con interfaces provistas y requeridas | Cualquier parte que realice una función del sistema |
| **Conexión** | Interfaces y dependencias | **Conectores**, que permiten la comunicación, coordinación y cooperación |

Por ejemplo, en una arquitectura cliente-servidor, los componentes son el **cliente**, el **servidor** y la **base de datos**, y un conector puede ser HTTP entre el cliente y el servidor.

El diagrama de componentes es una forma de mostrar esa organización. Podrías dibujar `Pedidos` y `Pagos` como componentes UML y usar una interfaz para indicar que `Pedidos` usa los servicios de `Pagos`.

**Para el parcial:** tu nota destaca que, a nivel arquitectónico, **no se especifican las propiedades internas de los componentes**. Se ve qué cajas hay y cómo se conectan, no cómo está hecha cada una.

Podés repasarlo en [[U5.5 - Arquitectura (V2)]] y en [[U4.2 - Componentes y Despliegue]].
[Timestamp: 2026/11/06 18:11:28]

**user**: La AD que es
[Timestamp: 2026/11/06 18:18:15]

**ai**: **AD** significa **Descripción Arquitectónica** (*Architectural Description*). Es el **conjunto de productos de trabajo**, como diagramas y documentos, que muestran la arquitectura del sistema desde **distintos puntos de vista**.

Se usan varias vistas porque no todos los participantes necesitan ver lo mismo. Cada vista atiende la **preocupación de un participante**. Por ejemplo, en un sistema de ventas podría ser así:

| Participante | Qué le preocupa | Qué vista le sirve |
| --- | --- | --- |
| **Usuario** | Qué puede hacer con el sistema | Casos de uso: comprar, pagar, consultar pedidos |
| **Desarrollador** | Cómo se organiza el código | Vista lógica: capas, paquetes y clases |
| **Infraestructura** | Dónde se ejecuta | Vista de despliegue: servidores, base de datos y protocolos |

Las tres vistas describen el mismo sistema, pero cada una muestra lo que le importa a un participante. Es como los planos de una casa: el arquitecto, el electricista y el plomero miran planos distintos de la misma construcción.

**Relación con el resto de la unidad:** tu nota dice que, en **UP**, la arquitectura se documenta en las vistas de **casos de uso**, **lógica** y **despliegue**, las mismas de la tabla.

**Sobre el nombre:** tu nota dice "descripción o vista arquitectónica (AD)". Para usar los términos con más precisión, la **descripción** es el conjunto completo y cada **vista** es una de sus partes.

**Para el parcial:** quedate con la definición de [[U5.5 - Arquitectura (V2)]]: es un conjunto de productos de trabajo que muestran distintos puntos de vista del sistema, y cada uno atiende la preocupación de un participante.
[Timestamp: 2026/11/06 18:18:15]

**user**: que es esto
[Timestamp: 2026/11/06 18:20:04]

**ai**: Son los **4 elementos que describen un estilo arquitectónico**. Un estilo, como cliente-servidor o capas, es una categoría de sistemas que comparten una forma de organizarse, y estos elementos explican cómo es esa forma.

**Ejemplo: una arquitectura en capas de un sistema de ventas**

| Elemento | Pregunta que responde | En el ejemplo |
| --- | --- | --- |
| **Componentes** | ¿Qué partes hay y qué función cumplen? | Presentación, Negocio, Persistencia y Base de datos |
| **Conectores** | ¿Cómo se comunican? | Llamadas a métodos entre capas y consultas SQL a la base de datos |
| **Restricciones** | ¿Qué reglas limitan cómo se integran? | Presentación no puede acceder directamente a Persistencia, sino que debe pasar por Negocio |
| **Modelos semánticos** | ¿Qué permite entender cómo se comporta el sistema en general? | Saber que un pedido pasa por las capas en orden permite razonar cómo afecta un cambio o dónde puede haber demoras |

**Una analogía: una empresa**

- **Componentes:** las áreas, como ventas, depósito y contabilidad.
- **Conectores:** los medios por los que se comunican, como el email o los formularios.
- **Restricciones:** las reglas, como que depósito no despacha sin una orden de ventas.
- **Modelos semánticos:** la comprensión del funcionamiento general, como saber cómo circula un pedido y dónde se puede trabar.

Los **modelos semánticos** suelen ser el elemento más abstracto. No son una pieza del sistema, sino lo que te permite razonar sobre sus propiedades generales sin analizar cada detalle.

**No lo confundas con las 4 dimensiones de la arquitectura:** estas son estructura, características, decisiones y principios, y describen la arquitectura de un sistema en general. Los 4 elementos de esta tabla describen un **estilo**, que corresponde a la dimensión de **estructura**.
[Timestamp: 2026/11/06 18:20:04]

**user**: los componentes describen una funcionalidad del sistema?
[Timestamp: 2026/11/06 18:25:51]

**ai**: **Casi:** los componentes no la describen, sino que la **realizan**. Cada uno es la parte del sistema que se encarga de una función.

Por ejemplo, en un sistema de ventas:

- **Pagos:** cobra los pedidos.
- **Inventario:** controla el stock.
- **Notificaciones:** envía los avisos a los clientes.
- **Base de datos:** guarda la información.

Lo que describe esa funcionalidad es otra cosa, como un diagrama, un caso de uso o la documentación de la arquitectura.

Además, la función no siempre es algo que el usuario ve. Por ejemplo, una base de datos no es una funcionalidad visible como "comprar", pero cumple la función de almacenar los datos.
[Timestamp: 2026/11/06 18:25:51]

**user**: Explicame las 4 dimensiones
[Timestamp: 2026/11/06 18:28:19]

**ai**: Las **4 dimensiones** son lo que hay que definir para describir la arquitectura de un sistema. Responden a preguntas distintas:

| Dimensión | Pregunta que responde | Ejemplo |
| --- | --- | --- |
| **Estructura** | ¿Qué estilo arquitectónico usa? | Capas o microservicios |
| **Características** | ¿Qué cualidades debe tener? | Escalabilidad o seguridad |
| **Decisiones** | ¿Qué reglas hay que cumplir? | Solo Negocio y Servicios pueden acceder a Persistencia |
| **Principios** | ¿Qué conviene hacer en general? | Preferir mensajería asíncrona entre servicios cuando sea posible |

**1. Estructura**

Es el estilo arquitectónico elegido, es decir, la forma general en que se organiza el sistema. Por ejemplo, un sistema de ventas puede organizarse en capas de presentación, negocio y persistencia.

**2. Características**

Son las cualidades que el sistema debe cumplir, las llamadas "-ilidades", como *availability* (disponibilidad), *scalability* (escalabilidad), *security* (seguridad) y *performance* (rendimiento). No dicen qué funciones tiene el sistema, sino **qué tan bien** tiene que funcionar. Por ejemplo, la tienda debería seguir funcionando con muchos usuarios durante una oferta.

**3. Decisiones**

Son **reglas obligatorias** para construir el sistema. Por ejemplo, tu nota menciona que *"solo las capas de negocio y de servicios pueden acceder a persistencia"*. Si una clase de presentación consulta directamente la base de datos, incumple esa regla.

**4. Principios**

Son **guías no obligatorias** que orientan al equipo. Por ejemplo, *"preferir, cuando sea posible, mensajería asíncrona entre servicios para mejorar el rendimiento"*. Si en un caso conviene otra opción, se puede usar.

**La diferencia que suelen tomar**

La clave para distinguir **decisión** y **principio** es si admite excepciones habituales:

- **Decisión:** es una regla que se debe cumplir. Suele aparecer con palabras como "solo", "debe" o "no puede".
- **Principio:** es una recomendación. Suele aparecer con palabras como "preferir", "cuando sea posible" o "se recomienda".

Tu simulador tiene preguntas justamente sobre esta diferencia. Podés repasarlo en [[U5.5 - Arquitectura (V2)]], sección "Las 4 dimensiones".
[Timestamp: 2026/11/06 18:28:19]

**user**: **Características** (las del diagrama): que significa del diagrama
[Timestamp: 2026/11/06 18:34:56]

**ai**: Significa que esas características son **las que aparecen en un diagrama de las 4 dimensiones**. Es decir, ese texto aclara de dónde sale la lista: no son todas las características posibles.

En tu nota, el diagrama más cercano es el que está justo arriba, ![[U5v2 - Dimensiones arquitectura.png]]. Pero ese diagrama muestra solo cinco: disponibilidad, escalabilidad, seguridad, rendimiento y elasticidad, seguidas de "...". La nota, en cambio, lista doce en inglés, así que probablemente se refiere al diagrama de la diapositiva de la cátedra, aunque no revisé el PDF para confirmarlo.

Si querés que se entienda mejor, podrías reemplazar "(las del diagrama)" por "(las del diagrama de la cátedra)" una vez que lo confirmes en la diapositiva.
[Timestamp: 2026/11/06 18:34:56]

**user**: que es particion tecnica vs por dominio
[Timestamp: 2026/11/06 18:38:56]

**ai**: Son dos formas de **dividir un sistema en partes**. La **técnica** divide según el **tipo de trabajo que hace el código**, y la de **dominio**, según el **área del negocio**.

**Ejemplo: una tienda online**

Partición técnica:

```text
Presentación  → pantallas de catálogo, carrito y envíos
Negocio       → reglas de catálogo, carrito y envíos
Persistencia  → acceso a datos de catálogo, carrito y envíos
```

Partición por dominio:

```text
Catálogo → sus pantallas, reglas y acceso a datos
Carrito  → sus pantallas, reglas y acceso a datos
Envíos   → sus pantallas, reglas y acceso a datos
```

Las dos tienen el mismo código, pero agrupado de otra manera.

| | **Técnica** | **Por dominio** |
| --- | --- | --- |
| **Se divide por** | Tipo de código | Área de negocio |
| **Partes típicas** | Presentación, negocio, persistencia | Catálogo, carrito, envíos |
| **Estilos típicos** | Capas, MVC | Microservicios, servicios |

**¿Qué cambia en la práctica?**

Supongamos que hay que agregar el "envío exprés", con una opción nueva en la pantalla, su regla de costo y un dato nuevo para guardar:

- **Con partición técnica:** el cambio atraviesa las 3 capas, porque hay que tocar presentación, negocio y persistencia.
- **Con partición por dominio:** el cambio suele quedar dentro de `Envíos`, aunque ese módulo tenga internamente esas mismas tres partes.

**Una analogía:** en un supermercado, la partición técnica sería organizar al personal por tarea: reponedores, cajeros y limpieza. La partición por dominio sería por sector: carnes, verdulería y bebidas, cada uno con su gente para todas las tareas.

**Para el parcial**

- **Para identificarla:** si las partes se llaman Presentación o Persistencia, es **técnica**. Si se llaman Pedidos o Envíos, es **por dominio**.
- **Dato de tu nota:** la fila "un cambio de negocio…" está marcada como *(extra)*, así que no sale del apunte de la cátedra.

Podés repasarlo en [[U5.5 - Arquitectura (V2)]], sección 3.
[Timestamp: 2026/11/06 18:38:56]

**user**: Cambiame ese cuadrito del resumen por otro mas facil de entender o que explique mejor
[Timestamp: 2026/11/06 18:44:09]

**ai**: Listo, cambié el cuadro de la sección 3 de [[U5.5 - Arquitectura (V2)]]. Quedó así:

| | **Partición técnica** | **Partición por dominio** |
| --- | --- | --- |
| **Idea** *(extra)* | Agrupa el código según **qué tipo de trabajo hace** | Agrupa el código según **a qué área del negocio pertenece** |
| **Partes** | Presentación, Reglas de negocio, Servicio, Persistencia | CatalogCheckout, UpdateInventory, ShipToCustomer, Reporting… |
| **Estilos típicos** | Capas, MVC | Microservicios, servicios |
| **Si agregás "envío exprés"** *(extra)* | Tocás pantalla, reglas y persistencia: el cambio **atraviesa varias capas** | El cambio suele quedar dentro de **`ShipToCustomer`** |
| **Cómo reconocerla** *(extra)* | Las partes tienen **nombres técnicos** | Las partes tienen **nombres del negocio** |

- **Qué agregué:** la idea de cada partición, un ejemplo concreto en lugar de la fila general sobre los cambios de negocio y una forma rápida de reconocerlas. Todo eso está marcado como *(extra)*, porque no sale del apunte de la cátedra.
- **Qué se mantiene:** las partes y los estilos típicos del apunte.
- **Qué no toqué:** la frase "Formas de dividir un sistema en partes" que acababas de agregar arriba del cuadro.
[Timestamp: 2026/11/06 18:44:09]

**user**: El estilo arqutitectonico de la tecnica es Capas , MVC
[Timestamp: 2026/11/06 18:46:28]

**ai**: **Sí, según tu nota, Capas y MVC son los estilos típicos de la partición técnica.** Son dos estilos distintos que dividen el sistema por el tipo de trabajo:

- **Capas:** presentación, negocio y persistencia.
- **MVC:** Modelo (datos y reglas), Vista (lo que se muestra) y Controlador (recibe las acciones y coordina).

Decimos "típicos" porque la partición no es un estilo en sí, sino el criterio para dividir el sistema. Estos estilos suelen seguir ese criterio, pero también se pueden combinar: por ejemplo, un sistema puede dividirse primero por dominio, como Pedidos y Envíos, y usar capas dentro de cada módulo.
[Timestamp: 2026/11/06 18:46:28]

**user**: Y monolitico vs distribuidos que son
[Timestamp: 2026/11/06 18:48:56]

**ai**: **Monolítico** y **distribuido** indican si el sistema se despliega como **una sola unidad** o como **varias partes independientes** que se comunican por red.

| | **Monolítico** | **Distribuido** |
| --- | --- | --- |
| **Despliegue** | Una sola unidad | Muchos servicios independientes |
| **Comunicación** | Interna, en memoria | Por red: API/REST, gRPC o mensajería |
| **Base de datos** | Generalmente una | Puede ser una por servicio |
| **A favor** *(extra)* | Simple, barato y fácil de probar | Escala por partes y permite equipos independientes |
| **En contra** *(extra)* | Escala "todo o nada" | Es complejo: red, latencia y consistencia |

**Ejemplo: una tienda online**

- **Monolítico:** Catálogo, Pagos y Envíos forman parte de una misma aplicación. Si cambiás algo en Pagos, volvés a desplegar toda la aplicación. Para cobrar, Catálogo o Carrito simplemente llama a un método de Pagos.
- **Distribuido:** Catálogo, Pagos y Envíos son servicios separados. Podés desplegar Pagos sin tocar los demás, pero para usarlo hay que enviarle una petición por la red, que puede demorarse o fallar.

**Qué significa "escala todo o nada"**

Si en una oferta se satura Pagos:

- **Monolítico:** tenés que replicar toda la aplicación, aunque solo Pagos necesite más capacidad.
- **Distribuido:** podés agregar más instancias solo de Pagos.

**Para no confundirlo**

- **No es lo mismo que la partición:** la partición dice cómo se divide el código, y esta elección dice cómo se despliega. Por ejemplo, un monolito puede estar organizado en capas o por dominio.
- **Tener varias capas no lo hace distribuido:** si esas capas se despliegan como una sola aplicación, sigue siendo monolítico.

**Para el parcial:** tu nota plantea esta como la primera gran elección de arquitectura. Si elegís distribuido, hay que tener en cuenta las **8 falacias**, como suponer que la red siempre es confiable. Podés repasarlo en [[U5.5 - Arquitectura (V2)]], sección 4.
[Timestamp: 2026/11/06 18:48:56]

**user**: pero que son arquitecturas?
[Timestamp: 2026/11/06 18:49:34]

**ai**: **Sí, son tipos de arquitectura.** Más precisamente, **monolítico** y **distribuido** son dos grandes categorías, y dentro de cada una hay **estilos arquitectónicos** concretos.

Según tu nota, se organizan así:

```text
Arquitectura
├── Monolítica
│   ├── Centrada en los datos
│   ├── En capas
│   ├── MVC
│   ├── Flujo de datos
│   └── Microkernel
└── Distribuida
    ├── Basada en servicios
    ├── Solicitud-respuesta
    ├── Eventos (Broker o Mediador)
    └── Microservicios
```

Por ejemplo, podés describir un sistema como "una arquitectura **monolítica** con estilo **en capas**":

- **Monolítica** indica que se despliega como una sola unidad.
- **En capas** indica cómo se organiza por dentro.

Y qué es la **arquitectura** en general: según tu nota, es la **estructura de organización de los componentes**, cómo **interactúan** y qué **datos** usan. Es como el plano general del sistema, antes de entrar en el detalle de cada parte.

**Para el parcial:** si te preguntan por un estilo, primero podés ubicar su categoría y después explicarlo. Por ejemplo: "Microservicios es un estilo **distribuido**, con muchos servicios chicos y cada uno con su propia base de datos".

Podés repasar esta clasificación en [[U5.5 - Arquitectura (V2)]], sección 5.
[Timestamp: 2026/11/06 18:49:34]

**user**: Una tienda online es una arquitectura distribuida
[Timestamp: 2026/11/06 18:54:03]

**ai**: **No necesariamente.** Una tienda online es un **tipo de sistema**, y la arquitectura es **cómo decidís construirlo**. Por eso, la misma tienda puede ser monolítica o distribuida:

| | Tienda monolítica | Tienda distribuida |
| --- | --- | --- |
| **Cómo se construye** | Catálogo, Pagos y Envíos están en una sola aplicación | Catálogo, Pagos y Envíos son servicios separados |
| **Cómo se comunican** | Con llamadas internas | Por la red |
| **Cómo se despliega** | Toda junta | Cada servicio por separado |
| **Cuándo puede convenir** | Una tienda chica con poco tráfico | Una tienda grande que necesita escalar partes por separado |

El hecho de que los clientes entren por Internet tampoco la hace distribuida en el sentido de esta clasificación. Una tienda monolítica también se usa desde el navegador, y lo que mira esta clasificación es si **el sistema mismo** está dividido en servicios independientes.

**Para el parcial:** si te dan un caso, no te fijes solo en de qué sistema se trata, sino en cómo está construido. Por ejemplo, si dice "una sola aplicación desplegada en un servidor", es monolítico, y si dice "servicios independientes que se comunican por API", es distribuido.
[Timestamp: 2026/11/06 18:54:03]

**user**: cual es el beneficio de escala por partes
[Timestamp: 2026/11/06 18:58:00]

**ai**: El beneficio es que **agregás capacidad solo a la parte que la necesita**, sin tener que replicar todo el sistema. Así usás mejor los recursos y normalmente gastás menos.

**Ejemplo: una tienda durante una oferta**

Supongamos que `Pagos` se satura, pero `Catálogo` y `Envíos` están funcionando bien:

| | Qué tenés que hacer | Resultado |
| --- | --- | --- |
| **Monolítico** | Levantar otra copia de **toda** la aplicación | También replicás `Catálogo` y `Envíos`, aunque no lo necesiten |
| **Distribuido** | Levantar más instancias solo de `Pagos` | Solo sumás capacidad donde hay demanda |

**Qué ganás**

- **Menos costo:** no pagás servidores para las partes que no lo necesitan.
- **Mejor rendimiento donde hace falta:** reforzás el servicio que causa el cuello de botella.
- **Una respuesta más flexible:** después de la oferta, podés reducir solo las instancias de `Pagos`.

**Una analogía:** si un supermercado tiene mucha fila en las cajas, abre más cajas, pero no duplica también la verdulería, la carnicería y el depósito.

**Una limitación:** esto solo ayuda si el servicio saturado es realmente el problema. Si varias instancias de `Pagos` comparten una misma base de datos y esa base es el cuello de botella, agregar más instancias no alcanza.
[Timestamp: 2026/11/06 18:58:00]

**user**: Levantar instancias significa dar mayor acceso simultaneo apagos?
[Timestamp: 2026/11/06 18:58:57]

**ai**: **Sí, ese es el efecto:** levantar más instancias permite que `Pagos` atienda **más solicitudes al mismo tiempo**. Pero el término se refiere a cómo se logra: **poner en marcha más copias del mismo servicio**.

```text
                        ┌→ Pagos (copia 1)
Clientes → Balanceador ─┼→ Pagos (copia 2)
                        └→ Pagos (copia 3)
```

El **balanceador de carga** reparte las solicitudes entre las copias. Si cada copia pudiera atender 100 pagos por segundo, las tres podrían atender cerca de 300, siempre que nada más limite el sistema, como la base de datos.

En la analogía del supermercado, cada instancia es una caja más abierta: los clientes se reparten y se atiende a más personas a la vez.

Esto es **escalar horizontalmente**, porque agregás más copias en lugar de hacer más grande una sola máquina, que sería escalar verticalmente.

Además, no se trata de dar más permisos: "acceso" acá significa capacidad para atender solicitudes, no autorización para entrar a `Pagos`.
[Timestamp: 2026/11/06 18:58:57]

**user**: en las falencias la red es confiable y la red segura no son lo mismo?
[Timestamp: 2026/11/06 19:00:53]

**ai**: **No son lo mismo.** La primera habla de **fallas** y la segunda, de **ataques**:

| Falacia | Qué se supone erróneamente | Qué puede pasar | Cómo se suele manejar |
| --- | --- | --- | --- |
| **"La red es confiable"** | Todo mensaje llega y recibe respuesta | Se corta la conexión o se pierde un mensaje | Tiempos de espera, reintentos y colas |
| **"La red es segura"** | Nadie puede espiar ni alterar lo que viaja | Alguien intercepta datos, los modifica o se hace pasar por otro | HTTPS/TLS, autenticación y autorización |

**Ejemplo con `Pedidos` y `Pagos`**

- **Falla de confiabilidad:** `Pedidos` le pide a `Pagos` que cobre, pero la conexión se corta y no llega ninguna respuesta. `Pedidos` no sabe si el cobro se hizo, así que reintentar sin cuidado podría cobrar dos veces.
- **Falla de seguridad:** el mensaje llega bien, pero un atacante lo interceptó y leyó los datos de la tarjeta, o cambió el monto.

**Pueden fallar por separado**

- **Confiable, pero insegura:** los mensajes siempre llegan, pero viajan sin cifrar y alguien puede leerlos.
- **Segura, pero poco confiable:** los mensajes viajan cifrados, pero la conexión se corta seguido.

**Para distinguirlas:** preguntate si el problema es que **el mensaje no llegó** (confiabilidad) o si **alguien pudo leerlo o alterarlo** (seguridad).
[Timestamp: 2026/11/06 19:00:53]

**user**: que es topologia
[Timestamp: 2026/11/06 19:01:18]

**ai**: La **topología** de una red es **cómo están conectados entre sí los servidores, routers y demás equipos**, es decir, la forma o el mapa de la red.

Por ejemplo, el mismo sistema podría estar conectado de estas dos maneras:

```text
Topología 1: Cliente → Router → Servidor Pagos

Topología 2: Cliente → Router A → Router B → Balanceador → Servidor Pagos
```

En la segunda, los datos pasan por más equipos antes de llegar a `Pagos`.

**La falacia "la topología no cambia"**

Es la suposición falsa de que esa forma se mantiene siempre igual. En la práctica puede cambiar porque:
- se agrega o se reemplaza un servidor;
- se cae un router y el tráfico toma otro camino;
- el servicio se muda a otra red o a la nube.

**Por qué importa:** si `Pedidos` tiene escrita en el código la dirección fija de `Pagos`, como `192.168.1.20`, y `Pagos` se muda a otro servidor, `Pedidos` deja de encontrarlo. Para evitarlo, se puede usar un nombre, como `pagos.mitienda.com`, que siga funcionando aunque cambie la dirección.
[Timestamp: 2026/11/06 19:01:18]

**user**: Explicame cada una de las 8 falacias corto
[Timestamp: 2026/11/06 19:05:01]

**ai**: Las **8 falacias** son suposiciones falsas que se suelen hacer al diseñar sistemas distribuidos. Cada una tiene su realidad:

1. **"La red es confiable":** los mensajes se pueden perder y las conexiones se pueden cortar.
2. **"La latencia es cero":** cada mensaje tarda un tiempo en ir y volver, y muchas llamadas por red pueden hacer lento al sistema.
3. **"El ancho de banda es infinito":** la cantidad de datos que puede transmitir la red por segundo tiene un límite, así que enviar demasiados puede saturarla.
4. **"La red es segura":** alguien puede interceptar, leer o modificar lo que viaja por la red.
5. **"La topología no cambia":** se pueden agregar, mover o caer servidores y routers, y entonces cambian las rutas y las direcciones.
6. **"Existe un solo administrador":** suele haber varios equipos o empresas a cargo de distintas partes, cada uno con sus propias reglas.
7. **"El transporte no tiene costo":** mover datos cuesta dinero y recursos, como infraestructura y tiempo de procesamiento.
8. **"La red es homogénea":** conviven equipos, sistemas operativos y protocolos distintos, que tienen que poder entenderse.

**Dos que se suelen confundir:**

- **Latencia y ancho de banda:** la latencia es **cuánto tarda** en llegar un dato, y el ancho de banda es **cuántos datos** pasan por segundo. Es como una ruta: la latencia es cuánto tarda un auto en llegar, y el ancho de banda es cuántos autos pasan por segundo.
- **Latencia y costo de transporte:** tu nota aclara que no son lo mismo. Uno se mide en **tiempo** y el otro, en **recursos o dinero**. Un envío puede ser rápido y aun así caro.
[Timestamp: 2026/11/06 19:05:01]

**user**: Los estilos arquitectonicos no son monolitico y distruibuido sino que los distintos estilos que hay dentro de una arquitectura monolitica por ejemplo
[Timestamp: 2026/11/06 19:08:41]

**ai**: **Sí, exacto.** Según tu nota, **monolítico y distribuido son las dos categorías**, y los **estilos** son las opciones concretas dentro de cada una:

| Categoría | Estilos |
| --- | --- |
| **Monolítica** | Centrado en los datos, En capas, MVC, Flujo de datos, Microkernel |
| **Distribuida** | Basada en servicios, Solicitud-respuesta, Eventos (Broker o Mediador), Microservicios |

Por ejemplo, si un sistema se despliega como una sola aplicación, es **monolítico**. Pero todavía falta saber cómo se organiza por dentro, y ahí entra el **estilo**: podría ser en capas o MVC.

En la práctica, a veces se habla de "estilo monolítico" o "estilo distribuido" de forma más general. Para el parcial, conviene usar la clasificación de tu nota: "**En capas** es un estilo **monolítico**".
[Timestamp: 2026/11/06 19:08:41]

**user**: Los estilos arquitectonicos son solo estilos luego el codigo es el mismo
[Timestamp: 2026/11/06 19:10:01]

**ai**: **No.** El estilo no es solo una forma de describir el sistema: **cambia cómo se organiza y se comunica el código**. Lo que puede mantenerse parecido es la **lógica de negocio**, como la regla para calcular el total de un pedido.

**Ejemplo: `Pedidos` necesita cobrar con `Pagos`**

En un monolito en capas, es una llamada directa dentro de la misma aplicación:

```java
pagoService.cobrar(pedido);
```

Con microservicios, es una petición por la red a otro servicio:

```java
try {
    restClient.post()
        .uri("http://pagos/cobros")
        .body(pedido)
        .retrieve()
        .toBodilessEntity();
} catch (RestClientException e) {
    // manejar el error, reintentar o avisar
}
```

La intención es la misma, cobrar el pedido, pero el código es distinto. En el segundo caso, además, hay que manejar problemas de red que antes no existían.

**Qué suele cambiar y qué no**

| | ¿Cambia con el estilo? | Ejemplo |
| --- | --- | --- |
| **Reglas de negocio** | Poco o nada | Calcular el total o validar el stock |
| **Organización** | Sí | Una aplicación con capas o varios servicios |
| **Comunicación** | Sí | Llamadas a métodos, HTTP o eventos |
| **Datos** | Puede cambiar | Una base compartida o una por servicio |
| **Despliegue** | Puede cambiar | Una sola unidad o varios servicios |

Es como una receta: los ingredientes y los pasos pueden ser los mismos, pero no se organiza igual una cocina casera que un restaurante con varias estaciones.

**Una corrección:** cuando expliqué la partición técnica y por dominio, dije que "las dos tienen el mismo código, pero agrupado de otra manera". Eso fue una simplificación: la funcionalidad puede ser la misma, pero el código también puede cambiar según la organización que elijas.
[Timestamp: 2026/11/06 19:10:01]

**user**: Que seria la persistencia
[Timestamp: 2026/11/06 19:13:29]

**ai**: La **persistencia** es **guardar los datos para que sigan existiendo aunque el programa se cierre o se apague el servidor**.

Por ejemplo, si un pedido queda solo en la memoria del programa, se pierde al reiniciarlo. Si se guarda en una base de datos, sigue disponible:

```java
Pedido pedido = new Pedido();     // solo existe en memoria
pedidoDAO.guardar(pedido);        // queda guardado en la base de datos
```

**La capa de persistencia** es la parte del sistema encargada de guardar y recuperar esos datos. Por ejemplo, en una arquitectura en capas:

- **Presentación:** muestra la pantalla del pedido.
- **Negocio:** aplica las reglas, como verificar si hay stock.
- **Persistencia:** guarda y consulta los pedidos.
- **Base de datos:** es donde quedan almacenados los datos.

La **persistencia no es lo mismo que la base de datos**. La capa de persistencia es el código que accede a los datos, como el **DAO** que viste en la Unidad 5, y la base de datos es donde se almacenan. Además, también se puede persistir en otros lugares, como un archivo.
[Timestamp: 2026/11/06 19:13:29]

**user**: En MVC que seria modelo
[Timestamp: 2026/11/06 19:15:45]

**ai**: En MVC, el **Modelo** es la parte que contiene **los datos y las reglas del negocio**. Según tu nota, tiene la **funcionalidad, el contenido y los estados** del sistema, y además **accede a los datos**. No sabe cómo se muestra la información al usuario.

**Ejemplo: confirmar un pedido**

```java
class Pedido {                         // Modelo
    private double total;
    private String estado = "PENDIENTE";

    public void confirmar() {          // regla de negocio
        if (total <= 0) {
            throw new IllegalStateException("El pedido no tiene un total válido");
        }
        estado = "CONFIRMADO";
    }
}
```

`Pedido` guarda el total y el estado, y sabe cuándo se puede confirmar. Las tres partes trabajan así:

1. **Vista:** muestra la pantalla, y el usuario aprieta "Confirmar".
2. **Controlador:** recibe esa acción y le pide al Modelo que confirme el pedido.
3. **Modelo:** aplica la regla, cambia el estado y puede guardarlo mediante un DAO.
4. **Vista:** muestra el resultado, como "Pedido confirmado".

**Para ubicar cada cosa**

| Si se trata de... | Va en... |
| --- | --- |
| Calcular el total o validar una regla del negocio | **Modelo** |
| Mostrar un botón o una tabla | **Vista** |
| Recibir el clic y decidir qué hacer | **Controlador** |

**No lo confundas:** el Modelo no es solo la base de datos ni una clase con datos. También incluye la lógica del negocio. Por eso, tu nota lo relaciona con la **entidad**, aunque el Modelo puede abarcar más que una sola clase, como servicios y DAO.
[Timestamp: 2026/11/06 19:15:45]

**user**: y el estilo arquitectonico de flujo de datos donde se usa
[Timestamp: 2026/11/06 19:17:41]

**ai**: El estilo de **flujo de datos** se usa cuando hay que **procesar datos en una serie de pasos**, donde cada uno recibe la salida del anterior:

```text
Entrada → [Filtro 1] → [Filtro 2] → [Filtro 3] → Salida
```

**Usos comunes**

- **Compiladores:** el código fuente pasa por análisis léxico, análisis sintáctico, optimización y generación de código.
- **Procesos ETL:** extraen datos, los transforman y los cargan en otra base, como un sistema de reportes.
- **Procesamiento de logs:** limpian los registros, filtran los errores, los pasan a JSON y arman un reporte. Este es el ejemplo de tu simulador.
- **Procesamiento de imagen, audio o video:** una foto puede pasar por pasos como recortar, aplicar un filtro y comprimir.
- **Comandos de Linux:** cada programa recibe la salida del anterior, como en este caso:

```bash
cat ventas.log | grep "ERROR" | sort | uniq
```

**Cuándo conviene**

Conviene cuando el trabajo tiene **pasos claros y en secuencia**, con una entrada y una salida definidas. Además, podés cambiar o reutilizar un filtro sin rehacer todo el proceso.

**Cuándo no conviene**

Como dice tu nota, no sirve para **sistemas interactivos**. Una tienda online, por ejemplo, tiene que responder a cada acción del usuario y no sigue siempre el mismo recorrido de principio a fin.

**Para el parcial:** si un caso dice que "cada paso solo recibe la salida del anterior", o menciona **filtros** y **tubos**, es flujo de datos. Los usos de esta lista, salvo el de logs, son ejemplos generales y no salen del apunte de la cátedra.
[Timestamp: 2026/11/06 19:17:41]

**user**: que hace esto cat ventas.log | grep "ERROR" | sort | uniq
[Timestamp: 2026/11/06 19:18:11]

**ai**: Ese comando **busca los errores en `ventas.log`, los ordena y quita las líneas repetidas**. Cada `|` (tubo o *pipe*) envía la salida de un comando como entrada del siguiente:

| Parte | Qué hace |
| --- | --- |
| `cat ventas.log` | Lee el archivo y pasa todas sus líneas |
| `grep "ERROR"` | Deja solo las líneas que contienen `ERROR` |
| `sort` | Las ordena alfabéticamente |
| `uniq` | Quita las repetidas que quedaron juntas |

**Ejemplo**

Si `ventas.log` contiene:

```text
INFO Venta realizada
ERROR Sin stock
INFO Cliente registrado
ERROR Pago rechazado
ERROR Sin stock
```

El resultado es:

```text
ERROR Pago rechazado
ERROR Sin stock
```

`uniq` solo detecta repetidas si están una al lado de la otra, por eso va después de `sort`.

**Relación con flujo de datos:** cada comando (`grep`, `sort`, `uniq`) es un **filtro** y cada `|` es un **tubo**.
[Timestamp: 2026/11/06 19:18:11]

**user**: y microkernel seria como obsidian por ejemplo que tiene un nucleo minimo y despues esta lleno de plugins
[Timestamp: 2026/11/06 19:20:10]

**ai**: **Sí, Obsidian es un muy buen ejemplo.** Tiene un **núcleo** con lo básico, como manejar las notas y los enlaces, y los **plugins** le agregan funciones, como Copilot o Excalidraw.

| Microkernel | En Obsidian |
| --- | --- |
| **Core System** | La aplicación base, que maneja las notas y la interfaz |
| **Plug-ins** | Copilot, Excalidraw, Dataview y otros |
| **Contrato entre ambos** | La API de plugins, que define cómo pueden conectarse |

**Lo que lo hace microkernel:**

- **Se extiende sin tocar el núcleo:** instalar Excalidraw no requiere modificar el código de Obsidian. Por eso tu nota dice que es **OCP a nivel arquitectura**.
- **Los plugins son opcionales:** podés activarlos o desactivarlos, y la aplicación sigue funcionando.
- **Los plugins dependen del núcleo:** sin Obsidian, un plugin de Obsidian no funciona por sí solo.

Un detalle: el núcleo de Obsidian no es mínimo en sentido estricto, porque ya trae bastantes funciones y hasta sus propios *core plugins*. Pero la idea general es la misma.

Otros ejemplos parecidos son **VS Code** con sus extensiones y un **navegador** con sus complementos.
[Timestamp: 2026/11/06 19:20:10]

**user**: adobe por ejemplo tambien
[Timestamp: 2026/11/06 19:20:20]

**ai**: **Sí, en parte.** Depende de qué parte de Adobe estés mirando:

- **Una aplicación como Photoshop:** se parece a microkernel, porque tiene una aplicación base y se le pueden sumar plugins, por ejemplo, de filtros.
- **Toda la suite de Adobe:** no sería un ejemplo de microkernel, porque Photoshop, Illustrator y Acrobat son aplicaciones separadas, no plugins de un mismo núcleo.

Pero Photoshop es un ejemplo menos puro que Obsidian o VS Code: su núcleo está lejos de ser mínimo, porque trae la mayoría de sus funciones incorporadas, y los plugins solo suman extras. Para el parcial, VS Code u Obsidian muestran más claro la idea de núcleo más plugins.
[Timestamp: 2026/11/06 19:20:20]

**user**: Entonces significa que por ejemplo obsidian tiene un estilo arquitectonico de microkernel pero tambien se puede representar como en capas?
[Timestamp: 2026/11/06 19:21:10]

**ai**: **Sí, los estilos se pueden combinar**, porque pueden describir distintos niveles del sistema:

- **Microkernel** describe la organización general: un núcleo más plugins.
- **En capas** puede describir cómo está organizado ese núcleo por dentro.

Tu nota lo menciona: en microkernel, *"el núcleo puede estar en capas (partición técnica) o en módulos (por dominio)"*.

```text
┌───────────── Core System ─────────────┐
│ Presentación                          │
│ Negocio                               │  ← plugins conectados a la API
│ Persistencia                          │
└───────────────────────────────────────┘
```

Un plugin también podría tener sus propias capas por dentro, y eso no cambiaría que el sistema general sea microkernel.

**Sobre Obsidian:** es un ejemplo hipotético, porque su código no es abierto y no sé cómo está organizado su núcleo internamente. Lo que se ve desde afuera es la parte de microkernel: una aplicación base con plugins.

**Una precisión:** no es que puedas dibujar cualquier sistema en capas y listo. Para que sea en capas, el código tiene que estar organizado así de verdad, con cada capa cumpliendo su función y respetando las reglas de acceso.

**Para el parcial:** al clasificar un caso, fijate en lo que más lo caracteriza. Si habla de un núcleo con plugins, es **microkernel**, aunque ese núcleo tenga capas por dentro.
[Timestamp: 2026/11/06 19:21:10]

**user**: Los patrones arquitectonicos son esto de los estilos arquitectonicos para cada arquitectura?
[Timestamp: 2026/11/06 19:25:53]

**ai**: **Sí, en la práctica son casi lo mismo.** Tus notas de la Unidad 5 ponen **Capas** y **MVC** como ejemplos de patrones de arquitectura y también como estilos arquitectónicos.

Según [[U5.1 - Patrones de Diseño (V2)]], un **patrón de arquitectura** es *el esquema estructural fundamental de todo el sistema*. Eso coincide con la idea de elegir un estilo como capas o microkernel.

Algunos autores los distinguen, por ejemplo, usando **estilo** para la forma general de organizar el sistema y **patrón** para una solución más concreta a un problema recurrente. Pero esa distinción no es uniforme y no la vi desarrollada en tus notas.

**Solo una corrección sobre "para cada arquitectura":** los estilos no se crean para cada sistema en particular. Son **opciones generales y reutilizables**, y vos elegís una para tu sistema. Por ejemplo, tu tienda puede **usar** el estilo en capas, y otro sistema puede usar ese mismo estilo.

**No los confundas con los patrones de diseño:**

| | Qué abarca | Ejemplos |
| --- | --- | --- |
| **Patrón de arquitectura** | Todo el sistema | Capas, MVC, Microkernel |
| **Patrón de diseño** | Clases y objetos | State, Singleton, Facade |
[Timestamp: 2026/11/06 19:25:53]

**user**: Explicame los estlios arquitectonicos en los distruibuidos con ejemplo por que no los entiendo
[Timestamp: 2026/11/06 19:27:53]

**ai**: Los estilos distribuidos reparten el sistema en partes que se comunican por red. Se diferencian principalmente por **cuántos servicios hay, quién coordina y si comparten la base de datos**. Veámoslos con el mismo caso: **una tienda online donde alguien compra un libro**.

## 1. Basada en servicios

Hay una interfaz, **pocos servicios grandes** y **una base de datos compartida**.

```text
             ┌→ Ventas ────┐
Interfaz  ───┼→ Inventario ┼→ Base de datos compartida
             └→ Envíos ────┘
```

**En la compra:** la interfaz llama a `Ventas`, que registra el pedido en la base. `Inventario` y `Envíos` trabajan sobre esa misma base.

**Idea clave:** separa el sistema, pero sin llegar a tantas partes como los microservicios.

## 2. Solicitud-respuesta

Un **Request Orchestrator** recibe la solicitud y la reparte entre varios **Request Processors**, que comparten la base.

```text
                               ┌→ Processor de pagos ─┐
Solicitud → Request Orchestrator                      ├→ Base compartida
                               └→ Processor de stock ─┘
```

**En la compra:** el orquestador recibe "comprar libro" y le pide a un processor que cobre y a otro que descuente el stock. Con esos resultados, arma la respuesta para el cliente.

**Idea clave:** hay un coordinador que reparte el trabajo y **responde a la solicitud**.

## 3. Eventos con Broker

**No hay coordinador.** Cada procesador reacciona a un evento y, al terminar, publica otro.

```text
order-created → Pagos ─→ payment-applied → Envíos ─→ order-shipped
              → Inventario ─→ stock-updated
```

**En la compra:**
1. Se publica `order-created`.
2. `Pagos` e `Inventario` reaccionan a ese evento.
3. `Pagos` termina y publica `payment-applied`.
4. `Envíos` reacciona a ese evento y prepara el envío.

**Idea clave:** es como una cadena de avisos, donde nadie dirige el proceso completo.

## 4. Eventos con Mediador

Los procesadores también trabajan por eventos, pero un **Event Mediator** **dirige los pasos**.

```text
Evento → Cola → Event Mediator ─┬→ 1. Pagos
                                ├→ 2. Inventario
                                └→ 3. Envíos
```

**En la compra:** el mediador recibe `order-created` y ordena: primero cobrar, después actualizar el stock y luego preparar el envío.

**Idea clave:** es como un director de orquesta, que sabe el orden completo y puede controlar los errores.

## 5. Microservicios

Hay **muchos servicios chicos**, cada uno con **su propia base de datos**, detrás de una **API Layer**.

```text
             ┌→ Catálogo ──→ BD Catálogo
API Layer ───┼→ Pagos ─────→ BD Pagos
             ├→ Inventario → BD Inventario
             └→ Envíos ────→ BD Envíos
```

**En la compra:** la solicitud entra por la API Layer. `Pagos` guarda el cobro en su base, `Inventario` actualiza la suya, y `Envíos` hace lo mismo. Ningún servicio entra directamente en la base de otro.

**Idea clave:** cada servicio es muy independiente y se puede desplegar y escalar por separado.

## Cómo diferenciarlos

| Estilo | Servicios | Base de datos | Quién coordina |
| --- | --- | --- | --- |
| **Basada en servicios** | Pocos y grandes | Compartida | No es lo que lo define |
| **Solicitud-respuesta** | Processors | Compartida | Request Orchestrator |
| **Eventos con Broker** | Procesadores | No es lo que lo define | Nadie: reaccionan a eventos |
| **Eventos con Mediador** | Procesadores | No es lo que lo define | Event Mediator |
| **Microservicios** | Muchos y chicos | Una por servicio | No es lo que lo define |

**Para el parcial, fijate en las pistas:**

- "Pocos servicios grandes" y "BD compartida": **basada en servicios**.
- "Request Orchestrator" y "Request Processors": **solicitud-respuesta**.
- "Sin coordinador" y "publica un evento nuevo": **Broker**.
- "Event Mediator" que orquesta: **Mediador**.
- "Muchos servicios chicos" y "BD propia": **microservicios**.

Los pasos de cada compra son ejemplos míos, salvo la secuencia de eventos del Broker, que sale de tu nota. Podés repasarlos en [[U5.5 - Arquitectura (V2)]], sección 5.
[Timestamp: 2026/11/06 19:27:53]

**user**: que es la capa API proxy gateaway
[Timestamp: 2026/11/06 19:30:39]

**ai**: La **capa API** es **la puerta de entrada al sistema**. En lugar de llamar directamente a cada servicio, los clientes le envían las solicitudes a esta capa, y ella las dirige al servicio que corresponde.

```text
                    ┌→ Catálogo
Cliente → Capa API ─┼→ Pagos
                    └→ Envíos
```

Tu nota menciona dos formas de esta capa:

| | Qué hace | Ejemplo |
| --- | --- | --- |
| **Proxy** | Principalmente recibe la solicitud y la **reenvía** al servicio | `/pagos` va a `Pagos` |
| **Gateway** | Reenvía y además suma **funciones comunes** | Verifica el inicio de sesión, limita solicitudes y registra accesos antes de llamar a `Pagos` |

Es parecido a un edificio de oficinas:

- **Proxy:** una recepción que solo te indica a qué oficina ir.
- **Gateway:** una recepción que también te pide el documento, controla si podés entrar y registra tu visita.

**Por qué sirve**

- **Un solo punto de entrada:** el cliente no necesita conocer la dirección de cada servicio.
- **Menos repetición:** por ejemplo, el control de acceso puede estar en un solo lugar, en vez de repetirse en cada servicio.
- **Más libertad para cambiar:** podés mover o dividir un servicio interno sin cambiar el cliente.

**Una desventaja:** si esa capa se cae, los clientes pueden quedarse sin acceso a los servicios, y también puede convertirse en un cuello de botella. Por eso se suelen usar varias instancias.

La distinción entre proxy y gateway no siempre es tan estricta, porque un proxy también puede tener funciones extra. Lo que importa es que un **gateway** suele hacer más que reenviar. Estas funciones y ejemplos son generales y no salen de tu nota, que solo los menciona como una capa que se puede agregar.
[Timestamp: 2026/11/06 19:30:39]

**user**: En solicitud - Respuesta si un request processor quiere usar la base de datos al mismo moneto que otro por ejemplo inventario para actualizar y factura para guardar la factura como seria
[Timestamp: 2026/11/06 19:34:38]

**ai**: **Los dos pueden usar la base al mismo tiempo.** Cada Request Processor abre su propia conexión, y el **motor de la base de datos** se encarga de coordinar las operaciones simultáneas, así que los processors normalmente no tienen que turnarse entre ellos.

```text
Processor de Inventario ── UPDATE stock ───┐
                                           ├→ Base de datos
Processor de Facturación ── INSERT factura ┘
```

**Tu ejemplo: datos distintos**

`Inventario` modifica la tabla de stock y `Facturación` agrega una fila en la tabla de facturas. Como no tocan los mismos datos, normalmente **no hay conflicto** y las dos operaciones pueden avanzar a la vez.

**Si tocan el mismo dato**

Supongamos que dos compras quieren descontar el mismo libro y solo queda 1 unidad:

1. La primera operación **bloquea** esa fila y descuenta el stock.
2. La segunda **espera** a que termine la primera.
3. Cuando la segunda continúa, ve que el stock quedó en 0 y puede rechazar la compra.

Para eso, la actualización debe comprobar el stock en la misma operación:

```sql
UPDATE stock
SET cantidad = cantidad - 1
WHERE libro_id = 10 AND cantidad > 0;
```

Si la segunda operación no modifica ninguna fila, significa que no había stock.

**Si tienen que salir bien las dos**

El problema puede aparecer si se descuenta el stock pero falla la factura. La simultaneidad no resuelve eso. Para no dejar la venta a medias, hay dos opciones comunes:

- **Una sola transacción:** si una operación falla, se deshacen las dos. Para eso tienen que formar parte de la misma transacción, algo que es más simple si un solo componente la maneja.
- **Compensación:** si falla la factura, el orquestador pide devolver el stock.

**La desventaja de compartir la base:** si llegan muchas operaciones, la base puede convertirse en un **cuello de botella**. Por eso, agregar más processors no siempre mejora el rendimiento.
[Timestamp: 2026/11/06 19:34:38]

**user**: eventos - mediador no usa BD ?
[Timestamp: 2026/11/06 19:36:59]

**ai**: **Sí, puede usarla.** En el diagrama de [[U5.5 - Arquitectura (V2)]] no aparece una base de datos en **Eventos: Mediador**, pero eso no significa que el estilo no use una. El diagrama muestra lo que lo caracteriza: **cómo circulan los eventos y quién coordina**.

Lo mismo pasa con **Eventos: Broker**, que tampoco dibuja una base de datos.

**Ejemplo: compra de un libro**

```text
Evento → Cola → Event Mediator ─┬→ Pagos ──────→ guarda el cobro
                                ├→ Inventario ─→ actualiza el stock
                                └→ Envíos ─────→ registra el envío
```

El mediador coordina los pasos, y cada procesador puede leer o guardar datos para hacer su trabajo.

La base puede organizarse de distintas formas, por ejemplo:

- **Compartida:** todos los procesadores usan la misma base.
- **Separada:** cada procesador o grupo de procesadores usa la suya.

**Por qué los otros diagramas sí la muestran**

En esos estilos, la base es parte de lo que los distingue:

| Estilo | Qué muestra el diagrama |
| --- | --- |
| **Basada en servicios** | Una base única compartida |
| **Solicitud-respuesta** | Una base compartida por los processors |
| **Microservicios** | Una base por servicio |
| **Eventos (Broker o Mediador)** | No dibuja la base porque se enfoca en los eventos |

**Para el parcial:** si un caso dice "Event Mediator" o "cola de eventos", identificalo por la **coordinación**, no por la base de datos.
[Timestamp: 2026/11/06 19:36:59]

**user**: la capa API en basada en servicios iria entre UI y Servicio?
[Timestamp: 2026/11/06 21:15:09]

**ai**: **Sí, exacto.** La capa API va **entre la interfaz de usuario y los servicios**, y es opcional en este estilo:

```text
Interfaz de usuario
        ↓
Capa API (proxy o gateway)
   ↓       ↓        ↓
Ventas  Inventario  Envíos
   ↓       ↓        ↓
     BD compartida
```

La interfaz le envía la solicitud a la capa API, y esta la dirige al servicio que corresponde. Por ejemplo, una solicitud a `/ventas` iría al servicio `Ventas`.

La base de datos no cambia: los servicios la siguen usando directamente, sin pasar por esta capa. Si la interfaz está dividida en varias, como tu nota contempla, todas pueden pasar por la misma capa API.
[Timestamp: 2026/11/06 21:15:09]

**user**: que hace esa capa
[Timestamp: 2026/11/06 21:15:20]

**ai**: Su trabajo principal es **recibir las solicitudes de la interfaz y enviarlas al servicio correcto**. Según cómo esté configurada, también puede hacer controles y tareas comunes antes de reenviarlas.

**Qué puede hacer**

- **Dirigir solicitudes:** envía `/ventas` a `Ventas` y `/envios` a `Envíos`.
- **Controlar el acceso:** verifica que el usuario haya iniciado sesión y tenga permiso.
- **Limitar el uso:** frena a un cliente que envía demasiadas solicitudes en poco tiempo.
- **Registrar actividad:** deja constancia de qué se pidió y si funcionó.
- **Repartir la carga:** si hay varias copias de `Ventas`, reparte las solicitudes entre ellas.

**Ejemplo: alguien compra un libro**

1. La interfaz envía la solicitud a `/ventas`.
2. La capa API verifica que el usuario haya iniciado sesión.
3. Registra la solicitud.
4. La reenvía a `Ventas`.
5. `Ventas` procesa la compra y responde.
6. La capa API le devuelve esa respuesta a la interfaz.

**Qué no debería hacer:** las reglas del negocio, como calcular el total o decidir si hay stock suficiente, van en los servicios. Esta capa se ocupa de que la solicitud llegue al lugar correcto y de las tareas comunes.
[Timestamp: 2026/11/06 21:15:20]

**user**: y si no hay capa API como la UI sabe a que servicio enviar
[Timestamp: 2026/11/06 21:16:22]

**ai**: **La interfaz tiene configuradas las direcciones de los servicios** y elige a cuál llamar según lo que quiere hacer el usuario. Por ejemplo:

```javascript
const VENTAS_URL = "https://ventas.mitienda.com";
const ENVIOS_URL = "https://envios.mitienda.com";

// El usuario aprieta "Comprar"
fetch(`${VENTAS_URL}/compras`, {
  method: "POST",
  body: JSON.stringify(compra)
});

// El usuario aprieta "Ver envío"
fetch(`${ENVIOS_URL}/envios/25`);
```

No lo descubre sola: el programador define **qué acción llama a qué servicio**. Las direcciones suelen estar en un archivo de configuración, para no tener que buscarlas por todo el código.

```text
Comprar   → Ventas
Ver stock → Inventario
Ver envío → Envíos
```

**La desventaja:** la interfaz queda más acoplada a los servicios, porque tiene que conocer sus direcciones. Si `Ventas` cambia de dirección o se divide en dos, hay que actualizar la interfaz. Además, tareas como controlar el acceso quedan en cada servicio, si no las centraliza otro componente.

Con una capa API, la interfaz solo necesita conocer esa entrada, y la capa se encarga de saber dónde está cada servicio.
[Timestamp: 2026/11/06 21:16:22]