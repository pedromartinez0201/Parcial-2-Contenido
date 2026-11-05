---
tags:
  - diseño-sistemas
  - parcial-2
  - unidad-5
  - indice
  - v2
version_anterior: "[[U5 - Índice]]"
---
# Unidad 5 — Patrones, SOLID y Arquitectura (versión 2)

← [[00 - Índice Parcial 2]] · Versión completa anterior → [[U5 - Índice]]

> [!info] Qué es esta versión
> Resumen **compacto y solo teórico** de la unidad, corroborado contra las 5 presentaciones. No tiene ejercicios ni preguntas de examen (esos siguen en la versión anterior y en [[Banco de preguntas - Exámenes anteriores]]).

| Subtema | Nota | Presentación |
| --- | --- | --- |
| 5.1 Patrones de diseño: qué son, State, Singleton | [[U5.1 - Patrones de Diseño (V2)]] | `Unidad 5.1 - Patrones de Diseño.pdf` |
| 5.2 Facade, Bridge, Mediator | [[U5.2 - Patrones de Diseño II (V2)]] | `Unidad 5.2 - Patrones de Diseño.pdf` |
| Práctica: DAO y DTO (la "5.3") | [[U5 - DAO y DTO (V2)]] | `Presentacion práctica DAO y DTO.pdf` |
| 5.4 SOLID | [[U5.4 - SOLID (V2)]] | `Unidad 5.4 - Solid.pdf` |
| 5.5 Arquitectura | [[U5.5 - Arquitectura (V2)]] | `Unidad 5.5 - Arquitectura-2.pdf` |

**Hilo conductor:** todo apunta a **bajo acoplamiento, alta cohesión y código fácil de extender sin romper lo que ya funciona**: a nivel de clases (patrones), de principios (SOLID) y de todo el sistema (arquitectura).

---

## Repaso rápido - patrones

| Patrón | Tipo | Problema | Idea clave |
| --- | --- | --- | --- |
| **State** | Comportamiento | Comportamiento que cambia según el estado (muchos `if/else`) | Cada estado es una clase; el contexto **delega** |
| **Singleton** | Creación | Necesito una sola instancia con acceso global | Constructor **privado** + `getInstance()` estático |
| **Facade** | Estructural | Subsistema complejo de usar | **Una puerta de entrada** simple |
| **Bridge** | Estructural | Explosión de clases por 2 dimensiones | **Composición**: abstracción + implementación |
| **Mediator** | Comportamiento | Objetos que se hablan todos con todos | **Intermediario central** |
| **DAO** | Acceso a datos (no GoF) | Lógica de negocio atada a la BD | **Interfaz** que encapsula el acceso a la BD |
| **DTO** | Transferencia (no GoF) | Exponer la entidad entera a la UI | **Valija** sin lógica, armada a medida |

## Repaso rápido - SOLID

| | Principio | Frase | Señal de violación |
| --- | --- | --- | --- |
| **S** | Responsabilidad Única | Una razón para cambiar | La clase "hace X **y** Y **y** Z" |
| **O** | Abierto-Cerrado | Extender sin modificar | `if (x is A) … else if (x is B)` |
| **L** | Sustitución de Liskov | La subclase no rompe el contrato | La subclase lanza `NotImplementedException` |
| **I** | Segregación de Interfaces | Interfaces chicas | Métodos vacíos o con `throw` porque "la interfaz lo pide" |
| **D** | Inversión de Dependencias | Depender de abstracciones | `new MySQLConnection()` dentro de la lógica de negocio |

## Repaso rápido - arquitectura

| Estilo | Clave | Mono / Distr. |
| --- | --- | --- |
| Centrado en datos | Almacén central | Mono |
| Capas | Cada capa con su función; cerradas o abiertas | Mono |
| MVC | Modelo, Vista, Controlador | Mono |
| Flujo de datos | Tubos y filtros | Mono |
| Microkernel | Núcleo + plug-ins | Mono |
| Basada en servicios | Pocos servicios grandes + BD compartida | Distr. |
| Solicitud-respuesta | Orquestador + procesadores | Distr. |
| Eventos | Broker (sin coordinador) o mediador | Distr. |
| Microservicios | Muchos servicios chicos, una BD cada uno | Distr. |

**Escalabilidad:** vertical = máquina más grande (tiene techo) · horizontal = más máquinas en cluster (más complejo).
