---
tags:
  - diseño-sistemas
  - parcial-2
  - unidad-6
  - indice
  - v2
version_anterior: "[[U6 - Índice]]"
---
# Unidad 6 — Pruebas e Implementación (versión 2)

← [[00 - Índice Parcial 2]] · Versión completa anterior → [[U6 - Índice]]

> [!info] Qué es esta versión
> Resumen **compacto y solo teórico** de la unidad, armado a partir de la versión completa (3 presentaciones + resumen `Parcial 2 - 2016.pdf`). No tiene ejercicios ni preguntas de examen: esos siguen en la versión anterior y en [[Banco de preguntas - Exámenes anteriores]].

| Subtema | Nota | Presentación |
| --- | --- | --- |
| 6.1 Pruebas: técnicas, inspecciones, debugging | [[U6.1 - Pruebas (V2)]] | `Unidad 6.1 - Pruebas v2.pdf` |
| 6.2 Tipos de pruebas: niveles, sistema, terminación | [[U6.2 - Tipos de Pruebas (V2)]] | `Unidad 6.2 - Tipos de Pruebas.pdf` |
| 6.3 Implementación: conversión y release | [[U6.3 - Implementación (V2)]] | `Unidad 6.3 - Implementación v2.pdf` |

> [!important] Si tenés poco tiempo, priorizá esto
> Pruebas es **el tema más preguntado** en exámenes anteriores. En orden:
> 1. **Definición de prueba**, caso exitoso y principios → [[U6.1 - Pruebas (V2)#1. Qué es probar|6.1]]
> 2. **Particiones de equivalencia y valores límite** (piden armar un lote de casos) → [[U6.1 - Pruebas (V2)#Particiones de equivalencia|6.1]]
> 3. **Plan de pruebas y criterio de terminación** → [[U6.2 - Tipos de Pruebas (V2)#7. Cuándo terminar y plan de pruebas|6.2]]
> 4. **Tipos de prueba con y sin usuarios** (aceptación, alfa, beta vs. el resto) → [[U6.2 - Tipos de Pruebas (V2)#6. Aceptación|6.2]]
> 5. **Debugging** (métodos, prueba vs. debugging) → [[U6.1 - Pruebas (V2)#5. Debugging|6.1]]
> 6. **Estrategias de conversión** (sobre todo las desventajas del paralelo) → [[U6.3 - Implementación (V2)#1. Conversión de programas|6.3]]

---

## Repaso rápido - pruebas

| Concepto | En una línea |
| --- | --- |
| Probar | Ejecutar **para encontrar errores**; caso exitoso = encuentra uno |
| Caso de prueba | Entradas + condiciones + **resultado esperado** |
| Error / defecto / falla | Persona / código / ejecución |
| Equivalencia | Válidas **combinadas**, inválidas **de a una** |
| Valores límite | Cada borde y **justo afuera**, entrada y salida |
| Cobertura | Sentencias < decisiones; condiciones no siempre cubre decisiones |
| Integración | Incremental; **descendente → stubs**, **ascendente → drivers** |
| Humo / sanidad / regresión | ¿Arranca? / ¿anda el arreglo? / ¿se rompió algo? |
| Volumen / esfuerzo / performance | Datos / pico de carga / tiempo objetivo |
| Alfa / beta | Sitio del desarrollador, presente / sitio del usuario, ausente |
| Terminar | **Combinar** métodos + errores estimados + **curva aplanada** |
| Plan | Objetivos, terminación, cronograma, responsabilidades, recursos |
| Debugging | Después de probar; ubicar (95 %) + corregir; lo hace el autor |

## Repaso rápido - implementación

| Estrategia | Riesgo | Costo | Cuándo |
| --- | --- | --- | --- |
| Total | Alto | Bajo | Simple, colapso, fecha legal |
| En paralelo | Bajo | Alto | Error inaceptable |
| Gradual | Medio | Medio | Modular |
| Prototipado | Bajo en requisitos | Medio | Requisitos difusos |
| Distribuida | Medio | Medio | Sucursales |

**Etapas:** programas, datos, procedimientos, capacitación, evaluación final · **Releases:** major.minor.patch y alpha → beta → RC → GA.
