---
tags:
  - diseño-sistemas
  - parcial-2
  - examenes
fuente: "Parcial 2 - Contenido/Exámenes/"
---
# 📝 Banco de preguntas — Exámenes anteriores

← [[00 - Índice Parcial 2]]

> [!info] De dónde sale esto
> Preguntas tomadas de los archivos de `Parcial 2 - Contenido/Exámenes/` (UTN FRSF, 2001–2017), ordenadas por unidad del programa actual.
> - **Parciales 2**: 2011 (recuperatorio) y 09/11/2017.
> - **Finales**: 02/03/2012 y 27/07/2012.
> - **Bancos de preguntas**: "Preguntas antiguas" y "Preguntas varias" (sin fecha clara, ~2001–2004).
> - `Parcial 2 - 2016.pdf` **no es un examen**: es un resumen de la teoría de **Pruebas y Debugging**. Lo uso como fuente para la [[U6 - Índice|Unidad 6]].

> [!warning] Cómo leer estas preguntas
> - El programa cambió: **patrones de diseño, SOLID y DAO/DTO no aparecen en ningún examen viejo**. Para esos temas, las preguntas de práctica las armo yo con el formato actual.
> - El **formato actual** (según los ejemplos de parcial 1 de 2026 que tenés) mezcla **múltiple opción, V/F y preguntas de desarrollo**. Los exámenes viejos eran **solo de desarrollo**.
> - **Unidad 6 (Pruebas)** es el tema **más repetido** en todos los exámenes. Prioridad alta.

## Mapa de frecuencia

| Tema | Veces que aparece | Unidad actual | Prioridad |
| --- | --- | --- | --- |
| Pruebas: plan, tipos, terminación, técnicas | 10+ | [[U6.1 - Pruebas]] / [[U6.2 - Tipos de Pruebas]] | 🔴 Alta |
| Debugging e inspecciones | 5 | [[U6.1 - Pruebas]] (sale del resumen 2016, no de las presentaciones) | 🔴 Alta |
| Modelo de diseño, relaciones, asociaciones, secuencia | 8 | [[U4.1 - Modelos de UP y Diagrama de Clases]] / [[U4 - Diagrama de Secuencia]] | 🟠 Media |
| Diagrama de estados | parcial 1 de 2026 | [[U4.3 - Máquinas de Estado]] | 🟠 Media |
| Arquitectura: capas, tiers, subsistemas, mecanismos | 5 | [[U5.5 - Arquitectura]] | 🟠 Media |
| Mantenimiento, rejuvenecimiento, conversión | 3 | [[U6.3 - Implementación]] | 🟠 Media |
| Riesgos, propuesta de sistemas, backup, seguridad | varios | ❓ verificar si siguen en el programa | ⚪ Baja |
| Patrones / SOLID / DAO-DTO | 0 | [[U5.1 - Patrones de Diseño]], [[U5.4 - SOLID]] | 🟠 Media (contenido nuevo) |

---

## Unidad 4 — Modelo de Diseño y Diagramas UML

> [!success] Respondidas
> Todas tienen respuesta en la sección de preguntas de cada nota (marcadas con 📝).

### 4.1 — Modelos de UP y clases → [[U4.1 - Modelos de UP y Diagrama de Clases#9. Preguntas tipo parcial]]
- ¿Cuántos **estereotipos** existen en el modelo de diseño? Fundamente. *(P2 2011)*
- ¿Cuál es la **composición** del modelo de diseño? *(Final 03/2012)*
- Describa las **actividades principales** para construir el modelo de diseño. *(Final 03/2012, P1 2017, 15 pts)*
- **Compare el modelo de análisis con el de diseño.** *(P1 2017)*
- Describa **todas las relaciones** entre clases y sus características. *(P2 2011, Final 03/2012, Final 07/2012)*
- En un diagrama de clases, ¿cuáles son los **elementos de una relación**? *(P1 2017)*
- Características de las **asociaciones** y de la **clase de asociación**. *(Final 03/2012, Final 07/2012)*
- ¿Qué métodos se esperan en una clase **entidad**? ¿Qué atributos en una de **control**? *(P1 2011)*
- Múltiple opción sobre el **modelo de diseño** *(ejemplo de parcial 1 de 2026)*

### 4.2 — Componentes y despliegue → [[U4.2 - Componentes y Despliegue#10. Preguntas tipo parcial]]
- ¿Qué es un **subsistema**? Ejemplifique. *(Final 03/2012)*
- Ejemplo de división en **capas físicas o tiers**. *(Final 03/2012)*

### 4.3 — Máquinas de estado → [[U4.3 - Máquinas de Estado#12. Preguntas tipo parcial]]
- Múltiple opción sobre **diagramas de estado**: estado inicial, guardas, determinismo, acciones de entrada. *(ejemplos de parcial 1 de 2026)*

### Secuencia → [[U4 - Diagrama de Secuencia#9. Preguntas tipo parcial]]
- Diferencias y coincidencias entre diagrama de **secuencia** y de **colaboración**. Dé un ejemplo. *(Final 03/2012)*

---

## Unidad 5 — Patrones, SOLID, Arquitectura

### 5.1 / 5.2 / 5.4 — Patrones y SOLID
- No hay preguntas en los exámenes viejos. Cada nota tiene su sección de práctica: [[U5.1 - Patrones de Diseño#6. Preguntas tipo parcial|5.1]], [[U5.2 - Patrones de Diseño II#Preguntas tipo parcial|5.2]], [[U5.4 - SOLID#Preguntas tipo parcial|5.4]] y [[U5 - Práctica DAO y DTO#8. Preguntas tipo parcial|DAO/DTO]].
- Relacionado y muy preguntado antes: **acoplamiento y cohesión** (tipos de cohesión: casual, lógica, temporal, de procedimiento, de comunicación, secuencial, funcional). Es la base conceptual de SOLID.

### 5.5 — Arquitectura
> [!success] Respondidas
> Estas 5 preguntas tienen respuesta desarrollada en [[U5.5 - Arquitectura#9. Preguntas de exámenes anteriores]].

- ¿Qué implica el **diseño de arquitectura**? *(P2 2011)*
- Describa la subactividad **"Identificación de los mecanismos"**. *(P2 2011)*
- ¿En qué consisten las **clases de diseño significativas para la arquitectura**? *(P2 2011)*
- Dé un ejemplo de división de componentes lógicos en **capas físicas o tiers**. *(Final 03/2012, 10 pts)*
- ¿Qué es un **subsistema**? Ejemplifique. *(Final 03/2012)*

---

## Unidad 6 — Pruebas e Implementación

### 6.1 y 6.2 — Pruebas

> [!success] Respondidas
> Todas tienen respuesta desarrollada (marcadas con 📝) en [[U6.1 - Pruebas#14. Preguntas tipo parcial]] (técnicas, inspecciones y debugging) y en [[U6.2 - Tipos de Pruebas#13. Preguntas tipo parcial]] (planes, tipos y terminación).

- Elabore un **plan de pruebas** considerando que cuenta con **tres programadores**. *(P2 2011)*
- Formule un **plan de pruebas personal** (aplicable a tu organización) y explique **en qué circunstancias lo daría por terminado**. *(P2 2017, 20 pts)*
- Defina y describa los **tipos de prueba** que conoce **con y sin usuarios presentes**. *(P2 2017, 20 pts)*
- Explique **cuándo se da por finalizada una prueba**. *(Final 07/2012)*
- Explique el método de **particiones de equivalencia** y complételo con un ejemplo. *(Final 03/2012)*
- Un programa clasifica **triángulos** en equiláteros, isósceles y escalenos. Formule el **lote de pruebas** e indique el criterio. *(Final 03/2012, 15 pts)*
- ¿**Cuándo** se usan las pruebas de **caja blanca**? *(2004 y banco de preguntas)*
- ¿Con qué **criterio** generaría un caso de prueba? *(banco)*
- Un módulo lee un archivo de **1 a 10.000 registros**. ¿Cómo lo probaría? *(banco)*
- Describa una **inspección** de software. *(banco)*
- ¿Qué **métodos de debugging** conoce? *(banco)*
- ¿Qué inconvenientes tiene el debugging por **esparcimiento de sentencias**? *(banco)*
- ¿En qué se diferencia un **caso de prueba para pruebas** de uno **para debugging**? *(banco)*

> [!bug] Respuesta incorrecta en el banco "Preguntas varias"
> Para el archivo de **1 a 10.000 registros**, el documento responde "probaría con 0, 1, 500, 1000 y 1001". **Está mal**: esos son límites de un rango de 1 a 1000.
> Con **análisis de valores límite** correcto: **0** (inválido), **1** (mínimo), **2**, **9.999**, **10.000** (máximo) y **10.001** (inválido). Se puede sumar un valor intermedio representativo de la partición válida.

### 6.3 — Implementación → [[U6.3 - Implementación#12. Preguntas tipo parcial]]

> [!warning] Fuera de la presentación
> **Mantenimiento** y **rejuvenecimiento** no están en la presentación 6.3. Las respuestas están como `Extra` en [[U6.3 - Implementación#11. Mantenimiento y rejuvenecimiento]].

- Explique los **tipos de mantenimiento** y cite ejemplos. *(Final 03/2012, Final 07/2012)*
- ¿En qué consiste el **"rejuvenecimiento del software"** y para qué sirve? *(Final 03/2012, 10 pts)*
- Nombre las **desventajas de la conversión en paralelo**. *(Final 07/2012)*

---

## ❓ Temas viejos a verificar en el programa actual

Aparecen en exámenes antiguos pero **no veo PDFs de estos temas** en tus carpetas. Preguntá a la cátedra o revisá el programa antes de estudiarlos:

- **Gestión de riesgos**: cómo se pondera un riesgo, catálogo de riesgos. *(P2 2017, 40 pts en total)*
- **Propuesta de sistemas**: objetivo, contenido, extensión y destinatarios del resumen ejecutivo. *(P2 2017)*
- **Backup**: abuela-madre-hija, incremental, diferencial, política con cinta de 4 GB. *(bancos 2001–2004)*
- **Seguridad informática**: definición, fraude vs. daño intencional, claves pública/privada, contraseñas. *(bancos 2002–2004)*

---

## Ya evaluado en el Parcial 1 (solo como referencia)
Sesgo de salidas, codificación de entradas, diseño de interfaces (Mandel), robustez/corrección/confiabilidad, clases de control y entidad, acoplamiento y cohesión.
