---
tags:
  - diseño-sistemas
  - parcial-2
  - unidad-5
  - patrones
  - persistencia
  - v2
unidad: "5 (práctica)"
fuente: "Parcial 2 - Contenido/Unidad 5/Presentacion práctica DAO y DTO.pdf"
version_anterior: "[[U5 - Práctica DAO y DTO]]"
---
# U5 — Diagrama de clases, DAO y DTO

← [[U5.5 - Arquitectura (V2)]] · [[U5 - Índice (V2)]]

> [!abstract] DAO y DTO en 4 frases
> 1. **Tesis de la clase:** *"cada clase debería tener una sola razón para cambiar"* ([[U5.4 - SOLID (V2)#S — Responsabilidad Única|SRP]]).
> 2. **DTO** = **una valija**: solo **transporta datos**. No piensa, no decide, no tiene lógica.
> 3. **DAO** = **el empleado del depósito**: el **único** que habla con la base de datos. Se define como **interfaz** → eso es **Inversión de Dependencias**.
> 4. **El DAO devuelve entidades**; el **gestor** arma el DTO que necesita cada pantalla.

---

## 1. El problema

Si la clase `Libro` cambia porque **cambió la base de datos** *y además* porque **cambió el diseño de la pantalla**, tiene **dos responsabilidades**. Se separan así:

| Responsabilidad | Quién |
| --- | --- |
| Datos y reglas del negocio | **Entidad** (`Libro`) |
| Hablar con la base de datos | **DAO** (`LibroDAO`) |
| Llevar datos a la pantalla | **DTO** (`LibroDTO`) |
| Orquestar el caso de uso | **Gestor** (`GestorLibros`) |

![[U5v2 - DAO DTO capas.png]]

---

## 2. DTO - Data Transfer Object

**Objeto de transferencia de datos.** Solo atributos con getters y setters: **sin lógica de negocio y sin conexión a la BD**. *"Es casi aburrido. Ese es el punto."*

**¿Para qué, si ya tengo la entidad?**
- **Filtrar:** si la tabla tiene `precio_costo` (dato interno) y mandás la entidad entera a la UI, ese dato **viaja al navegador** y cualquiera lo ve con el inspector. El DTO es la valija que armás **a propósito** con solo lo que querés que viaje.
- Transmitir información **entre cliente y servidor** con estructuras **independientes del modelo de datos**.
- Armar las **"vistas"** que necesita cada cliente: de un mismo objeto de negocio salen **varios DTO**.
- Controlar el **formato, los nombres y los tipos** de lo que se transmite.
- Si el modelo cambia, **el cliente no se entera** (bajo acoplamiento).

> [!example] Ejemplo del apunte - Candidato
> De la entidad `Candidato` (id, nombre, apellido, fecha de nacimiento, promedio, universidad, dirección, fecha de egreso, historial académico) salen:
> - `CandidatoResumenDTO` (búsqueda y listado): id, nombre, apellido.
> - `CandidatoOrdenDeMeritoDTO` (orden de mérito): nombre, apellido, promedio, fecha de egreso.
>
> *"El DTO es una **vista filtrada** del modelo de dominio: expone **solo** los datos que necesita un caso de uso."*

> [!danger] Regla de oro
> Si un DTO tiene un método que **calcula, valida o llama a otra clase**, **dejó de ser un DTO** (y probablemente esté mal diseñado).

---

## 3. DAO - Data Access Object

**Objeto de acceso a datos.** Hay muchos tipos de bases (relacionales, documentales como MongoDB, de grafos, clave-valor, columnares) y **esa variedad no debe afectar a la lógica del software**. Objetivos: **bajar el acoplamiento** y **disminuir el impacto de los cambios**.

> [!quote] Definición
> Objeto que **encapsula la lógica** necesaria para llevar los datos desde las clases del dominio (**capa de negocio**) hacia la persistencia (**capa de datos**) y viceversa. Ofrece operaciones **CRUD**: **añadir, buscar, actualizar y borrar**.

```java
public interface LibroDAO {            // es una INTERFAZ, no una clase
    Libro buscarPorIsbn(String isbn);  // devuelve la ENTIDAD
    List<Libro> listarTodos();
    void guardar(Libro libro);
    void actualizarStock(String isbn, int nuevoStock);
    void eliminar(String isbn);
}
// Implementaciones: LibroDAOMySQL, LibroDAOMongo, LibroDAOFake (datos en memoria, para tests)
```

**¿Por qué interfaz?** Porque permite **varias implementaciones** y el resto del sistema **nunca se entera** de cuál se usa. Eso es **Inversión de Dependencias**: la lógica de negocio depende de una **abstracción**. Consecuencias:
1. Se **cambia la base de datos** sin tocar el resto.
2. Se **testea la lógica** sin una base real corriendo (con el Fake).
3. Se puede **desarrollar en paralelo** mientras infraestructura elige el motor.

---

## 4. Error típico - el DAO devuelve un DTO

`public LibroDTO buscarPorIsbn(...)` dentro del DAO **mezcla las dos responsabilidades** que se quisieron separar. El mismo libro se muestra distinto en 3 pantallas (con precio, sin precio, solo título):
- DAO devuelve un **DTO fijo** → quedás **atado** a una pantalla.
- DAO devuelve la **entidad** → el gestor **arma el DTO que quiera** en cada caso.

## 5. Pasos para implementar el patrón DAO (apunte)

1. Identificar las **clases de dominio** (*Business Objects*).
2. Implementar una **clase DTO** por cada clase de dominio a usar: solo los atributos necesarios, **sin lógica de negocio**.
3. Definir **una interfaz DAO por cada clase de dominio** con las operaciones **CRUD** y los métodos extra que hagan falta.
4. Implementar la **clase** que da el código de cada interfaz (ej. `CandidatoDAOPostgres`).

> [!warning] Ojo con el paso 2
> Dice "un DTO por clase de dominio", pero el resto de la clase (Candidato, el error típico) muestra **varios DTO por entidad, uno por pantalla o caso de uso**, y el DAO trabajando con **entidades**. Quedate con eso: **DAO ↔ entidad** y **gestor ↔ DTO ↔ UI**.

---

## 6. Lo que me confundió (y la respuesta)

| Yo pensaba… | En realidad… |
| --- | --- |
| La entidad `Libro` se relaciona con `LibroDTO` (por ejemplo, con un `toDTO()`) | **No.** La relación con el DTO la tiene el **gestor**: le pide la entidad al DAO, lee sus datos y **arma el DTO**. Ni la entidad ni el DAO conocen a los DTO. |
| ¿Por qué el DAO es una interfaz? | Porque **declara** los métodos CRUD (y las búsquedas que pidan los CU) **sin implementarlos**. Cada tipo de base de datos tiene su clase que **implementa esos mismos métodos** a su manera, y el gestor solo conoce la interfaz. |

---

## Conceptos relacionados
- [[U5.4 - SOLID (V2)]]: SRP (separar responsabilidades) y DIP (DAO como interfaz)
- [[U5.5 - Arquitectura (V2)]]: el DAO vive en la capa de persistencia y es un mecanismo de persistencia
