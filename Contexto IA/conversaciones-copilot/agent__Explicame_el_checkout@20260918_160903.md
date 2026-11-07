---
epoch: 1789758543714
mode: agent
backendId: codex
sessionId: "01a0b5eb-f56c-7cd2-86d9-fce1c4b0e01e"
agentLabel: "Explicame el checkout"
usage: '{"usedTokens":22359,"contextWindow":258400,"updatedAt":1789758689094}'
tags:
  - copilot-conversation
---

**user**: Explicame el checkout
[Timestamp: 2026/09/18 16:09:03]

**ai**: Voy a leer el PDF de la clase y explicarte `checkout` usando exactamente el contexto de tus apuntes. Para eso usaré la habilidad de lectura de PDF.La lectura integrada no está activa, así que aplico el mecanismo alternativo local para extraer el texto del mismo PDF y ubicar la sección sobre `checkout`.Según [[Diagrama de Secuencia y GIT/Clase de práctica 11_09_26 - Git.pdf]], `git checkout` se utiliza principalmente para **cambiar la versión del proyecto que tenés en tu directorio de trabajo**.

### Cambiar de rama

Si la rama ya existe localmente:

```bash
git checkout develop
```

Git mueve el proyecto al último commit de `develop`. Desde ese momento, los nuevos commits se harán en esa rama.

Para crear una rama y cambiarte a ella inmediatamente:

```bash
git checkout -b task/login
```

Esto equivale a:

```bash
git branch task/login
git checkout task/login
```

### Traer una rama remota

La forma que aparece en el PDF es:

```bash
git checkout -b <rama-local> <rama-remota>
```

Por ejemplo:

```bash
git checkout -b task/login origin/task/login
```

Esto:

- Crea la rama local `task/login`.
- La conecta con `origin/task/login`.
- Cambia tu directorio de trabajo a esa rama.

### Recuperar archivos

`checkout` también puede reemplazar un archivo modificado por la versión guardada en Git:

```bash
git checkout -- archivo.txt
```

Esto descarta los cambios no confirmados de ese archivo, por lo que hay que usarlo con cuidado.

### Comandos modernos

Actualmente Git ofrece comandos más claros para separar las dos funciones de `checkout`:

```bash
git switch develop
git switch -c task/login
git restore archivo.txt
```

En resumen: `checkout` le dice a Git **“quiero trabajar con esta rama, commit o versión de un archivo”**. Antes de cambiar de rama conviene hacer `commit` o guardar temporalmente los cambios con `git stash`, porque podrían impedir el cambio o mezclarse con la nueva rama.
[Timestamp: 2026/09/18 16:09:03]

**user**: como funcionan las ramas
[Timestamp: 2026/09/18 16:11:16]

**ai**: Las ramas de Git funcionan como **líneas de trabajo independientes** dentro del mismo proyecto. Permiten desarrollar una funcionalidad sin modificar directamente la versión principal.

Imaginá este historial:

```text
A──B──C  master
```

Cada letra representa un commit. Cuando creás una rama:

```bash
git switch -c task/login
```

Git crea un nombre que apunta al commit actual:

```text
A──B──C  master
       └ task/login
```

Al hacer nuevos commits, avanza solamente la rama activa:

```text
A──B──C  master
       \
        D──E  task/login
```

`master` permanece en `C`, mientras `task/login` contiene el trabajo nuevo.

Para volver a la rama principal:

```bash
git switch master
```

Git actualiza los archivos del directorio para mostrar la versión correspondiente a `master`.

Cuando la funcionalidad está terminada, podés integrarla:

```bash
git switch master
git merge task/login
```

El resultado sería:

```text
A──B──C──D──E  master
              task/login
```

Luego, si ya no necesitás la rama:

```bash
git branch -d task/login
```

## Ramas locales y remotas

Una rama local existe solamente en tu computadora:

```bash
git branch task/login
```

Para publicarla en el repositorio remoto:

```bash
git push -u origin task/login
```

A partir de ahí existen dos referencias relacionadas:

- `task/login`: tu rama local.
- `origin/task/login`: la última información que tenés sobre la rama remota.

## Flujo de trabajo del apunte

Según [[Diagrama de Secuencia y GIT/Clase de práctica 11_09_26 - Git.pdf]], las ramas base son `master` y `develop`, y no debería hacerse `push` directo sobre ellas.

El flujo habitual sería:

```text
master
  └── develop
        └── task/login
```

- `master`: versión estable o de producción.
- `develop`: reúne el desarrollo de la próxima versión.
- `task/login`: trabajo aislado para una funcionalidad.
- `release/...`: preparación de una versión.
- `hotfix/...`: corrección urgente que parte de `master`.

Por ejemplo:

```bash
git switch develop
git pull
git switch -c task/login

# Trabajás y confirmás cambios
git add .
git commit -m "Add user login"

# Publicás la rama
git push -u origin task/login
```

Después se realiza un merge —normalmente mediante una revisión o *pull request*— para integrar `task/login` en `develop`.

La idea fundamental es que una rama **no copia todo el proyecto**: es una referencia liviana a una secuencia de commits. Esto permite crear muchas ramas rápidamente y trabajar sin desestabilizar las ramas principales.
[Timestamp: 2026/09/18 16:11:16]