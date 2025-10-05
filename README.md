
# 🐍 Actividad 4 - Validaciones y bucles

Actividad de Lenguaje de programación I, de la carrera de ingeniería de software, segundo semestre. 

5 ejercicios practicos implementando validaciones, bucles y condicionales

## 📘 Información del Proyecto

- **Autor:** Katherynn Gomez 
- **GitHub:** [@KoShLaBs](https://github.com/KoShLaBs)
- **Profesor:** Ing. Johan Manuel Gordillo Mesa
- **Materia:** Lenguaje de Programación
- **Fecha:** 05 de octubre de 2025
- **Repositorio:** [ProgrammingLanguageKatG]  
- **Rama actual:** `actividadcuatro`  

---

## 1️⃣ Caja del día – Ventas hasta “cerrar”

**Objetivo:**  
Registrar ventas realizadas durante el día hasta que el cajero escriba `cerrar`.

**Instrucciones:**

- Ingresar montos de venta uno a uno.
- Solo se aceptan montos entre `1` y `1_000_000`.
- Escribe `cerrar` para finalizar el día.
- Se debe alcanzar una meta mínima de:
  - **Total ≥ 500_000**
  - **Mínimo 5 transacciones válidas**

**Salida esperada:**

- Total del día
- Número de ventas
- Ticket promedio
- Mensaje: `Meta cumplida` o `Meta no cumplida`

---

## 2️⃣ Pase de lista de empleados (turno)

**Objetivo:**  
Contar la asistencia de `N` empleados y determinar si el turno fue óptimo.

**Instrucciones:**

- Ingresar el número total de empleados (`N`).
- Por cada uno, ingresar su estado:  
  - `p`: presente  
  - `t`: tarde (pedirá justificación: `s/n`)  
  - `a`: ausente

**Reglas:**

- Se considera que un empleado **cumple** si está presente o si llega tarde con justificación (`s`).
- El turno es **óptimo** si al menos el 90% de los empleados cumplen.

**Salida esperada:**

- Número de presentes, tardes, ausentes
- Número de empleados que cumplen
- Mensaje: `Turno óptimo` o no

---

## 3️⃣ Control de calidad en línea de producción

**Objetivo:**  
Inspeccionar hasta 50 piezas en una línea de producción.

**Instrucciones:**

- Por cada pieza, ingresar:
  - `ok` si está correcta
  - `def` si tiene defecto (pedirá tipo: `leve` o `critico`)

**Reglas:**

- Si aparece una pieza con defecto **crítico**, se detiene inmediatamente la línea.

**Salida esperada:**

- Cantidad de piezas `ok`
- Defectos leves y críticos
- Estado final: si la línea fue detenida por un defecto crítico

---

## 4️⃣ Estacionamiento por horas

**Objetivo:**  
Calcular el cobro por estacionamiento de varios vehículos.

**Instrucciones:**

- Por cada vehículo, ingresar:
  - Horas estacionadas (debe ser > 0)
  - Tipo de vehículo: `oficial`, `discap`, `normal`
- Escribe `fin` para terminar.

**Reglas de cobro:**

- **Gratis** si:
  - Tipo `discap`
  - Tipo `oficial` con ≤ 0.5 horas
- Tipo `normal`:
  - Tarifa base: $3.000 por hora
  - Si supera 8 horas **o** es fin de semana (`s/n`), se aplica un tope de $20.000

**Salida esperada:**

- Monto por ticket
- Acumulado total del día
- Cantidad de vehículos con tarifa gratuita

---

## 5️⃣ Promedio de calificaciones con aprobación

**Objetivo:**  
Leer 5 notas, calcular el promedio y determinar si el estudiante aprueba.

**Instrucciones:**

- Ingresar 5 notas entre 0.0 y 5.0
- Si alguna nota es inválida, volver a solicitarla

**Reglas para aprobación:**

- Promedio **≥ 3.0**
- Ninguna nota debe ser **< 2.0**

**Salida esperada:**

- Promedio con dos decimales
- Estado: `Aprobado` o `Requiere refuerzo`
---

## 🔧 Clonar y usar este repositorio

```bash
# Clonar el repositorio
git clone https://github.com/KoShLaBs/ProgrammingLanguageKatG.git

# Entrar al directorio del proyecto
cd ProgrammingLanguageKatG

# Cambiar a la rama de ejercicios
git checkout actividadcuatro
