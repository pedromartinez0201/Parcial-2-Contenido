---
name: tp-diseno-grupo10
description: "TP Diseño de Sistemas 2026 (Grupo 10, \"Capit@l Humano\"): carpeta, entregas hechas y lo que falta (etapa 7 = implementar CU020 y CU028)"
metadata:
  node_type: memory
  type: project
  originSessionId: ced9673f-ba11-4a10-9072-8ef2fa7c98e2
  modified: 2026-11-03T18:40:16.751Z
---

TP en `~/Escritorio/TP- Diseño/` (no es repo git; solo diagramas .puml y PDFs, sin código todavía). Grupo 10. Entregas 1–6 hechas (clases `TP3-Main.puml`, secuencia CU020/021/025 en `5ta Entrega - G10/`, CU026/028 + despliegue en `Entrega 6 - Grupo 10/`).
Etapa 7 (vence 2026-11-06): implementar CU020 Gestionar Preguntas (+ CU021/022/023 que extiende) y CU028 Emitir Orden de Mérito. Final 2026-11-20.
Código en `capitalhumano/` (backend Spring Boot 3.5 + frontend HTML/JS + docker-compose; README con la lista de cambios a pasar a los diagramas). CU020 completo y probado el 2026-11-03; CU028 pendiente (las entidades ya están mapeadas, faltan DAOs de Puesto/Candidato/Cuestionario y datos de prueba de cuestionarios). Decisión de diseño: nueva clase `GrupoOpcionRespuesta` = "Opción de Respuesta" del enunciado.
Stack definido en el despliegue: backend Java 25 jar con Tomcat embebido (Spring Boot), frontend web HTML/JS/CSS, PostgreSQL, Docker.

**Why:** el enunciado exige que el código se adecúe al diseño, si no el TP no aprueba.
**How to apply:** al implementar, respetar nombres de gestores/DAO/DTO de los diagramas y anotar las inconsistencias a corregir. Relacionado: [[diseno-sistemas-parcial2]].
